# OpenCV 学习笔记

使用 Python 学习 OpenCV 的练习代码，从基础图像与视频操作逐步过渡到常用图像处理方法。

## 学习内容

- 图像的读取、显示与保存
- 视频读取与逐帧导出
- 感兴趣区域（ROI）
- 图像加减与透明叠加
- 边界填充与归一化
- 图像阈值与平滑滤波

## 环境要求

- Python 3
- OpenCV Contrib 5.0.0
- NumPy
- Matplotlib

## 安装

在 PowerShell 中执行：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 运行示例

```powershell
python read_image.py
python read_video.py
python threshold_smoothing.py
```

## 目录说明

```text
images/     示例输入图像
videos/     示例输入视频
*.py        学习脚本
output/     程序生成结果（Git 不跟踪）
```

## 说明

OpenCV 默认以 BGR 通道顺序读取彩色图像。
