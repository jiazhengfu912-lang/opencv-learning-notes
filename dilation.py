import cv2
from pathlib import Path

# 读取原始图像
image = cv2.imread("images/basics/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 转为灰度图并平滑，减少二值化时的噪声
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 让较暗的人物和黑猫成为白色前景
_, binary = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# 创建 5 × 5 矩形结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 膨胀会扩大白色前景区域
dilated = cv2.dilate(binary, kernel, iterations=1)

# 保存二值图与膨胀结果
Path("output/morphology").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/morphology/binary.jpg", binary)
cv2.imwrite("output/morphology/dilated.jpg", dilated)

# 显示膨胀前后的结果
cv2.imshow("Binary", binary)
cv2.imshow("Dilated", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
