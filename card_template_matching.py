import sys

import cv2
import numpy as np

from result_utils import save_result_grid


# 卡号 ROI 在 card_01_clean.png 中的手动坐标
NUMBER_LEFT = 70
NUMBER_TOP = 315
NUMBER_RIGHT = 710
NUMBER_BOTTOM = 375

# 数字 1 模板在 number_roi 中的手动坐标
TEMPLATE_LEFT = 0
TEMPLATE_TOP = 0
TEMPLATE_RIGHT = 35
TEMPLATE_BOTTOM = 60

# 归一化相关系数达到该值时，认为是数字 1 的候选位置
MATCH_THRESHOLD = 0.90


image = cv2.imread("images/card_template_matching/card_01_clean.png")

if image is None:
    print("Image read failed")
    raise SystemExit

# 裁出整行卡号，减少银行名称、芯片和持卡人文字的干扰
number_roi = image[
    NUMBER_TOP:NUMBER_BOTTOM,
    NUMBER_LEFT:NUMBER_RIGHT,
]

# 从卡号 ROI 左侧的第一个数字 1 裁出模板
one_template = number_roi[
    TEMPLATE_TOP:TEMPLATE_BOTTOM,
    TEMPLATE_LEFT:TEMPLATE_RIGHT,
]

# 转为灰度图后进行模板匹配，先专注于亮度结构
roi_gray = cv2.cvtColor(number_roi, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(one_template, cv2.COLOR_BGR2GRAY)

# 计算模板在 ROI 每个可能位置的归一化相关系数
score_map = cv2.matchTemplate(
    roi_gray,
    template_gray,
    cv2.TM_CCOEFF_NORMED,
)

# 找出相似度大于等于阈值的全部候选位置
y_positions, x_positions = np.where(score_map >= MATCH_THRESHOLD)

# 在原图副本上绘制候选模板的位置
result = image.copy()
template_height, template_width = template_gray.shape

for x, y in zip(x_positions, y_positions):
    left = x + NUMBER_LEFT
    top = y + NUMBER_TOP
    right = left + template_width
    bottom = top + template_height

    cv2.rectangle(
        result,
        (left, top),
        (right, bottom),
        (0, 255, 0),
        2,
    )

print(f"Match count before duplicate removal: {len(x_positions)}")

save_result_grid(
    "docs/results/card_template_matching.jpg",
    [
        (number_roi, "Number ROI"),
        (one_template, "Digit Template - One"),
        (result, "Template Matching Result"),
    ],
    columns=2,
)

if "--save-only" not in sys.argv:
    cv2.imshow("Number ROI", number_roi)
    cv2.imshow("Digit Template - One", one_template)
    cv2.imshow("Template Matching Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
