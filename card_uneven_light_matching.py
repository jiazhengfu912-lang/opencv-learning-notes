import sys

import cv2
import numpy as np

from result_utils import save_result_grid


# card_04 中卡号 ROI 的手动坐标
NUMBER_LEFT = 70
NUMBER_TOP = 315
NUMBER_RIGHT = 710
NUMBER_BOTTOM = 375

# 第一个数字 0 在 number_roi 中的手动模板坐标
ZERO_LEFT = 38
ZERO_TOP = 10
ZERO_RIGHT = 64
ZERO_BOTTOM = 53

# 模板匹配分数阈值与 NMS 去重阈值
MATCH_THRESHOLD = 0.90
NMS_IOU_THRESHOLD = 0.30


def apply_nms(candidate_boxes, iou_threshold):
    # 输入框格式：[left, top, right, bottom, score]
    candidate_boxes.sort(key=lambda box: box[4], reverse=True)
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

            intersection_area = (
                max(0, right - left) *
                max(0, bottom - top)
            )

            best_area = (
                (best_box[2] - best_box[0]) *
                (best_box[3] - best_box[1])
            )

            box_area = (
                (box[2] - box[0]) *
                (box[3] - box[1])
            )

            union_area = best_area + box_area - intersection_area
            iou = intersection_area / union_area

            # 重叠不严重的框可能对应另一个真实数字，进入下一轮 NMS
            if iou < iou_threshold:
                remaining_boxes.append(box)

        candidate_boxes = remaining_boxes

    return kept_boxes


image = cv2.imread("images/card_template_matching/card_04_uneven_light.png")

if image is None:
    print("Image read failed")
    raise SystemExit

# 裁出卡号区域，当前练习只处理已知位置的卡号
number_roi = image[
    NUMBER_TOP:NUMBER_BOTTOM,
    NUMBER_LEFT:NUMBER_RIGHT,
]

# CLAHE 分区域拉开数字与不均匀背景之间的亮度差异
roi_gray = cv2.cvtColor(number_roi, cv2.COLOR_BGR2GRAY)
clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8),
)
roi_enhanced = clahe.apply(roi_gray)

# 从增强后的 ROI 中取第一个 0；模板与搜索图采用相同预处理
zero_template = roi_enhanced[
    ZERO_TOP:ZERO_BOTTOM,
    ZERO_LEFT:ZERO_RIGHT,
]

# 生成每个可能位置的归一化相关系数分数
score_map = cv2.matchTemplate(
    roi_enhanced,
    zero_template,
    cv2.TM_CCOEFF_NORMED,
)

y_positions, x_positions = np.where(score_map >= MATCH_THRESHOLD)
template_height, template_width = zero_template.shape

# 将高分位置转换为原图中的候选框
candidate_boxes = []

for x, y in zip(x_positions, y_positions):
    left = x + NUMBER_LEFT
    top = y + NUMBER_TOP
    right = left + template_width
    bottom = top + template_height
    score = score_map[y, x]

    candidate_boxes.append([left, top, right, bottom, score])

# 删除同一数字周围的重复高分候选框
kept_boxes = apply_nms(candidate_boxes, NMS_IOU_THRESHOLD)

print(f"Best score: {score_map.max():.4f}")
print(f"Match count before NMS: {len(x_positions)}")
print(f"Match count after NMS: {len(kept_boxes)}")

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
        f"0: {score:.2f}",
        (left, top - 8),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        (0, 255, 0),
        1,
    )

save_result_grid(
    "docs/results/card_uneven_light_matching.jpg",
    [
        (number_roi, "Original Number ROI"),
        (roi_enhanced, "CLAHE Enhanced ROI"),
        (zero_template, "Digit Template - Zero"),
        (result, "Zero Matching Result After NMS"),
    ],
    columns=2,
)

if "--save-only" not in sys.argv:
    cv2.imshow("Original Number ROI", number_roi)
    cv2.imshow("CLAHE Enhanced ROI", roi_enhanced)
    cv2.imshow("Digit Template - Zero", zero_template)
    cv2.imshow("Zero Matching Result After NMS", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
