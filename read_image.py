import cv2

# 按相对路径读取 BGR 彩色图像
image = cv2.imread("images/basics/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# shape 的顺序为：高度、宽度、通道数
print("Image shape:", image.shape)

# 显示图像；按任意键后关闭窗口
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
