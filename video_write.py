import cv2
from pathlib import Path
#打开视频文件
cap = cv2.VideoCapture("videos/test.mp4")
#创建输出目录；目录已存在时候不会把报错
Path("output/bgr").mkdir(parents=True,exist_ok=True)
Path("output/gray").mkdir(parents=True,exist_ok=True)
#用于给每一帧图片编号 避免保存时覆盖
frame_id = 0
#不断读取视频帧 直到视频结束
while True:
    #ret：是否读取成功；frame：当前帧的BGR图像
    ret,frame = cap.read()

    if not ret:
        break
#将当前的BGR彩色帧转换成单通道的灰度帧
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#保存原始BGR彩色图：06d表示用6位数字表示，不足的前面补0
    cv2.imwrite(f"output/bgr/{frame_id:06d}.jpg",frame)
#保存灰度图
    cv2.imwrite(f"output/gray/{frame_id:06d}.jpg",gray)
#处理下一帧前 编号加一
    frame_id+=1
#释放视频文件资源
cap.release()
#输出实际保存的帧数
print(f"已保存{frame_id}帧")
