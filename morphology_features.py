import cv2
from pathlib import Path

# 读取原始图像
image = cv2.imread("images/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 形态学特征提取通常在灰度图上进行
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 小核用于提取较细的边缘
edge_kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (5, 5)
)

# 大核用于突出相对较小的亮细节和暗细节
hat_kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (15, 15)
)

# 形态学梯度：膨胀结果减去腐蚀结果，突出边缘
gradient = cv2.morphologyEx(
    gray,
    cv2.MORPH_GRADIENT,
    edge_kernel
)

# 礼帽：原图减去开运算，突出小亮区域
top_hat = cv2.morphologyEx(
    gray,
    cv2.MORPH_TOPHAT,
    hat_kernel
)

# 黑帽：闭运算减去原图，突出小暗区域
black_hat = cv2.morphologyEx(
    gray,
    cv2.MORPH_BLACKHAT,
    hat_kernel
)

# 保存形态学特征结果
Path("output/morphology").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/morphology/gradient.jpg", gradient)
cv2.imwrite("output/morphology/top_hat.jpg", top_hat)
cv2.imwrite("output/morphology/black_hat.jpg", black_hat)

# 对比灰度图、梯度、礼帽和黑帽结果
cv2.imshow("Gray", gray)
cv2.imshow("Morphological Gradient", gradient)
cv2.imshow("Top Hat", top_hat)
cv2.imshow("Black Hat", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
