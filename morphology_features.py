import cv2
from pathlib import  Path

image = cv2.imread("images/test.jpg")

if image is None:
    print("image read failed")
    raise SystemExit

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edge_kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (5,5)
)

hat_kernel = cv2.getStructuringElement(
    cv2.MORPH_ELLIPSE,
    (15,15)
)

gradient = cv2.morphologyEx(
    gray,
    cv2.MORPH_GRADIENT,
    edge_kernel
)

top_hat = cv2.morphologyEx(
    gray,
    cv2.MORPH_TOPHAT,
    hat_kernel
)

black_hat = cv2.morphologyEx(
    gray,
    cv2.MORPH_BLACKHAT,
    hat_kernel
)

# 创建输出目录并保存结果
Path("output/morphology").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/morphology/gradient.jpg", gradient)
cv2.imwrite("output/morphology/top_hat.jpg", top_hat)
cv2.imwrite("output/morphology/black_hat.jpg", black_hat)

# 显示结果
cv2.imshow("Gray", gray)
cv2.imshow("Morphological Gradient", gradient)
cv2.imshow("Top Hat", top_hat)
cv2.imshow("Black Hat", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()