import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np

from result_utils import save_result_grid


# 卡号 ROI 在 card_03_blur_noise.png 中的手动坐标
NUMBER_LEFT = 70
NUMBER_TOP = 315
NUMBER_RIGHT = 710
NUMBER_BOTTOM = 375

# 第一个数字 3 在 number_roi 中的手动模板坐标
TEMPLATE_LEFT = 0
TEMPLATE_TOP = 0
TEMPLATE_RIGHT = 35
TEMPLATE_BOTTOM = 60

# 模板匹配相似度阈值
MATCH_THRESHOLD = 0.90

# NMS 的交并比阈值，用于删除同一数字周围的重叠候选框
NMS_IOU_THRESHOLD = 0.30


image = cv2.imread("images/card_template_matching/card_03_blur_noise.png")

if image is None:
    print("Image read failed")
    raise SystemExit

# 裁出整行卡号 ROI
number_roi = image[
    NUMBER_TOP:NUMBER_BOTTOM,
    NUMBER_LEFT:NUMBER_RIGHT,
]

# 转灰度图，只分析亮度结构
roi_gray = cv2.cvtColor(number_roi, cv2.COLOR_BGR2GRAY)

# 使用小核高斯滤波，轻度压低噪声
roi_blur = cv2.GaussianBlur(
    roi_gray,
    (3, 3),
    0
)

# 局部对比度增强，让数字笔画更突出
clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

roi_enhanced = clahe.apply(roi_blur)

# 从已经预处理完成的 ROI 中裁出第一个数字 3
# 这样模板和搜索区域具有完全一致的预处理效果
template_enhanced = roi_enhanced[
    TEMPLATE_TOP:TEMPLATE_BOTTOM,
    TEMPLATE_LEFT:TEMPLATE_RIGHT,
]

# 模板在 ROI 中逐位置滑动，生成相似度分数图
score_map = cv2.matchTemplate(
    roi_enhanced,
    template_enhanced,
    cv2.TM_CCOEFF_NORMED,
)

# 找到全局最高分及其坐标
min_score, max_score, min_location, max_location = cv2.minMaxLoc(
    score_map
)

print(f"Score map shape: {score_map.shape}")
print(f"Minimum score: {min_score:.4f}")
print(f"Maximum score: {max_score:.4f}")
print(f"Best location in ROI: {max_location}")

# 输出得分最高的 10 个位置
scores_1d = score_map[0]
top_indices = np.argsort(scores_1d)[::-1][:10]

print("\nTop 10 candidate scores:")

for rank, x in enumerate(top_indices, start=1):
    score = scores_1d[x]
    print(f"{rank:02d}: x={x}, y=0, score={score:.4f}")

# 保留得分达到模板匹配阈值的候选位置
y_positions, x_positions = np.where(
    score_map >= MATCH_THRESHOLD
)

print(
    f"\nMatch count before NMS: "
    f"{len(x_positions)}"
)

# 将每个候选位置整理为：
# [left, top, right, bottom, score]
template_height, template_width = template_enhanced.shape
candidate_boxes = []

for x, y in zip(x_positions, y_positions):
    left = x + NUMBER_LEFT
    top = y + NUMBER_TOP
    right = left + template_width
    bottom = top + template_height
    score = score_map[y, x]

    candidate_boxes.append(
        [left, top, right, bottom, score]
    )

# 按匹配分数从高到低排序，让每轮优先保留最高分框
candidate_boxes.sort(
    key=lambda box: box[4],
    reverse=True,
)

# 非极大值抑制：保留最高分框，删除与它过度重叠的低分框
kept_boxes = []

while candidate_boxes:
    best_box = candidate_boxes.pop(0)
    kept_boxes.append(best_box)

    remaining_boxes = []

    for box in candidate_boxes:
        left = max(best_box[0], box[0])
        top = max(best_box[1], box[1])
        right = min(best_box[2], box[2])
        bottom = min(best_box[3], box[3])

        # 两个候选框的交集面积
        intersection_width = max(0, right - left)
        intersection_height = max(0, bottom - top)
        intersection_area = intersection_width * intersection_height

        best_area = (
            (best_box[2] - best_box[0]) *
            (best_box[3] - best_box[1])
        )

        box_area = (
            (box[2] - box[0]) *
            (box[3] - box[1])
        )

        # IoU = 交集面积 / 并集面积
        union_area = best_area + box_area - intersection_area
        iou = intersection_area / union_area

        # IoU 较小表示不太重叠，可能是另一个真实数字
        if iou < NMS_IOU_THRESHOLD:
            remaining_boxes.append(box)

    candidate_boxes = remaining_boxes

print(f"Match count after NMS: {len(kept_boxes)}")

# 在原图副本上仅绘制 NMS 后保留的最终候选框
result = image.copy()

for left, top, right, bottom, score in kept_boxes:

    cv2.rectangle(
        result,
        (left, top),
        (right, bottom),
        (0, 255, 0),
        2,
    )

    cv2.putText(
        result,
        f"3: {score:.2f}",
        (left, top - 8),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        (0, 255, 0),
        1,
    )

save_result_grid(
    "docs/results/card_blur_noise_matching.jpg",
    [
        (number_roi, "Original Number ROI"),
        (roi_blur, "Blurred Number ROI"),
        (roi_enhanced, "CLAHE Enhanced ROI"),
        (template_enhanced, "Digit Template - Three"),
        (result, "Template Matching Result"),
    ],
    columns=2,
)

# score_map 只有一行，使用曲线更适合观察各位置分数
plt.figure(figsize=(14, 4))
plt.plot(scores_1d, color="blue")
plt.axhline(
    MATCH_THRESHOLD,
    color="red",
    linestyle="--",
    label=f"Threshold = {MATCH_THRESHOLD}",
)
plt.scatter(
    x_positions,
    scores_1d[x_positions],
    color="green",
    label="Candidates",
)
plt.title("Template Matching Score Map")
plt.xlabel("Template Left Position in Number ROI")
plt.ylabel("Similarity Score")
plt.ylim(-1.0, 1.05)
plt.grid()
plt.legend()
plt.tight_layout()
plt.savefig(
    "docs/results/card_blur_noise_matching_scores.jpg",
    dpi=150,
    bbox_inches="tight",
)

if "--save-only" not in sys.argv:
    cv2.imshow("Original Number ROI", number_roi)
    cv2.imshow("Blurred Number ROI", roi_blur)
    cv2.imshow("CLAHE Enhanced ROI", roi_enhanced)
    cv2.imshow("Digit Template - Three", template_enhanced)
    cv2.imshow("Template Matching Result", result)
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    plt.close()
