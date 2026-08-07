# OpenCV 初学者教材

[返回仓库首页](../README.md)

这套章节围绕仓库中已经存在的 14 个脚本编写。每一章都遵循同一条路线：理解概念 → 运行代码 → 调整参数 → 回答自测题。

## 推荐学习方式

1. 从第一章开始，先读“核心理论”和 ASCII 示意图。
2. 点击章节中的脚本链接，在项目根目录运行示例。
3. 每次只改一个参数，例如核大小、阈值或权重，再比较输出。
4. 用章节末尾的复习卡确认自己能解释结果，而不是只会复制代码。

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

## 当前学习位置

完成一章后，直接使用章节底部的“上一章 / 下一章”继续。需要复习时，可以先从本页进入目标章节，再跳转到对应脚本定位实现。

## 运行前准备

在仓库根目录激活虚拟环境后执行脚本：

```powershell
.\.venv\Scripts\Activate.ps1
python read_image.py
```

完整安装步骤见 [仓库首页](../README.md#安装与运行)。
