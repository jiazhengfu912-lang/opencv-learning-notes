import sys

import cv2
import numpy as np

from result_utils import save_result_grid


# 校正后的标准银行卡尺寸与卡号 ROI 的相对固定位置
CARD_WIDTH = 1024
CARD_HEIGHT = 640
NUMBER_LEFT = 70
NUMBER_TOP = 315
NUMBER_RIGHT = 710
NUMBER_BOTTOM = 375

# card_01 清晰参考卡中的已知演示号码，用于建立 0~9 模板库
REFERENCE_DIGITS = "1234567890123456"
TARGET_SIZE = (32, 48)


def order_points(points):
    # 将四个角点固定排序为：左上、右上、右下、左下
    ordered = np.zeros((4, 2), dtype=np.float32)
    sums = points.sum(axis=1)
    differences = np.diff(points, axis=1).ravel()

    ordered[0] = points[np.argmin(sums)]
    ordered[2] = points[np.argmax(sums)]
    ordered[1] = points[np.argmin(differences)]
    ordered[3] = points[np.argmax(differences)]

    return ordered


def find_card_corners(image):
    # card05 中卡片颜色饱和、背景接近黑灰，可用饱和度提取卡片主体
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    card_mask = cv2.inRange(
        hsv,
        (0, 50, 20),
        (179, 255, 255),
    )

    contours, _ = cv2.findContours(
        card_mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    if not contours:
        print("Card contour not found")
        raise SystemExit

    # 面积最大的高饱和度区域视为银行卡主体
    card_contour = max(contours, key=cv2.contourArea)
    rectangle = cv2.minAreaRect(card_contour)
    corners = cv2.boxPoints(rectangle)

    return order_points(corners), card_mask


def correct_card(image, source_corners):
    # 将旋转四边形映射为统一尺寸的正面银行卡矩形
    target_corners = np.float32(
        [
            [0, 0],
            [CARD_WIDTH - 1, 0],
            [CARD_WIDTH - 1, CARD_HEIGHT - 1],
            [0, CARD_HEIGHT - 1],
        ]
    )

    transform = cv2.getPerspectiveTransform(
        source_corners,
        target_corners,
    )

    return cv2.warpPerspective(
        image,
        transform,
        (CARD_WIDTH, CARD_HEIGHT),
    )


def preprocess_roi(roi):
    # CLAHE 处理局部亮度差异，再用 Otsu 得到白色数字前景
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8),
    )
    enhanced = clahe.apply(gray)

    _, binary = cv2.threshold(
        enhanced,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )

    return enhanced, binary


def find_digit_boxes(binary):
    # 只取最外层轮廓，避免 0、6、8、9 的内部孔洞被当成独立目标
    contours, _ = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    boxes = []

    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)

        # 当前标准 ROI 高 60 像素，数字高度约为 40 像素
        if height < 35 or width < 8 or width > 45:
            continue

        boxes.append((x, y, width, height))

    # 卡号的读取顺序由左至右
    boxes.sort(key=lambda box: box[0])

    return boxes


def normalize_digit(binary, box):
    x, y, width, height = box
    digit = binary[y:y + height, x:x + width]

    # 补黑色边距后统一缩放，确保模板与待识别数字尺寸一致
    digit = cv2.copyMakeBorder(
        digit,
        4,
        4,
        4,
        4,
        cv2.BORDER_CONSTANT,
        value=0,
    )

    return cv2.resize(
        digit,
        TARGET_SIZE,
        interpolation=cv2.INTER_AREA,
    )


def build_digit_templates(reference_binary):
    reference_boxes = find_digit_boxes(reference_binary)

    if len(reference_boxes) != len(REFERENCE_DIGITS):
        print(f"Reference digit count is invalid: {len(reference_boxes)}")
        raise SystemExit

    templates = {}

    for digit, box in zip(REFERENCE_DIGITS, reference_boxes):
        # 相同数字出现多次时，保留第一个样本作为该数字模板
        if digit not in templates:
            templates[digit] = normalize_digit(reference_binary, box)

    if len(templates) != 10:
        print(f"Template library is incomplete: {len(templates)} digits")
        raise SystemExit

    return templates


def recognize_digits(target_binary, templates):
    target_boxes = find_digit_boxes(target_binary)

    if len(target_boxes) != 16:
        print(f"Target digit count is invalid: {len(target_boxes)}")
        raise SystemExit

    digits = []
    scores = []

    for box in target_boxes:
        target_digit = normalize_digit(target_binary, box)
        best_digit = None
        best_score = -1.0

        # 单个数字与 0~9 模板逐一计算相似度
        for digit, template in templates.items():
            score_map = cv2.matchTemplate(
                target_digit,
                template,
                cv2.TM_CCOEFF_NORMED,
            )
            score = score_map[0, 0]

            if score > best_score:
                best_digit = digit
                best_score = score

        digits.append(best_digit)
        scores.append(best_score)

    return target_boxes, digits, scores


reference_image = cv2.imread(
    "images/card_template_matching/card_01_clean.png"
)
rotated_image = cv2.imread(
    "images/card_template_matching/card_05_rotated.png"
)

if reference_image is None or rotated_image is None:
    print("Image read failed")
    raise SystemExit

# 1. 自动找到旋转银行卡的四个角，并校正为正面标准尺寸
source_corners, card_mask = find_card_corners(rotated_image)
corrected_card = correct_card(rotated_image, source_corners)

# 2. 在校正后的银行卡中提取卡号区域
reference_roi = reference_image[
    NUMBER_TOP:NUMBER_BOTTOM,
    NUMBER_LEFT:NUMBER_RIGHT,
]
target_roi = corrected_card[
    NUMBER_TOP:NUMBER_BOTTOM,
    NUMBER_LEFT:NUMBER_RIGHT,
]

# 3. 从 card01 建立模板库，识别校正后的 card05 卡号
_, reference_binary = preprocess_roi(reference_roi)
target_enhanced, target_binary = preprocess_roi(target_roi)
digit_templates = build_digit_templates(reference_binary)
target_boxes, digits, scores = recognize_digits(
    target_binary,
    digit_templates,
)

raw_number = "".join(digits)
formatted_number = " ".join(
    raw_number[index:index + 4]
    for index in range(0, len(raw_number), 4)
)

print(f"Recognized demo number: {formatted_number}")

for index, (digit, score) in enumerate(zip(digits, scores), start=1):
    print(f"Position {index:02d}: digit={digit}, score={score:.4f}")

# 4. 在校正后的银行卡上标记每一位数字的最终识别结果
result = corrected_card.copy()

for box, digit, score in zip(target_boxes, digits, scores):
    x, y, width, height = box
    left = x + NUMBER_LEFT
    top = y + NUMBER_TOP
    right = left + width
    bottom = top + height

    cv2.rectangle(
        result,
        (left, top),
        (right, bottom),
        (0, 255, 0),
        1,
    )

    cv2.putText(
        result,
        f"{digit}:{score:.2f}",
        (left, top - 5),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.35,
        (0, 255, 0),
        1,
    )

# 将 0~9 模板拼成一张图，便于检查模板库
template_strip = np.hstack(
    [digit_templates[str(digit)] for digit in range(10)]
)

save_result_grid(
    "docs/results/card_rotated_recognition.jpg",
    [
        (rotated_image, "Rotated Card 05"),
        (card_mask, "Card Color Mask"),
        (corrected_card, "Corrected Card"),
        (target_enhanced, "Target Enhanced Number ROI"),
        (target_binary, "Target Binary Number ROI"),
        (template_strip, "Digit Templates 0 To 9"),
        (result, "Rotated Card Recognition Result"),
    ],
    columns=2,
)

if "--save-only" not in sys.argv:
    cv2.imshow("Rotated Card 05", rotated_image)
    cv2.imshow("Card Color Mask", card_mask)
    cv2.imshow("Corrected Card", corrected_card)
    cv2.imshow("Target Enhanced Number ROI", target_enhanced)
    cv2.imshow("Target Binary Number ROI", target_binary)
    cv2.imshow("Digit Templates 0 To 9", template_strip)
    cv2.imshow("Rotated Card Recognition Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
