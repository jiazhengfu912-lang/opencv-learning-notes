import sys
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np


CUTOFF_RATIO = 0.08


def create_circular_masks(height, width, cutoff_ratio):
    # 计算移位后频谱中每个位置到中心的距离
    center_y = height // 2
    center_x = width // 2
    y, x = np.ogrid[:height, :width]
    distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)

    # 截止半径随图像尺寸变化，避免固定像素值受分辨率影响
    cutoff = max(1, int(min(height, width) * cutoff_ratio))

    # 圆内保留低频，圆外保留高频
    low_mask = (distance <= cutoff).astype(np.float32)
    high_mask = 1.0 - low_mask

    return low_mask, high_mask, cutoff


def process_image(image_path):
    image = cv2.imread(str(image_path))

    if image is None:
        print(f"Image read failed: {image_path}")
        raise SystemExit

    # 转为单通道灰度图，先专注于亮度的频率变化
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    # 正向傅里叶变换，并将零频移动到频谱中心
    spectrum = np.fft.fft2(gray)
    shifted = np.fft.fftshift(spectrum)

    # 使用对数幅度谱显示频率强度
    magnitude = 20 * np.log1p(np.abs(shifted))

    low_mask, high_mask, cutoff = create_circular_masks(
        height,
        width,
        CUTOFF_RATIO,
    )

    # 在频域中分别保留低频和高频
    low_spectrum = shifted * low_mask
    high_spectrum = shifted * high_mask

    # 反移位后进行逆变换，回到空间域
    low_image = np.real(np.fft.ifft2(np.fft.ifftshift(low_spectrum)))
    high_detail = np.real(np.fft.ifft2(np.fft.ifftshift(high_spectrum)))

    low_display = np.clip(low_image, 0, 255).astype(np.uint8)

    # 高通结果包含正负细节，取绝对值并归一化后显示
    high_display = cv2.normalize(
        np.abs(high_detail),
        None,
        0,
        255,
        cv2.NORM_MINMAX,
    ).astype(np.uint8)

    panels = [
        (gray, "Original Gray", 0, 255),
        (magnitude, "Log Magnitude Spectrum", None, None),
        (low_mask, f"Low-pass Mask (r={cutoff})", 0, 1),
        (low_display, "Low-pass Result", 0, 255),
        (high_mask, f"High-pass Mask (r={cutoff})", 0, 1),
        (high_display, "High-pass Result", 0, 255),
    ]

    return panels, cutoff


def main():
    image_paths = [
        Path("images/frequency/building_facade.png"),
        Path("images/frequency/lena_portrait.png"),
    ]
    figure, axes = plt.subplots(len(image_paths), 6, figsize=(18, 10))

    for row, image_path in enumerate(image_paths):
        panels, cutoff = process_image(image_path)

        for axis, (panel, title, vmin, vmax) in zip(axes[row], panels):
            axis.imshow(panel, cmap="gray", vmin=vmin, vmax=vmax)
            axis.set_title(title)
            axis.axis("off")

        axes[row][0].set_ylabel(
            f"{image_path.stem}\ncutoff={cutoff}",
            fontsize=11,
        )

    figure.suptitle(
        f"Fourier Filtering | Cutoff Ratio: {CUTOFF_RATIO}",
        fontsize=16,
    )
    figure.tight_layout(rect=(0, 0, 1, 0.94))

    output_path = Path("docs/results/fourier_filter.jpg")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, dpi=150)
    print(f"Saved result: {output_path}")

    if "--save-only" not in sys.argv:
        plt.show()
    else:
        plt.close(figure)


if __name__ == "__main__":
    main()
