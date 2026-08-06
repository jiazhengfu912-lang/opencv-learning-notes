import cv2
import numpy as np
from pathlib import Path

image = cv2.imread("images/test.jpg")

if image is None:
    print("image read failed")
    raise SystemExit

offset = np.full_like(image,50)

add_image = cv2.add(image,offset)

subtract_image = cv2.subtract(image,offset)

Path("output/math").mkdir(parents = True,exist_ok = True)
cv2.imwrite("output/math/add_image.jpg",add_image)
cv2.imwrite("output/math/subtract_image.jpg",subtract_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Original",image)
cv2.imshow("Add 50",add_image)
cv2.imshow("Subtract 50",subtract_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

