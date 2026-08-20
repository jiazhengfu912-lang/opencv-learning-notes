# OpenCV 学习笔记

[English](README.md) | 中文

使用 Python 学习 OpenCV 的中文入门仓库。内容按“理解理论 → 运行代码 → 调整参数 → 对照结果 → 完成复习”的路径组织，适合初学者顺序学习，也适合后续复习。

[从第一章开始](docs/01-image-basics.md) · [查看完整教材目录](docs/README.md) · [环境与运行](#环境与运行)

## 你将学到

- 图像与视频读取、BGR、ROI、像素数值运算、平滑和阈值。
- 形态学、梯度、Canny、轮廓、几何特征、模板匹配和直方图。
- 傅里叶变换、频域滤波、低通与高通掩膜。
- 从基础模板匹配逐步完成银行卡演示号码定位、候选框去重、数字分割与旋转校正。

## 学习路线

每一章包含中文理论、可运行代码、参数说明、复习卡和运行结果。点击“结果”可跳转到章节底部的结果图。

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

### 阶段五：频域与综合实战

| 章节 | 核心知识点 | 理论 | 代码 | 结果 |
| --- | --- | --- | --- | --- |
| 13 | FFT/IFFT、频谱、低通、高通、截止比例 | [傅里叶变换与频域滤波](docs/13-fourier-transform.md) | [fourier_filter.py](fourier_filter.py) | [查看结果](docs/13-fourier-transform.md#运行结果) |
| 14 | CLAHE、NMS、IoU、数字分割、模板库、卡片校正 | [银行卡号模板匹配实战](docs/14-card-number-template-matching.md) | [6 个实战脚本](docs/14-card-number-template-matching.md#对应实践) | [查看结果](docs/14-card-number-template-matching.md#运行结果) |

## 如何使用本仓库

1. 从学习路线进入理论章节，先理解核心概念和示意图。
2. 打开对应脚本，在项目根目录运行；每次只调整一个参数，再观察变化。
3. 对照章节末尾的结果图，确认输出是否符合预期。
4. 完成复习卡；需要回顾实现时，通过下方代码速查返回理论章节。

结果图片只嵌入理论章节，不放在首页。新增脚本支持 `--save-only`，可重新生成文档结果而不弹出窗口。

## 代码速查

| 脚本 | 内容 | 所属理论章节 |
| --- | --- | --- |
| [read_image.py](read_image.py) | 读取、显示图像与 `shape` | [01 图像基础](docs/01-image-basics.md) |
| [read_video.py](read_video.py) | 循环读取视频帧并显示灰度效果 | [02 视频读取与处理](docs/02-video-processing.md) |
| [video_write.py](video_write.py) | 将视频帧保存为 BGR 图和灰度图 | [02 视频读取与处理](docs/02-video-processing.md) |
| [ROI_example.py](ROI_example.py) | 提取 ROI 并在原图标记区域 | [03 ROI 与图像叠加](docs/03-roi-and-overlay.md) |
| [image_add.py](image_add.py) | 使用 `addWeighted()` 透明叠加 | [03 ROI 与图像叠加](docs/03-roi-and-overlay.md) |
| [numeric_basics.py](numeric_basics.py) | 像素、ROI 均值、亮度和对比度 | [04 数值运算](docs/04-numerical-operations.md) |
| [image_math.py](image_math.py) | 饱和加法与减法 | [04 数值运算](docs/04-numerical-operations.md) |
| [border_padding.py](border_padding.py) | 常量、复制和镜像边界填充 | [05 预处理](docs/05-preprocessing.md) |
| [threshold_smoothing.py](threshold_smoothing.py) | 平滑、固定阈值与 Otsu | [05 预处理](docs/05-preprocessing.md) |
| [erosion.py](erosion.py) | 腐蚀 | [06 形态学基础](docs/06-morphology-basics.md) |
| [dilation.py](dilation.py) | 膨胀 | [06 形态学基础](docs/06-morphology-basics.md) |
| [opening_closing.py](opening_closing.py) | 开运算与闭运算 | [06 形态学基础](docs/06-morphology-basics.md) |
| [morphology_features.py](morphology_features.py) | 形态学梯度、礼帽与黑帽 | [07 形态学特征](docs/07-morphological-features.md) |
| [gradient_operators.py](gradient_operators.py) | Sobel、Scharr 和 Laplacian | [08 图像梯度算子](docs/08-image-gradients.md) |
| [Canny_test.py](Canny_test.py) | Canny 边缘检测 | [09 Canny 边缘检测](docs/09-canny-edge-detection.md) |
| [edge_contour_compare.py](edge_contour_compare.py) | 边缘、二值图与轮廓对比 | [10 轮廓与几何特征](docs/10-contours-and-geometry.md) |
| [contour_geometry.py](contour_geometry.py) | 边界矩形、最小旋转矩形与轮廓近似 | [10 轮廓与几何特征](docs/10-contours-and-geometry.md) |
| [template_matching.py](template_matching.py) | 基础模板匹配 | [11 模板匹配](docs/11-template-matching.md) |
| [histogram_gray.py](histogram_gray.py) | 灰度直方图统计与绘制 | [12 灰度直方图](docs/12-gray-histogram.md) |
| [fourier_filter.py](fourier_filter.py) | 频谱、低通与高通滤波 | [13 傅里叶变换](docs/13-fourier-transform.md) |
| [card_template_matching.py](card_template_matching.py) | 清晰卡片的单数字匹配 | [14 银行卡号实战](docs/14-card-number-template-matching.md) |
| [card_low_contrast_matching.py](card_low_contrast_matching.py) | CLAHE 处理低对比度卡片 | [14 银行卡号实战](docs/14-card-number-template-matching.md) |
| [card_blur_noise_matching.py](card_blur_noise_matching.py) | 模糊噪声、得分图和 NMS | [14 银行卡号实战](docs/14-card-number-template-matching.md) |
| [card_uneven_light_matching.py](card_uneven_light_matching.py) | 不均匀光照与 IoU 去重 | [14 银行卡号实战](docs/14-card-number-template-matching.md) |
| [card_number_recognition.py](card_number_recognition.py) | 模板库识别完整号码 | [14 银行卡号实战](docs/14-card-number-template-matching.md) |
| [card_rotated_recognition.py](card_rotated_recognition.py) | 旋转卡片校正与完整号码识别 | [14 银行卡号实战](docs/14-card-number-template-matching.md) |

`result_utils.py` 是新增脚本共用的结果拼图工具，不作为独立学习章节。

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

所有脚本都应在仓库根目录运行，确保相对路径能找到 `images/` 和 `videos/`：

```powershell
python fourier_filter.py
python card_rotated_recognition.py
```

## 图片目录分类

```text
images/
  basics/                 基础读取、ROI、数值运算、阈值与形态学示例
  frequency/              傅里叶变换和直方图示例
  color_segmentation/     颜色分割练习素材
  geometry/               轮廓、几何形状与透视相关素材
  documents_ocr/          文档文字、包装文字与 OCR 练习素材
  perspective/            透视校正练习素材
  ui_screenshots/         软件界面截图与图标素材
  Harris/                 Harris 角点检测示例素材
  card_template_matching/ 银行卡模板匹配实战素材与演示标签
```

## 目录说明

```text
docs/         中文理论教材、复习卡和运行结果图
docs/results/ 文档中嵌入的静态结果拼图
images/       按学习主题分类的输入图像
videos/       示例输入视频
*.py          可运行的 OpenCV 学习脚本
output/       旧脚本生成的本地结果，已被 Git 忽略
```

## 约定

- OpenCV 默认以 BGR 通道顺序读取彩色图像。
- 变量名、路径和运行输出使用英文；代码注释使用中文。
- 形态学示例通常将待分析的暗色目标转换为白色前景。
- 真实身份证件、银行卡和隐私图片不应上传到公开仓库。
