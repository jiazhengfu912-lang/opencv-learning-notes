# 02 视频读取与处理

[上一章：图像基础](01-image-basics.md) · [教材目录](README.md) · [下一章：ROI 与图像叠加](03-roi-and-overlay.md)

## 学习目标与前置知识

- 理解视频是按时间连续排列的图像帧。
- 掌握 `ret, frame = cap.read()` 的返回含义。
- 会按原帧率播放视频，并将 BGR/灰度帧保存为图片。

前置知识：已学习图像读取、BGR 和灰度图的基本概念。

## 核心理论

视频可看成一组连续帧：

```text
frame 0 -> frame 1 -> frame 2 -> ... -> frame N
   t=0      t=1/FPS                    t=N/FPS
```

`cap.read()` 每执行一次就尝试读取下一帧，并返回两个值：

| 返回值 | 含义 |
| --- | --- |
| `ret` | 布尔值；成功读取为 `True`，文件结束或读取失败为 `False` |
| `frame` | 成功时为当前帧 BGR 图像；失败时通常无有效图像 |

若视频帧率为 $F$，单帧显示等待时间约为：

$$delay = \frac{1000}{F}\text{ ms}$$

例如 30 FPS 对应约 33 ms。这个等待时间用于接近原播放速度；它不是图像处理本身的耗时。

## 对应实践

对应脚本：[视频读取示例](../read_video.py) · [视频逐帧保存示例](../video_write.py)

```powershell
python read_video.py
python video_write.py
```

`read_video.py` 从 `videos/test.mp4` 读取视频，显示原始 BGR 帧和灰度帧；按 `q` 退出。`video_write.py` 读取同一视频，将每一帧分别保存到 `output/bgr/` 与 `output/gray/`。

灰度转换使用：

```python
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```

若输入视频为 30 FPS 且完整读取 1 秒，在没有丢帧的情况下可保存约 30 张 BGR 图和 30 张灰度图。

## 参数速查与常见误区

| 写法 | 作用 |
| --- | --- |
| `cv2.VideoCapture(path)` | 打开视频文件或摄像头 |
| `cap.isOpened()` | 检查视频是否成功打开 |
| `cap.read()` | 读取下一帧，返回 `ret, frame` |
| `cap.get(cv2.CAP_PROP_FPS)` | 获取文件声明的帧率 |
| `cv2.waitKey(delay)` | 等待按键并控制显示节奏 |
| `cv2.imwrite(path, image)` | 将一帧保存为图像文件 |

常见误区：

- 忽略 `if not ret: break`，读到结尾后继续处理无效帧。
- 以为变量名 `ret`、`frame` 是固定关键字；它们只是常用命名。
- 用 `waitKey(0)` 播放视频，会停在第一帧；视频需要有限等待时间。

## 复习卡

关键结论：视频读取循环的结束条件来自 `ret`；`frame` 是 BGR 图；帧率决定理想显示间隔。

<details>
<summary>自测 1：为什么在处理 <code>frame</code> 前必须先判断 <code>ret</code>？</summary>

因为视频结束或读取失败时没有可用帧；继续访问会导致后续函数报错。
</details>

<details>
<summary>自测 2：30 FPS 的理论帧间隔约是多少？</summary>

约为 1000 / 30 = 33.3 ms。
</details>

<details>
<summary>自测 3：保存灰度帧前为什么要调用 <code>cvtColor</code>？</summary>

视频读取到的 `frame` 默认是 BGR 三通道；灰度帧需要按颜色权重转换为单通道图像。
</details>

[上一章：图像基础](01-image-basics.md) · [教材目录](README.md) · [下一章：ROI 与图像叠加](03-roi-and-overlay.md)
