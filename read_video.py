import cv2

# 打开本地视频文件
cap = cv2.VideoCapture("videos/test.mp4")

if not cap.isOpened():
    print("Video open failed")
    raise SystemExit

# 获取视频帧率，并换算每帧显示的等待时间
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps) if fps > 0 else 33

while True:
    # ret 表示是否读取成功，frame 是当前 BGR 视频帧
    ret, frame = cap.read()

    # 视频读完或读取失败时退出循环
    if not ret:
        break

    # 将当前彩色帧转换为单通道灰度帧
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 显示原始帧和灰度处理结果
    cv2.imshow("Original Video", frame)
    cv2.imshow("Gray Video", gray)

    # 按 q 键可提前退出视频播放
    if cv2.waitKey(delay) & 0xFF == ord("q"):
        break

# 释放视频资源并关闭窗口
cap.release()
cv2.destroyAllWindows()
