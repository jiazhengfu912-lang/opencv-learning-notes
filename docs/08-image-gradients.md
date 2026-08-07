# 08 图像梯度算子：Sobel、Scharr 与 Laplacian

[上一章：形态学特征](07-morphological-features.md) · [教材目录](README.md) · [返回仓库首页](../README.md)

## 学习目标与前置知识

- 理解梯度表示图像亮度变化的方向和强度。
- 掌握 Sobel、Scharr 的一阶导数及 Laplacian 的二阶导数。
- 理解为什么计算使用 `CV_64F`，显示前要转回 8 位图。

前置知识：灰度图、平滑滤波和基础数学中的导数概念。

## 核心理论

图像中亮度变化很快的位置通常是边缘。对灰度图 $I(x,y)$，一阶梯度由两个方向组成：

$$G_x = \frac{\partial I}{\partial x}, \qquad G_y = \frac{\partial I}{\partial y}$$

综合强度（幅值）为：

$$G = \sqrt{G_x^2 + G_y^2}$$

```text
亮 ---- 突变边缘 ---- 暗
      梯度值大

横向变化 -> Gx 强
纵向变化 -> Gy 强
```

| 算子 | 导数阶数 | 特点 |
| --- | --- | --- |
| Sobel | 一阶 | 同时考虑差分与局部平滑，常用边缘算子 |
| Scharr | 一阶 | 在 3×3 小核下对方向变化更敏感 |
| Laplacian | 二阶 | 对快速变化敏感，也更容易受噪声影响 |

一阶导数会产生正值和负值，不能直接用无符号 `uint8` 保存，否则负方向信息会丢失。因此示例先使用 `CV_64F` 计算，再通过 `convertScaleAbs` 取绝对值并转换为可显示的 8 位图像。

## 对应实践

对应脚本：[梯度算子示例](../gradient_operators.py)

```powershell
python gradient_operators.py
```

脚本先将 `images/test.jpg` 转灰度并做高斯滤波，再计算 Sobel X/Y 和幅值、Scharr X/Y 和幅值，以及 Laplacian。最终将结果转换为 8 位图显示并保存到 `output/`。

核心调用关系：

```python
sobel_x = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)
sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)
```

## 参数速查与常见误区

| 写法 | 作用 |
| --- | --- |
| `cv2.Sobel(src, ddepth, dx, dy, ksize=3)` | 计算指定方向的一阶 Sobel 导数 |
| `cv2.Scharr(src, ddepth, dx, dy)` | 计算 Scharr 一阶导数 |
| `cv2.Laplacian(src, ddepth, ksize=3)` | 计算二阶 Laplacian 导数 |
| `cv2.CV_64F` | 用 64 位浮点保存正负导数值 |
| `cv2.magnitude(x, y)` | 计算 $\sqrt{x^2+y^2}$ |
| `cv2.convertScaleAbs(src)` | 取绝对值、缩放并转为 `uint8` 显示 |

常见误区：

- 把 `dx=1, dy=0` 误解为“只找水平线”；它表示对 x 方向求导，通常对垂直边缘响应更明显。
- 直接以 `uint8` 计算导数，导致负值信息丢失。
- 未先平滑就使用 Laplacian，噪声也会被强烈响应为边缘。

## 复习卡

关键结论：梯度衡量亮度变化；Sobel/Scharr 是一阶导数，Laplacian 是二阶导数；导数计算需保留正负值。

<details>
<summary>自测 1：<code>cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)</code> 中的 <code>1, 0</code> 表示什么？</summary>

表示对 x 方向求一阶导数、对 y 方向不求导，即计算 `Gx`。
</details>

<details>
<summary>自测 2：为什么不能直接把 Sobel 的导数结果当普通 <code>uint8</code> 图显示？</summary>

导数包含负值，而 `uint8` 只能表示 0 到 255；需要先保留符号，再转换为适合显示的绝对值图。
</details>

<details>
<summary>自测 3：为什么示例在计算梯度前先做高斯滤波？</summary>

梯度会放大快速变化，噪声也是快速变化；先平滑可以减少噪声被误检为边缘。
</details>

[上一章：形态学特征](07-morphological-features.md) · [教材目录](README.md) · [返回仓库首页](../README.md)
