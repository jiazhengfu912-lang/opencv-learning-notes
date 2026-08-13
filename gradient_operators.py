import cv2
from pathlib import Path

# 读取原始图像
image = cv2.imread("images/basics/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 转为灰度图并平滑，降低噪声对梯度的影响
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 计算 Sobel 的 X、Y 方向一阶梯度
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

# 合成 Sobel 梯度幅值：sqrt(sobel_x^2 + sobel_y^2)
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)

# 取绝对值并转换为 8 位图，便于显示和保存
sobel_x_display = cv2.convertScaleAbs(sobel_x)
sobel_y_display = cv2.convertScaleAbs(sobel_y)
sobel_display = cv2.convertScaleAbs(sobel_magnitude)

# 计算 Scharr 的 X、Y 方向一阶梯度
scharr_x = cv2.Scharr(blur, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(blur, cv2.CV_64F, 0, 1)

# 合成 Scharr 梯度幅值并转换为可显示图像
scharr_magnitude = cv2.magnitude(scharr_x, scharr_y)
scharr_display = cv2.convertScaleAbs(scharr_magnitude)

# 计算 Laplacian 二阶导数并转换为可显示图像
laplacian = cv2.Laplacian(blur, cv2.CV_64F, ksize=3)
laplacian_display = cv2.convertScaleAbs(laplacian)

# 保存各类梯度结果
Path("output/gradient").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/gradient/sobel_x.jpg", sobel_x_display)
cv2.imwrite("output/gradient/sobel_y.jpg", sobel_y_display)
cv2.imwrite("output/gradient/sobel.jpg", sobel_display)
cv2.imwrite("output/gradient/scharr.jpg", scharr_display)
cv2.imwrite("output/gradient/laplacian.jpg", laplacian_display)

# 对比不同梯度算子的结果
cv2.imshow("Gray", gray)
cv2.imshow("Sobel X", sobel_x_display)
cv2.imshow("Sobel Y", sobel_y_display)
cv2.imshow("Sobel Magnitude", sobel_display)
cv2.imshow("Scharr Magnitude", scharr_display)
cv2.imshow("Laplacian", laplacian_display)

cv2.waitKey(0)
cv2.destroyAllWindows()
