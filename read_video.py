import cv2

cap = cv2.VideoCapture("videos/test.mp4")

if not cap.isOpened():
    print("视频读取失败了：请检查一下路和文件或者视频编码是否正确")
    raise SystemExit
while True:
    ret,frame = cap.read()
    if not ret:
        break;

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Original Video",frame)
    cv2.imshow("Gray Video",gray)

    if cv2.waitKey(33)& 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
