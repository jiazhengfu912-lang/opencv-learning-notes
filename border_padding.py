import cv2

image = cv2.imread("images/test.jpg")

if image is None:
    print("图片读取失败了")
    raise SystemExit
constant_border = cv2.copyMakeBorder(
    image,
    80,
    80,
    80,
    80,
    cv2.BORDER_CONSTANT,
    value=(0,0,0)
)

replicate_border = cv2.copyMakeBorder(
    image,
    80,
    80,
    80,
    80,
    cv2.BORDER_REPLICATE

)
reflect_border = cv2.copyMakeBorder(
    image,
    80,
    80,
    80,
    80,
    cv2.BORDER_REFLECT_101
)

cv2.imshow("Original",image)
cv2.imshow("Constant Border",constant_border)
cv2.imshow("Replicate Border",replicate_border)
cv2.imshow("Reflect Border",reflect_border)

cv2.waitKey(0)
cv2.destroyAllWindows()

