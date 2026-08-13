import sys

import cv2
import numpy as np

from result_utils import save_result_grid


# 已校正为标准尺寸的演示卡片中，卡号区域的手动坐标
NUMBER_LEFT = 70
NUMBER_TOP = 315
NUMBER_RIGHT = 710
NUMBER_BOTTOM = 375

# card_01 是清晰参考图，其中每个位置的数字已知
REFERENCE_DIGITS = "1234567890123456"
TARGET_SIZE = (32, 48)


def preprocess_roi(image):
    # 灰度化后使用 CLAHE，减弱 card04 中局部光照不均的影响
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8),
    )
    enhanced = clahe.apply(gray)

    # Otsu 自动选择二值化阈值，数字成为白色前景
    _, binary = cv2.threshold(
        enhanced,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU,
    )

    return enhanced, binary


def find_digit_boxes(binary):
    # 只提取数字的最外层轮廓，避免 0、6、8、9 内孔被单独识别
    contours, _ = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )

    boxes = []

    for contour in contours:
        x, y, width, height = cv2.boundingRect(contour)

        # 当前卡号 ROI 高 60 像素；数字高度约 40 像素
        # 排除过小噪声、过宽背景和非数字区域
        if height < 35 or width < 8 or width > 45:
            continue

        boxes.append((x, y, width, height))

    # 卡号读取顺序由左至右，因此按 x 坐标排序
    boxes.sort(key=lambda box: box[0])

    return boxes


def normalize_digit(binary, box):
    x, y, width, height = box
    digit = binary[y:y + height, x:x + width]

    # 给笔画保留黑色边距，再统一缩放到固定大小
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
        # 相同数字出现多次时，保留第一个清晰样本作为模板
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

    recognized_digits = []
    recognition_scores = []

    for box in target_boxes:
        target_digit = normalize_digit(target_binary, box)
        best_digit = None
        best_score = -1.0

        # 单个待识别数字与 0~9 模板逐一比较，保留最高分数字
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

        recognized_digits.append(best_digit)
        recognition_scores.append(best_score)

    return target_boxes, recognized_digits, recognition_scores


reference_image = cv2.imread(
    "images/card_template_matching/card_01_clean.png"
)
target_image = cv2.imread(
    "images/card_template_matching/card_04_uneven_light.png"
)

if reference_image is None or target_image is None:
    print("Image read failed")
    raise SystemExit

# 参考卡和目标卡都在同一标准布局中，先裁出各自卡号区域
reference_roi = reference_image[
    NUMBER_TOP:NUMBER_BOTTOM,
    NUMBER_LEFT:NUMBER_RIGHT,
]
target_roi = target_image[
    NUMBER_TOP:NUMBER_BOTTOM,
    NUMBER_LEFT:NUMBER_RIGHT,
]

_, reference_binary = preprocess_roi(reference_roi)
target_enhanced, target_binary = preprocess_roi(target_roi)

# 从 card01 建立 0~9 模板库，再识别 card04 的 16 位演示号码
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

# 在原图副本上标记每一位识别结果和相似度
result = target_image.copy()

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

# 将 0~9 模板拼成一张图，便于观察模板库内容
template_strip = np.hstack(
    [digit_templates[str(digit)] for digit in range(10)]
)

save_result_grid(
    "docs/results/card_number_recognition.jpg",
    [
        (reference_binary, "Reference Binary - Card 01"),
        (target_enhanced, "Target Enhanced ROI - Card 04"),
        (target_binary, "Target Binary - Card 04"),
        (template_strip, "Digit Templates 0 To 9"),
        (result, "Card Number Recognition Result"),
    ],
    columns=2,
)

if "--save-only" not in sys.argv:
    cv2.imshow("Reference Binary - Card 01", reference_binary)
    cv2.imshow("Target Enhanced ROI - Card 04", target_enhanced)
    cv2.imshow("Target Binary - Card 04", target_binary)
    cv2.imshow("Digit Templates 0 To 9", template_strip)
    cv2.imshow("Card Number Recognition Result", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
