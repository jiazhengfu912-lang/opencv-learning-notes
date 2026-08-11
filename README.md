# OpenCV 学习笔记

使用 Python 学习 OpenCV 的中文入门仓库。内容按照“理解理论 → 运行代码 → 调整参数 → 对照结果 → 复习”的路径组织，适合初学者循序学习，也适合作为后续复习索引。

[从第一章开始](docs/01-image-basics.md) · [查看完整教材目录](docs/README.md) · [环境与运行](#环境与运行)

## 你将学到

- 图像与视频的读取、显示、颜色空间和帧处理。
- ROI、像素数值运算、平滑、阈值与边界填充。
- 形态学操作、梯度、Canny 边缘与轮廓分析。
- 模板匹配、边界矩形、轮廓近似与灰度直方图。

## 学习路线

每一章都包含中文理论、可运行代码、参数说明、复习卡和运行结果。点击“结果”可直接跳到章节底部的结果拼图，无需先运行程序。

### 阶段一：图像与视频基础

| 章节 | 核心知识点 | 理论 | 代码 | 结果 |
| --- | --- | --- | --- | --- |
| 01 | 图像矩阵、像素、`shape`、BGR | [图像基础](docs/01-image-basics.md) | [read_image.py](read_image.py) | [查看结果](docs/01-image-basics.md#运行结果) |
| 02 | 视频帧、`ret/frame`、逐帧保存 | [视频读取与处理](docs/02-video-processing.md) | [read_video.py](read_video.py)、[video_write.py](video_write.py) | [查看结果](docs/02-video-processing.md#运行结果) |

### 阶段二：图像操作与预处理

| 章节 | 核心知识点 | 理论 | 代码 | 结果 |
| --- | --- | --- | --- | --- |
| 03 | ROI 坐标、切片、矩形标记、透明叠加 | [ROI 与图像叠加](docs/03-roi-and-overlay.md) | [ROI_example.py](ROI_example.py)、[image_add.py](image_add.py) | [查看结果](docs/03-roi-and-overlay.md#运行结果) |
| 04 | 饱和加减、亮度、对比度、归一化 | [数值运算](docs/04-numerical-operations.md) | [numeric_basics.py](numeric_basics.py)、[image_math.py](image_math.py) | [查看结果](docs/04-numerical-operations.md#运行结果) |
| 05 | 边界填充、均值/高斯/中值滤波、固定阈值、Otsu | [预处理：填充、平滑与阈值](docs/05-preprocessing.md) | [border_padding.py](border_padding.py)、[threshold_smoothing.py](threshold_smoothing.py) | [查看结果](docs/05-preprocessing.md#运行结果) |

### 阶段三：形态学、梯度与边缘

| 章节 | 核心知识点 | 理论 | 代码 | 结果 |
| --- | --- | --- | --- | --- |
| 06 | 结构元素、腐蚀、膨胀、开运算、闭运算 | [形态学基础](docs/06-morphology-basics.md) | [erosion.py](erosion.py)、[dilation.py](dilation.py)、[opening_closing.py](opening_closing.py) | [查看结果](docs/06-morphology-basics.md#运行结果) |
| 07 | 形态学梯度、礼帽、黑帽 | [形态学特征](docs/07-morphological-features.md) | [morphology_features.py](morphology_features.py) | [查看结果](docs/07-morphological-features.md#运行结果) |
| 08 | Sobel、Scharr、Laplacian、梯度可视化 | [图像梯度算子](docs/08-image-gradients.md) | [gradient_operators.py](gradient_operators.py) | [查看结果](docs/08-image-gradients.md#运行结果) |
| 09 | 高斯滤波、非极大值抑制、双阈值、Canny | [Canny 边缘检测](docs/09-canny-edge-detection.md) | [Canny_test.py](Canny_test.py) | [查看结果](docs/09-canny-edge-detection.md#运行结果) |

### 阶段四：目标特征分析

| 章节 | 核心知识点 | 理论 | 代码 | 结果 |
| --- | --- | --- | --- | --- |
| 10 | 边缘与轮廓、面积、边界矩形、轮廓近似 | [轮廓与几何特征](docs/10-contours-and-geometry.md) | [edge_contour_compare.py](edge_contour_compare.py)、[contour_geometry.py](contour_geometry.py) | [查看结果](docs/10-contours-and-geometry.md#运行结果) |
| 11 | 模板、匹配方法、匹配位置与得分 | [模板匹配](docs/11-template-matching.md) | [template_matching.py](template_matching.py) | [查看结果](docs/11-template-matching.md#运行结果) |
| 12 | 灰度分布、直方图统计与可视化 | [灰度直方图](docs/12-gray-histogram.md) | [histogram_gray.py](histogram_gray.py) | [查看结果](docs/12-gray-histogram.md#运行结果) |

## 如何使用本仓库

1. 从学习路线进入目标理论章节，先理解核心概念和示意图。
2. 打开对应脚本，在项目根目录运行；每次只调整一个参数，再观察变化。
3. 对照章节末尾的运行结果，确认你的输出是否符合预期。
4. 完成章节中的复习卡和自测题；需要回顾实现时，通过下方代码速查返回对应章节。

运行结果图片仅嵌入理论章节，不放在首页，以保持仓库主页加载快速、导航清晰。

## 代码速查

| 脚本 | 内容 | 所属理论章节 |
| --- | --- | --- |
| [read_image.py](read_image.py) | 读取与显示图像、查看图像形状 | [01 图像基础](docs/01-image-basics.md) |
| [read_video.py](read_video.py) | 循环读取视频帧并显示灰度效果 | [02 视频读取与处理](docs/02-video-processing.md) |
| [video_write.py](video_write.py) | 将视频帧保存为 BGR 图和灰度图 | [02 视频读取与处理](docs/02-video-processing.md) |
| [ROI_example.py](ROI_example.py) | 提取 ROI 并在原图标记区域 | [03 ROI 与图像叠加](docs/03-roi-and-overlay.md) |
| [image_add.py](image_add.py) | 使用 `addWeighted()` 半透明叠加 | [03 ROI 与图像叠加](docs/03-roi-and-overlay.md) |
| [numeric_basics.py](numeric_basics.py) | 像素、ROI 均值、亮度和对比度 | [04 数值运算](docs/04-numerical-operations.md) |
| [image_math.py](image_math.py) | 饱和加法与减法 | [04 数值运算](docs/04-numerical-operations.md) |
| [border_padding.py](border_padding.py) | 常量、复制和镜像边界填充 | [05 预处理](docs/05-preprocessing.md) |
| [threshold_smoothing.py](threshold_smoothing.py) | 平滑、固定阈值与 Otsu 阈值 | [05 预处理](docs/05-preprocessing.md) |
| [erosion.py](erosion.py) | 腐蚀操作 | [06 形态学基础](docs/06-morphology-basics.md) |
| [dilation.py](dilation.py) | 膨胀操作 | [06 形态学基础](docs/06-morphology-basics.md) |
| [opening_closing.py](opening_closing.py) | 开运算与闭运算 | [06 形态学基础](docs/06-morphology-basics.md) |
| [morphology_features.py](morphology_features.py) | 形态学梯度、礼帽和黑帽 | [07 形态学特征](docs/07-morphological-features.md) |
| [gradient_operators.py](gradient_operators.py) | Sobel、Scharr 和 Laplacian | [08 图像梯度算子](docs/08-image-gradients.md) |
| [Canny_test.py](Canny_test.py) | Canny 边缘检测 | [09 Canny 边缘检测](docs/09-canny-edge-detection.md) |
| [edge_contour_compare.py](edge_contour_compare.py) | 边缘、二值图与轮廓对比 | [10 轮廓与几何特征](docs/10-contours-and-geometry.md) |
| [contour_geometry.py](contour_geometry.py) | 边界矩形、旋转矩形与轮廓近似 | [10 轮廓与几何特征](docs/10-contours-and-geometry.md) |
| [template_matching.py](template_matching.py) | 基础模板匹配 | [11 模板匹配](docs/11-template-matching.md) |
| [histogram_gray.py](histogram_gray.py) | 灰度直方图统计与绘制 | [12 灰度直方图](docs/12-gray-histogram.md) |

## 环境与运行

### 环境要求

- Python 3
- OpenCV Contrib 5.0.0
- NumPy
- Matplotlib

### 安装

在项目根目录打开 PowerShell：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 运行示例

所有脚本都应在项目根目录 `D:\OpenCV_Learning` 中运行，确保相对路径能找到 `images/` 和 `videos/`：

```powershell
python read_video.py
```

## 目录说明

```text
docs/       中文理论教材、复习卡和运行结果图片
images/     示例输入图像
videos/     示例输入视频
*.py        可运行的 OpenCV 学习脚本
output/     程序生成结果，已被 Git 忽略
```

## 约定

- OpenCV 默认以 BGR 通道顺序读取彩色图像。
- 变量名、路径和运行输出使用英文；代码注释使用中文。
- 形态学示例通常将待分析的暗色目标转换为白色前景。
