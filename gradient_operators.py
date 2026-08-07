import cv2
from pathlib import Path

# 读取原始图像
image = cv2.imread("images/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 转为灰度图并先去噪
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Sobel X 和 Sobel Y 一阶梯度
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

# 根据公式计算 Sobel 梯度幅值
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)

# 转为可显示的 8 位图像
sobel_x_display = cv2.convertScaleAbs(sobel_x)
sobel_y_display = cv2.convertScaleAbs(sobel_y)
sobel_display = cv2.convertScaleAbs(sobel_magnitude)

# Scharr X 和 Scharr Y 一阶梯度
scharr_x = cv2.Scharr(blur, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(blur, cv2.CV_64F, 0, 1)

# 根据公式计算 Scharr 梯度幅值
scharr_magnitude = cv2.magnitude(scharr_x, scharr_y)
scharr_display = cv2.convertScaleAbs(scharr_magnitude)

# Laplacian 二阶导数
laplacian = cv2.Laplacian(blur, cv2.CV_64F, ksize=3)
laplacian_display = cv2.convertScaleAbs(laplacian)

# 保存结果
Path("output/gradient").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/gradient/sobel_x.jpg", sobel_x_display)
cv2.imwrite("output/gradient/sobel_y.jpg", sobel_y_display)
cv2.imwrite("output/gradient/sobel.jpg", sobel_display)
cv2.imwrite("output/gradient/scharr.jpg", scharr_display)
cv2.imwrite("output/gradient/laplacian.jpg", laplacian_display)

# 显示结果
cv2.imshow("Gray", gray)
cv2.imshow("Sobel X", sobel_x_display)
cv2.imshow("Sobel Y", sobel_y_display)
cv2.imshow("Sobel Magnitude", sobel_display)
cv2.imshow("Scharr Magnitude", scharr_display)
cv2.imshow("Laplacian", laplacian_display)

cv2.waitKey(0)
cv2.destroyAllWindows()