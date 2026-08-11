# OpenCV 初学者教材

[返回学习路线首页](../README.md) · [从第一章开始](01-image-basics.md)

根目录的 [README](../README.md) 用于快速了解学习路线、对应代码和运行结果入口；本页提供完整章节目录与学习方式。每个章节都围绕仓库中已有的 19 个脚本编写，遵循同一条路线：理解概念 → 运行代码 → 调整参数 → 查看运行结果 → 回答自测题。

## 推荐学习方式

1. 按 01–12 的顺序阅读，先理解“核心理论”和 ASCII 示意图。
2. 点击章节内的脚本链接，在项目根目录运行示例。
3. 每次只调整一个参数，例如核大小、阈值或权重，再比较输出。
4. 查看章节末尾的运行结果拼图，并用复习卡确认自己能解释结果。

## 教材目录

| 顺序 | 章节 | 主要代码 |
| --- | --- | --- |
| 01 | [图像基础：矩阵、像素与 BGR](01-image-basics.md) | [read_image.py](../read_image.py) |
| 02 | [视频读取与处理](02-video-processing.md) | [read_video.py](../read_video.py)、[video_write.py](../video_write.py) |
| 03 | [ROI 与图像叠加](03-roi-and-overlay.md) | [ROI_example.py](../ROI_example.py)、[image_add.py](../image_add.py) |
| 04 | [数值运算](04-numerical-operations.md) | [numeric_basics.py](../numeric_basics.py)、[image_math.py](../image_math.py) |
| 05 | [预处理：填充、平滑与阈值](05-preprocessing.md) | [border_padding.py](../border_padding.py)、[threshold_smoothing.py](../threshold_smoothing.py) |
| 06 | [形态学基础](06-morphology-basics.md) | [erosion.py](../erosion.py)、[dilation.py](../dilation.py)、[opening_closing.py](../opening_closing.py) |
| 07 | [形态学特征](07-morphological-features.md) | [morphology_features.py](../morphology_features.py) |
| 08 | [图像梯度算子](08-image-gradients.md) | [gradient_operators.py](../gradient_operators.py) |
| 09 | [Canny 边缘检测](09-canny-edge-detection.md) | [Canny_test.py](../Canny_test.py) |
| 10 | [轮廓与几何特征](10-contours-and-geometry.md) | [edge_contour_compare.py](../edge_contour_compare.py)、[contour_geometry.py](../contour_geometry.py) |
| 11 | [模板匹配](11-template-matching.md) | [template_matching.py](../template_matching.py) |
| 12 | [灰度直方图](12-gray-histogram.md) | [histogram_gray.py](../histogram_gray.py) |

## 当前学习位置

完成一章后，可使用章节底部的“上一章 / 下一章”继续学习；最后一章可返回本目录或 [学习路线首页](../README.md)。每章末尾的运行结果拼图包含该脚本的全部 `imshow` 窗口；视频示例使用首帧作为静态代表。

## 运行前准备

在仓库根目录激活虚拟环境后执行脚本：

```powershell
.\.venv\Scripts\Activate.ps1
python read_image.py
```

完整安装步骤见 [学习路线首页的环境与运行部分](../README.md#环境与运行)。
