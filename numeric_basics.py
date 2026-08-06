import cv2
from pathlib import Path

image = cv2.imread("images/test.jpg")

if image is None:
    print("图片读取失败")
    raise SystemExit
print("图象尺寸 shape:",image.shape)
print("数据类型 dtype:",image.dtype)
print("最小像素值:",image.min())
print("最大像素值:",image.max())

x,y = 600,500
b,g,r = image[y,x]


print(f"坐标 ({x},{y})的BGR的值:",image[y,x])
print(f"B = {b},G = {g},R={r}")

cat_roi = image[850:1160,250:550]

mean_b,mean_g,mean_r,_ = cv2.mean(cat_roi)
print(f"黑猫ROI的平均BRG值为:{mean_b:.1f},{mean_g:.1f},{mean_r:.1f}")
                       

brighter = cv2.convertScaleAbs(image,alpha=1.0,beta=50)

high_contrast = cv2.convertScaleAbs(image,alpha=1.5,beta=0)

Path("output/numeric").mkdir(parents = True,exist_ok=True)

cv2.imwrite("output/numeric/brighter.jpg",brighter)
cv2.imwrite("output/numeric/high_contrast.jpg",high_contrast)

cv2.imshow("Original",image)
cv2.imshow("Brighter",brighter)
cv2.imshow("High Contrast",high_contrast)

cv2.waitKey(0)
cv2.destroyAllWindows()

