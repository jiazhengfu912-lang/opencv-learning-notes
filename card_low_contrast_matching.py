import sys

import cv2
import numpy as np

from result_utils import save_result_grid

image = cv2.imread("images/card_template_matching/card_02_low_contrast.png")

if image is None:
    print("Image read failed")
    raise SystemExit

# card_02 仍是正面固定布局，先手动裁出卡号行
number_roi = image[315:375, 70:710]

# 从第一组卡号中的数字 2 裁出模板
two_template = number_roi[0:60, 0:35]

# 灰度化：只分析亮度结构
roi_gray = cv2.cvtColor(number_roi, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(two_template, cv2.COLOR_BGR2GRAY)

# 创建 CLAHE：局部增强数字与背景之间的亮度差异
clahe = cv2.createCLAHE(
    clipLimit=2.0,
    tileGridSize=(8, 8)
)

# 搜索图与模板必须使用同一种增强方式
roi_enhanced = clahe.apply(roi_gray)
template_enhanced = clahe.apply(template_gray)

# 在增强后的卡号 ROI 中寻找数字 2
score_map = cv2.matchTemplate(
    roi_enhanced,
    template_enhanced,
    cv2.TM_CCOEFF_NORMED
)

threshold = 0.90
y_positions, x_positions = np.where(score_map >= threshold)

result = image.copy()
template_height, template_width = template_enhanced.shape

for x, y in zip(x_positions, y_positions):
    left = x + 70
    top = y + 315
    right = left + template_width
    bottom = top + template_height

    cv2.rectangle(
        result,
        (left, top),
        (right, bottom),
        (0, 255, 0),
        2
    )

print(f"Best score: {score_map.max():.3f}")
print(f"Match count before duplicate removal: {len(x_positions)}")

save_result_grid(
    "docs/results/card_low_contrast_matching.jpg",
    [
        (number_roi, "Original Number ROI"),
        (roi_enhanced, "CLAHE Enhanced ROI"),
        (two_template, "Digit Template - Two"),
        (result, "Template Matching Result"),
    ],
    columns=2,
)

if "--save-only" not in sys.argv:
    cv2.imshow("Original Number ROI", number_roi)
    cv2.imshow("CLAHE Enhanced ROI", roi_enhanced)
    cv2.imshow("Digit Template - Two", two_template)
    cv2.imshow("Template Matching Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
