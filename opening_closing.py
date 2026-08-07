import cv2
from pathlib import Path

# 读取原始图像
image = cv2.imread("images/test.jpg")

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

# 椭圆核适合处理较平滑的目标轮廓
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

# 开运算：先腐蚀再膨胀，用于去除小白点
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# 闭运算：先膨胀再腐蚀，用于填补小黑洞和小缝隙
closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# 保存二值图、开运算和闭运算结果
Path("output/morphology").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/morphology/binary.jpg", binary)
cv2.imwrite("output/morphology/opened.jpg", opened)
cv2.imwrite("output/morphology/closed.jpg", closed)

# 显示形态学组合操作的结果
cv2.imshow("Binary", binary)
cv2.imshow("Opening", opened)
cv2.imshow("Closing", closed)

cv2.waitKey(0)
cv2.destroyAllWindows()
