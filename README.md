# OpenCV Learning Notes

English | [中文](README.zh.md)

A beginner-friendly OpenCV learning repository built with Python. The material follows a learn-by-doing path: understand the theory, run the code, adjust parameters, compare results, and review the concepts. It works both as a sequential course and as a reference for later review.

The detailed course chapters under `docs/` are currently written in Chinese.

[Start with Chapter 1](docs/01-image-basics.md) · [View the complete Chinese course index](docs/README.md) · [Environment and usage](#environment-and-usage)

## What you will learn

- Image and video loading, BGR, ROI, pixel arithmetic, smoothing, and thresholding.
- Morphology, gradients, Canny, contours, geometric features, template matching, and histograms.
- Fourier transforms, frequency-domain filtering, and low-pass/high-pass masks.
- A progressive bank-card demo covering number localization, candidate-box deduplication, digit segmentation, and rotation correction.

## Learning path

Each chapter includes Chinese theory, runnable code, parameter explanations, review cards, and execution results. Use the result link to jump to the output images at the end of a chapter.

### Stage 1: Image and video fundamentals

| Chapter | Core topics | Theory | Code | Results |
| --- | --- | --- | --- | --- |
| 01 | Image matrices, pixels, `shape`, BGR | [Image fundamentals](docs/01-image-basics.md) | [read_image.py](read_image.py) | [View results](docs/01-image-basics.md#运行结果) |
| 02 | Video frames, `ret/frame`, frame-by-frame saving | [Video reading and processing](docs/02-video-processing.md) | [read_video.py](read_video.py), [video_write.py](video_write.py) | [View results](docs/02-video-processing.md#运行结果) |

### Stage 2: Image operations and preprocessing

| Chapter | Core topics | Theory | Code | Results |
| --- | --- | --- | --- | --- |
| 03 | ROI coordinates, slicing, rectangles, alpha blending | [ROI and image overlay](docs/03-roi-and-overlay.md) | [ROI_example.py](ROI_example.py), [image_add.py](image_add.py) | [View results](docs/03-roi-and-overlay.md#运行结果) |
| 04 | Saturated arithmetic, brightness, contrast, normalization | [Numerical operations](docs/04-numerical-operations.md) | [numeric_basics.py](numeric_basics.py), [image_math.py](image_math.py) | [View results](docs/04-numerical-operations.md#运行结果) |
| 05 | Border padding, mean/Gaussian/median filtering, fixed threshold, Otsu | [Preprocessing: padding, smoothing, and thresholding](docs/05-preprocessing.md) | [border_padding.py](border_padding.py), [threshold_smoothing.py](threshold_smoothing.py) | [View results](docs/05-preprocessing.md#运行结果) |

### Stage 3: Morphology, gradients, and edges

| Chapter | Core topics | Theory | Code | Results |
| --- | --- | --- | --- | --- |
| 06 | Structuring elements, erosion, dilation, opening, closing | [Morphology fundamentals](docs/06-morphology-basics.md) | [erosion.py](erosion.py), [dilation.py](dilation.py), [opening_closing.py](opening_closing.py) | [View results](docs/06-morphology-basics.md#运行结果) |
| 07 | Morphological gradient, top-hat, black-hat | [Morphological features](docs/07-morphological-features.md) | [morphology_features.py](morphology_features.py) | [View results](docs/07-morphological-features.md#运行结果) |
| 08 | Sobel, Scharr, Laplacian, gradient visualization | [Image gradient operators](docs/08-image-gradients.md) | [gradient_operators.py](gradient_operators.py) | [View results](docs/08-image-gradients.md#运行结果) |
| 09 | Gaussian filtering, non-maximum suppression, double threshold, Canny | [Canny edge detection](docs/09-canny-edge-detection.md) | [Canny_test.py](Canny_test.py) | [View results](docs/09-canny-edge-detection.md#运行结果) |

### Stage 4: Object feature analysis

| Chapter | Core topics | Theory | Code | Results |
| --- | --- | --- | --- | --- |
| 10 | Edges and contours, area, bounding rectangles, contour approximation | [Contours and geometric features](docs/10-contours-and-geometry.md) | [edge_contour_compare.py](edge_contour_compare.py), [contour_geometry.py](contour_geometry.py) | [View results](docs/10-contours-and-geometry.md#运行结果) |
| 11 | Templates, matching methods, match locations, scores | [Template matching](docs/11-template-matching.md) | [template_matching.py](template_matching.py) | [View results](docs/11-template-matching.md#运行结果) |
| 12 | Grayscale distributions, histogram statistics, visualization | [Grayscale histogram](docs/12-gray-histogram.md) | [histogram_gray.py](histogram_gray.py) | [View results](docs/12-gray-histogram.md#运行结果) |

### Stage 5: Frequency domain and integrated practice

| Chapter | Core topics | Theory | Code | Results |
| --- | --- | --- | --- | --- |
| 13 | FFT/IFFT, spectra, low-pass/high-pass filtering, cutoff ratios | [Fourier transform and frequency-domain filtering](docs/13-fourier-transform.md) | [fourier_filter.py](fourier_filter.py) | [View results](docs/13-fourier-transform.md#运行结果) |
| 14 | CLAHE, NMS, IoU, digit segmentation, template sets, card correction | [Bank-card number template-matching practice](docs/14-card-number-template-matching.md) | [Six practice scripts](docs/14-card-number-template-matching.md#对应实践) | [View results](docs/14-card-number-template-matching.md#运行结果) |

## How to use this repository

1. Follow the learning path into a theory chapter and understand the core concepts first.
2. Open the corresponding script and run it from the repository root. Change only one parameter at a time and observe the effect.
3. Compare the output with the result images at the end of the chapter.
4. Complete the review card, then use the code reference below whenever you need to revisit an implementation.

Result images are embedded in the theory chapters rather than on the repository homepage. Newer scripts support `--save-only` to regenerate documented results without opening a window.

## Code reference

| Script | Purpose | Theory chapter |
| --- | --- | --- |
| [read_image.py](read_image.py) | Load and display an image and its `shape` | [01 Image fundamentals](docs/01-image-basics.md) |
| [read_video.py](read_video.py) | Read video frames in a loop and display a grayscale result | [02 Video reading and processing](docs/02-video-processing.md) |
| [video_write.py](video_write.py) | Save video frames as BGR and grayscale images | [02 Video reading and processing](docs/02-video-processing.md) |
| [ROI_example.py](ROI_example.py) | Extract an ROI and mark the region on the source image | [03 ROI and overlay](docs/03-roi-and-overlay.md) |
| [image_add.py](image_add.py) | Blend images with `addWeighted()` | [03 ROI and overlay](docs/03-roi-and-overlay.md) |
| [numeric_basics.py](numeric_basics.py) | Pixels, ROI averages, brightness, and contrast | [04 Numerical operations](docs/04-numerical-operations.md) |
| [image_math.py](image_math.py) | Saturated addition and subtraction | [04 Numerical operations](docs/04-numerical-operations.md) |
| [border_padding.py](border_padding.py) | Constant, replicated, and reflected border padding | [05 Preprocessing](docs/05-preprocessing.md) |
| [threshold_smoothing.py](threshold_smoothing.py) | Smoothing, fixed thresholds, and Otsu | [05 Preprocessing](docs/05-preprocessing.md) |
| [erosion.py](erosion.py) | Erosion | [06 Morphology fundamentals](docs/06-morphology-basics.md) |
| [dilation.py](dilation.py) | Dilation | [06 Morphology fundamentals](docs/06-morphology-basics.md) |
| [opening_closing.py](opening_closing.py) | Opening and closing | [06 Morphology fundamentals](docs/06-morphology-basics.md) |
| [morphology_features.py](morphology_features.py) | Morphological gradient, top-hat, and black-hat | [07 Morphological features](docs/07-morphological-features.md) |
| [gradient_operators.py](gradient_operators.py) | Sobel, Scharr, and Laplacian | [08 Image gradient operators](docs/08-image-gradients.md) |
| [Canny_test.py](Canny_test.py) | Canny edge detection | [09 Canny edge detection](docs/09-canny-edge-detection.md) |
| [edge_contour_compare.py](edge_contour_compare.py) | Compare edges, binary images, and contours | [10 Contours and geometry](docs/10-contours-and-geometry.md) |
| [contour_geometry.py](contour_geometry.py) | Bounding rectangles, minimum-area rectangles, and contour approximation | [10 Contours and geometry](docs/10-contours-and-geometry.md) |
| [template_matching.py](template_matching.py) | Basic template matching | [11 Template matching](docs/11-template-matching.md) |
| [histogram_gray.py](histogram_gray.py) | Grayscale histogram statistics and plotting | [12 Grayscale histogram](docs/12-gray-histogram.md) |
| [fourier_filter.py](fourier_filter.py) | Spectra, low-pass filtering, and high-pass filtering | [13 Fourier transform](docs/13-fourier-transform.md) |
| [card_template_matching.py](card_template_matching.py) | Match a single digit on a clear card | [14 Bank-card practice](docs/14-card-number-template-matching.md) |
| [card_low_contrast_matching.py](card_low_contrast_matching.py) | Process a low-contrast card with CLAHE | [14 Bank-card practice](docs/14-card-number-template-matching.md) |
| [card_blur_noise_matching.py](card_blur_noise_matching.py) | Blur/noise handling, score maps, and NMS | [14 Bank-card practice](docs/14-card-number-template-matching.md) |
| [card_uneven_light_matching.py](card_uneven_light_matching.py) | Uneven lighting and IoU deduplication | [14 Bank-card practice](docs/14-card-number-template-matching.md) |
| [card_number_recognition.py](card_number_recognition.py) | Recognize a complete number with a template set | [14 Bank-card practice](docs/14-card-number-template-matching.md) |
| [card_rotated_recognition.py](card_rotated_recognition.py) | Correct a rotated card and recognize its complete number | [14 Bank-card practice](docs/14-card-number-template-matching.md) |

`result_utils.py` is a shared result-composition helper for the newer scripts and is not a standalone learning chapter.

## Environment and usage

### Requirements

- Python 3
- OpenCV Contrib 5.0.0
- NumPy
- Matplotlib

### Installation

Open PowerShell in the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Example commands

Run every script from the repository root so that relative paths can find `images/` and `videos/`:

```powershell
python fourier_filter.py
python card_rotated_recognition.py
```

## Image categories

```text
images/
  basics/                 Basic loading, ROI, arithmetic, threshold, and morphology examples
  frequency/              Fourier-transform and histogram examples
  color_segmentation/     Color-segmentation practice assets
  geometry/               Contour, geometry, and perspective assets
  documents_ocr/          Document text, packaging text, and OCR practice assets
  perspective/            Perspective-correction practice assets
  ui_screenshots/         Software UI screenshots and icon assets
  Harris/                 Harris corner-detection example assets
  card_template_matching/ Bank-card template-matching practice assets and demo labels
```

## Project layout

```text
docs/         Chinese theory lessons, review cards, and execution-result images
docs/results/ Static result composites embedded in the documentation
images/       Input images grouped by learning topic
videos/       Example input videos
*.py          Runnable OpenCV learning scripts
output/       Local output from older scripts; ignored by Git
```

## Conventions

- OpenCV loads color images in BGR channel order by default.
- Variable names, paths, and runtime output use English; code comments use Chinese.
- Morphology examples generally convert dark target regions into white foreground objects.
- Do not upload real identity documents, bank cards, or private images to this public repository.
