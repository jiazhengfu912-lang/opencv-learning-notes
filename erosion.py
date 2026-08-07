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
#创建一个5*5的矩阵核 输入二值图 kernel是结构元素 决定检查邻域大小与形状
eroded = cv2.erode(binary,kernel,iterations=1)

#增大腐蚀强度的方法 kernel=cv2.GetStructuringElement(cv2.MORPH_RECT(7,7))
#eroded = cv2.erode(binary,kernel,interations=1) 或者将iterations改为2
Path("output/morphology").mkdir(parents=True,exist_ok=True)
cv2.imwrite("output/morphology/binary.jpg",binary)
cv2.imwrite("output/morphology/eroded.jpg",eroded)

cv2.imshow("Binary",binary)
cv2.imshow("Eroded",eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

