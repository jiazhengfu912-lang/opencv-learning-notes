# OpenCV 学习笔记

这是一个使用 Python 学习 OpenCV 的中文入门仓库。仓库保留了可直接运行的示例代码，并新增按学习顺序编排的理论章节，适合边运行、边理解、边复习。

## 从教材开始

从 [OpenCV 初学者教材目录](docs/README.md) 进入。建议按章节顺序学习：先读理论和图示，再打开对应脚本运行、修改参数并观察变化。

## 学习地图

| 章节 | 主题 | 对应代码 |
| --- | --- | --- |
| [01](docs/01-image-basics.md) | 图像基础：矩阵、像素、BGR | [read_image.py](read_image.py) |
| [02](docs/02-video-processing.md) | 视频读取与逐帧保存 | [read_video.py](read_video.py)、[video_write.py](video_write.py) |
| [03](docs/03-roi-and-overlay.md) | ROI、矩形标记、透明叠加 | [ROI_example.py](ROI_example.py)、[image_add.py](image_add.py) |
| [04](docs/04-numerical-operations.md) | 数值运算、亮度、对比度、归一化 | [numeric_basics.py](numeric_basics.py)、[image_math.py](image_math.py) |
| [05](docs/05-preprocessing.md) | 边界填充、平滑、阈值 | [border_padding.py](border_padding.py)、[threshold_smoothing.py](threshold_smoothing.py) |
| [06](docs/06-morphology-basics.md) | 腐蚀、膨胀、开运算、闭运算 | [erosion.py](erosion.py)、[dilation.py](dilation.py)、[opening_closing.py](opening_closing.py) |
| [07](docs/07-morphological-features.md) | 形态学梯度、礼帽、黑帽 | [morphology_features.py](morphology_features.py) |
| [08](docs/08-image-gradients.md) | Sobel、Scharr、Laplacian 梯度 | [gradient_operators.py](gradient_operators.py) |

## 环境要求

- Python 3.10 或更高版本
- OpenCV：`opencv-python`
- NumPy：`numpy`
- Matplotlib：`matplotlib`
- VS Code + Python 扩展

## 安装与运行

在项目根目录打开 PowerShell：

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install opencv-python numpy matplotlib
```

激活虚拟环境后，运行任意示例：

```powershell
python read_image.py
python threshold_smoothing.py
```

如果 VS Code 没有使用虚拟环境：按 `Ctrl+Shift+P`，选择 `Python: Select Interpreter`，再选择项目中的 `.venv\Scripts\python.exe`。

## 目录说明

```text
.
├── docs/                 # 中文理论教材与学习导航
├── images/               # 示例图片
├── videos/               # 示例视频
├── output/               # 脚本运行生成的结果（已忽略）
├── *.py                  # 14 个可运行的 OpenCV 示例
└── README.md             # 仓库首页
```

## 代码约定

- 脚本在项目根目录运行，相对路径以根目录为基准。
- 图像默认以 BGR 顺序读入；显示、保存和处理时应注意颜色空间。
- 图像读取失败会主动退出并显示提示。
- 视频窗口中按 `q` 可退出播放。
- `output/` 是生成结果，不提交到 Git。
