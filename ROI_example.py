import cv2

# 读取原始图像
image = cv2.imread("images/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 定义黑猫区域的左上角和右下角坐标
x1, y1 = 250, 850
x2, y2 = 550, 1160

# NumPy 切片顺序是 [y, x]，因此先写上下坐标再写左右坐标
cat_roi = image[y1:y2, x1:x2]

# 复制原图，用于绘制 ROI 边框而不影响裁剪结果
display = image.copy()

# 在原图上绘制绿色 ROI 矩形
cv2.rectangle(display, (x1, y1), (x2, y2), (0, 255, 0), 3)

# 分别显示带标记的原图和裁剪区域
cv2.imshow("Original With ROI", display)
cv2.imshow("Cat ROI", cat_roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
