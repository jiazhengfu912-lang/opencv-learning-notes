import cv2
from pathlib import Path

# 读取原始图像
image = cv2.imread("images/basics/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 阈值和滤波通常先在单通道灰度图上进行
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 使用三种平滑方法减少局部噪声
mean_blur = cv2.blur(gray, (5, 5))
gaussian_blur = cv2.GaussianBlur(gray, (5, 5), 0)
median_blur = cv2.medianBlur(gray, 5)

# 固定阈值：亮度大于 160 的像素变为白色
_, binary = cv2.threshold(
    gaussian_blur,
    160,
    255,
    cv2.THRESH_BINARY
)

# 反向固定阈值：亮度较低的像素变为白色
_, binary_inv = cv2.threshold(
    gaussian_blur,
    160,
    255,
    cv2.THRESH_BINARY_INV
)

# Otsu 根据灰度直方图自动选择全局阈值
otsu_value, binary_otsu = cv2.threshold(
    gaussian_blur,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print(f"Otsu threshold: {otsu_value}")

# 保存平滑和阈值处理结果
Path("output/threshold").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/threshold/gray.jpg", gray)
cv2.imwrite("output/threshold/mean_blur.jpg", mean_blur)
cv2.imwrite("output/threshold/gaussian_blur.jpg", gaussian_blur)
cv2.imwrite("output/threshold/median_blur.jpg", median_blur)
cv2.imwrite("output/threshold/binary.jpg", binary)
cv2.imwrite("output/threshold/binary_inv.jpg", binary_inv)
cv2.imwrite("output/threshold/binary_otsu.jpg", binary_otsu)

# 对比原图、平滑结果和二值图
cv2.imshow("Original", image)
cv2.imshow("Gray", gray)
cv2.imshow("Mean Blur", mean_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Binary", binary)
cv2.imshow("Binary Inverse", binary_inv)
cv2.imshow("Binary Otsu", binary_otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
