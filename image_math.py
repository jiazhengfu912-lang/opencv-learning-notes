import cv2
import numpy as np
from pathlib import Path

# 读取原始图像
image = cv2.imread("images/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 创建与原图同尺寸、每个通道值均为 50 的偏移图像
offset = np.full_like(image, 50)

# OpenCV 饱和加法：像素值超过 255 时保持为 255
add_image = cv2.add(image, offset)

# OpenCV 饱和减法：像素值小于 0 时保持为 0
subtract_image = cv2.subtract(image, offset)

# 保存加法和减法结果
Path("output/math").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/math/add_image.jpg", add_image)
cv2.imwrite("output/math/subtract_image.jpg", subtract_image)

# 显示原图、变亮图和变暗图
cv2.imshow("Original", image)
cv2.imshow("Add 50", add_image)
cv2.imshow("Subtract 50", subtract_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
