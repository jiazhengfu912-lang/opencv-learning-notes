import cv2

# 读取原始 BGR 图像
image = cv2.imread("images/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 在四周各填充 80 像素的固定黑色边框
constant_border = cv2.copyMakeBorder(
    image,
    80,
    80,
    80,
    80,
    cv2.BORDER_CONSTANT,
    value=(0, 0, 0)
)

# 重复最外侧像素来填充边界
replicate_border = cv2.copyMakeBorder(
    image,
    80,
    80,
    80,
    80,
    cv2.BORDER_REPLICATE
)

# 以镜像方式填充边界，不重复最边缘像素
reflect_border = cv2.copyMakeBorder(
    image,
    80,
    80,
    80,
    80,
    cv2.BORDER_REFLECT_101
)

# 对比不同边界填充策略
cv2.imshow("Original", image)
cv2.imshow("Constant Border", constant_border)
cv2.imshow("Replicate Border", replicate_border)
cv2.imshow("Reflect Border", reflect_border)

cv2.waitKey(0)
cv2.destroyAllWindows()
