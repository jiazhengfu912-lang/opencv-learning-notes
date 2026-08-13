import cv2
import matplotlib.pyplot as plt

# 读取图像
image = cv2.imread("images/frequency/lena_portrait.png")

if image is None:
    print("Image read failed")
    raise SystemExit

# 转为灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 统计灰度图每个灰度值的像素数量

hist = cv2.calcHist(
    [gray],
    [0],
    None,
    [256],
    [0,256]
)

# 显示原始图像
cv2.imshow("Original", image)
cv2.imshow("Gray", gray)

# 绘制灰度直方图
plt.figure("Gray Histogram")
plt.plot(hist,color="black")
plt.xlim([0,256])
plt.xlabel("Gray Value")
plt.ylabel("Pixel Count")
plt.title("Gray Histogram")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

