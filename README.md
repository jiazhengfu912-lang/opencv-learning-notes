# OpenCV Learning Notes

Python OpenCV learning exercises, progressing from basic image and video operations to common image-processing techniques.

## Topics

- Image reading, display, and saving
- Video frame reading and frame export
- Regions of interest (ROI)
- Image arithmetic and alpha blending
- Border padding and normalization
- Thresholding and smoothing filters

## Requirements

- Python 3
- OpenCV Contrib 5.0.0
- NumPy
- Matplotlib

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run an Example

```powershell
python read_image.py
python read_video.py
python threshold_smoothing.py
```

## Project Layout

```text
images/     Input images used by the examples
videos/     Input videos used by the examples
*.py        Learning scripts
output/     Generated results (ignored by Git)
```

## Notes

OpenCV reads color images in BGR channel order by default.
