import cv2
from pathlib import Path

image = cv2.imread("images/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

_, binary = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU
)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

dilated = cv2.dilate(binary,kernel,iterations=1)

Path("output/morphology").mkdir(parents=True,exist_ok=True)
cv2.imwrite("output/morphology/binary.jpg",binary)
cv2.imwrite("output/morphology/dilated.jpg",dilated)

cv2.imshow("Binary",binary)
cv2.imshow("Dilated",dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()