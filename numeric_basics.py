import cv2
from pathlib import Path

# 读取原始 BGR 图像
image = cv2.imread("images/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 查看图像矩阵的形状、数据类型和像素范围
print("Image shape:", image.shape)
print("Image dtype:", image.dtype)
print("Pixel minimum:", image.min())
print("Pixel maximum:", image.max())

# 读取坐标 (x, y) 处的 BGR 像素值
x, y = 600, 500
b, g, r = image[y, x]
print(f"Pixel at ({x}, {y}):", image[y, x])
print(f"B={b}, G={g}, R={r}")

# 裁剪黑猫区域，并计算该区域的平均 BGR 值
cat_roi = image[850:1160, 250:550]
mean_b, mean_g, mean_r, _ = cv2.mean(cat_roi)
print(f"Cat ROI mean BGR: {mean_b:.1f}, {mean_g:.1f}, {mean_r:.1f}")

# beta 增加 50，使图像整体变亮
brighter = cv2.convertScaleAbs(image, alpha=1.0, beta=50)

# alpha 大于 1，提高图像对比度
high_contrast = cv2.convertScaleAbs(image, alpha=1.5, beta=0)

# 保存数值计算结果
Path("output/numeric").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/numeric/brighter.jpg", brighter)
cv2.imwrite("output/numeric/high_contrast.jpg", high_contrast)

# 显示原图与两种数值变换结果
cv2.imshow("Original", image)
cv2.imshow("Brighter", brighter)
cv2.imshow("High Contrast", high_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()
