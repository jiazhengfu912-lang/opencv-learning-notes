import cv2
from pathlib import Path

# 打开本地视频文件
cap = cv2.VideoCapture("videos/test.mp4")

if not cap.isOpened():
    print("Video open failed")
    raise SystemExit

# 创建彩色帧和灰度帧的输出目录
Path("output/bgr").mkdir(parents=True, exist_ok=True)
Path("output/gray").mkdir(parents=True, exist_ok=True)

# 帧编号用于避免保存图片时发生覆盖
frame_id = 0

while True:
    # ret 表示读取是否成功，frame 是当前 BGR 视频帧
    ret, frame = cap.read()

    # 视频读完或读取失败时退出循环
    if not ret:
        break

    # 将当前 BGR 彩色帧转换为单通道灰度帧
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 使用六位编号保存彩色帧与灰度帧
    cv2.imwrite(f"output/bgr/{frame_id:06d}.jpg", frame)
    cv2.imwrite(f"output/gray/{frame_id:06d}.jpg", gray)

    # 处理下一帧前递增编号
    frame_id += 1

# 释放视频文件资源
cap.release()

# 输出实际保存的帧数
print(f"Saved frames: {frame_id}")
