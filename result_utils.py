from pathlib import Path

import cv2
import matplotlib.pyplot as plt


def save_result_grid(output_path, panels, columns=2):
    """将多个 OpenCV 或灰度图结果保存为可嵌入 Markdown 的拼图。"""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    rows = (len(panels) + columns - 1) // columns
    figure, axes = plt.subplots(rows, columns, figsize=(12, 4 * rows))
    axes = axes.ravel() if hasattr(axes, "ravel") else [axes]

    for axis, (image, title) in zip(axes, panels):
        if image.ndim == 2:
            axis.imshow(image, cmap="gray", vmin=0, vmax=255)
        else:
            axis.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        axis.set_title(title)
        axis.axis("off")

    for axis in axes[len(panels):]:
        axis.axis("off")

    figure.tight_layout()
    figure.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(figure)

    print(f"Saved result: {output_path}")
