import cv2
from pathlib import Path

image = cv2.imread("images/test.jpg")

if image is None:
    print("image read failed")
    raise SystemExit

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

mean_blur = cv2.blur(gray,(5,5))
gaussian_blur = cv2.GaussianBlur(gray,(5,5),0)
median_blur = cv2.medianBlur(gray,5)


_, binary = cv2.threshold(
    gaussian_blur,
    160,
    255,
    cv2.THRESH_BINARY
)

_, binary_inv = cv2.threshold(

    gaussian_blur,
    160,
    255,
    cv2.THRESH_BINARY_INV
)

otsu_value,binary_otsu=cv2.threshold(
    gaussian_blur,
    0,
    255,
    cv2.THRESH_BINARY+cv2.THRESH_OTSU
)

print(f"otsu threshold:{otsu_value}")

Path("output/threshold").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/threshold/gray.jpg", gray)
cv2.imwrite("output/threshold/mean_blur.jpg", mean_blur)
cv2.imwrite("output/threshold/gaussian_blur.jpg", gaussian_blur)
cv2.imwrite("output/threshold/median_blur.jpg", median_blur)
cv2.imwrite("output/threshold/binary.jpg", binary)
cv2.imwrite("output/threshold/binary_inv.jpg", binary_inv)
cv2.imwrite("output/threshold/binary_otsu.jpg", binary_otsu)

# 显示处理结果
cv2.imshow("Original", image)
cv2.imshow("Gray", gray)
cv2.imshow("Mean Blur", mean_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Binary", binary)
cv2.imshow("Binary Inverse", binary_inv)
cv2.imshow("Binary Otsu", binary_otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()