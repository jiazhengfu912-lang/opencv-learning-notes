import cv2

image = cv2.imread("images/test.jpg")

if image is None:
    print("图片读取失败 请检查图片路径和文件名")
    raise SystemExit

x1,y1 = 250,500
x2,y2 = 550,1160

cat_roi = image[y1:y2,x1:x2]

display = image.copy()

cv2.rectangle(display,(x1,y1),(x2,y2),(0,0,255),4)

cv2.imshow("Original Image- Green Box Is ROI",display)
cv2.imshow("Cat ROI",cat_roi)

cv2.waitKey(0)
cv2.destroyAllWindows()

