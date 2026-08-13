import cv2

# 读取原始图像
image = cv2.imread("images/basics/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 复制原图作为叠加层，避免直接修改原图
overlay = image.copy()

# 定义黑猫区域的左上角和右下角坐标
x1, y1 = 250, 850
x2, y2 = 550, 1160

# 在叠加层绘制实心绿色 ROI 矩形
cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 255, 0), -1)

# 将绿色叠加层按 35% 透明度混合到原图
result = cv2.addWeighted(overlay, 0.35, image, 0.65, 0)

# 显示原图和半透明 ROI 叠加结果
cv2.imshow("Original", image)
cv2.imshow("Overlay", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
