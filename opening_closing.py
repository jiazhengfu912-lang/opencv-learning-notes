import cv2
from pathlib import Path

image = cv2.imread("images/test.jpg")

if image is None:
    print("image read failed")
    raise SystemExit

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

_, binary = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU
)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))

opened = cv2.morphologyEx(binary,cv2.MORPH_OPEN,kernel)

closed = cv2.morphologyEx(binary,cv2.MORPH_CLOSE,kernel)

Path("output/morphology").mkdir(parents=True,exist_ok=True)
cv2.imwrite("output/morphology/binary.jpg",binary)
cv2.imwrite("output/morphology/opened.jpg",opened)
cv2.imwrite("output/morphology/closed.jpg",closed)

cv2.imshow("binary",binary)
cv2.imshow("Opening",opened)
cv2.imshow("Closing",closed)

cv2.waitKey(0)
cv2.destroyAllWindows()
