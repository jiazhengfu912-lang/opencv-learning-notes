import cv2

image = cv2.imread("images/test.jpg")

if image is None:
    print("images read failed")
    raise SystemExit

overlay = image.copy()

x1,y1=250,850
x2,y2=550,1160
cv2.rectangle(overlay,(x1,y1),(x2,y2),(0,255,0),-1)

result = cv2.addWeighted(overlay,0.35,image,0.65,0)

cv2.imshow("Original",image)
cv2.imshow("Overlay",result)

cv2.waitKey(0)
cv2.destroyAllWindows()

