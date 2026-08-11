# OpenCV 学习笔记

使用 Python 学习 OpenCV 的可运行示例。每个脚本聚焦一个概念，按下面的顺序学习即可。

## 学习导航

| 阶段 | 示例 | 内容 |
|---|---|---|
| 1 | [read_image.py](read_image.py) | 读取、显示图像，理解 `shape` 与 BGR 图像数据。 |
| 2 | [read_video.py](read_video.py) | 循环读取视频帧、灰度化、按 `q` 退出。 |
| 3 | [video_write.py](video_write.py) | 将视频逐帧保存为 BGR 图和灰度图。 |
| 4 | [ROI_example.py](ROI_example.py) | 使用坐标和 NumPy 切片提取黑猫 ROI。 |
| 5 | [numeric_basics.py](numeric_basics.py) | 查看像素、ROI 均值、亮度和对比度。 |
| 6 | [image_math.py](image_math.py) | 使用饱和加法和减法改变图像亮度。 |
| 7 | [image_add.py](image_add.py) | 使用 `addWeighted()` 实现半透明 ROI 叠加。 |
| 8 | [border_padding.py](border_padding.py) | 对比常量、复制和镜像边界填充。 |
| 9 | [threshold_smoothing.py](threshold_smoothing.py) | 均值、高斯、中值平滑与固定/Otsu 阈值。 |
| 10 | [erosion.py](erosion.py) | 腐蚀：缩小白色前景并去除小白点。 |
| 11 | [dilation.py](dilation.py) | 膨胀：扩大白色前景并填补小黑缝。 |
| 12 | [opening_closing.py](opening_closing.py) | 开运算去白点，闭运算填黑洞。 |
| 13 | [morphology_features.py](morphology_features.py) | 形态学梯度、礼帽和黑帽。 |
| 14 | [gradient_operators.py](gradient_operators.py) | Sobel、Scharr 与 Laplacian 梯度算子。 |
| 15 | [Canny_test.py](Canny_test.py) | 高斯滤波与 Canny 边缘检测。 |
| 16 | [edge_contour_compare.py](edge_contour_compare.py) | 对比 Canny 边缘图、二值前景与轮廓。 |
| 17 | [contour_geometry.py](contour_geometry.py) | 轮廓面积、边界矩形、最小旋转矩形与轮廓近似。 |
| 18 | [template_matching.py](template_matching.py) | 使用归一化相关系数进行基础模板匹配。 |
| 19 | [histogram_gray.py](histogram_gray.py) | 灰度直方图统计与可视化。 |

GitHub 会将表格中的相对链接渲染为可点击链接。例如，点击 [read_video.py](read_video.py) 会打开视频读取示例。

## 理论教材

从 [OpenCV 初学者教材目录](docs/README.md) 进入。上方“阶段”按脚本顺序编号；教材按主题合并多个脚本，因此脚本编号与章节编号不一定相同。每个教材章节底部都嵌入了对应脚本的运行结果拼图，GitHub 可以直接查看，无需运行程序。

## 环境要求

- Python 3
- OpenCV Contrib 5.0.0
- NumPy
- Matplotlib

## 安装

在项目根目录打开 PowerShell：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 运行示例

例如运行视频读取示例：

```powershell
python read_video.py
```

所有脚本都应在项目根目录 `D:\OpenCV_Learning` 中运行，以确保相对路径能找到 `images/` 和 `videos/`。

## 目录说明

```text
images/     示例输入图像
videos/     示例输入视频
*.py        按学习主题编写的可运行脚本
output/     程序生成结果，已由 Git 忽略
```

## 约定

- OpenCV 默认以 BGR 通道顺序读取彩色图像。
- 变量名、路径和运行输出使用英文；代码注释使用中文。
- 形态学示例中，通常将待分析的暗色目标转换为白色前景。
