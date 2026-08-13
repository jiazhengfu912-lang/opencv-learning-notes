import cv2
import numpy as np

# 读取规则几何图形
image = cv2.imread("images/geometry/geometric_shapes.png")

if image is None:
    print("Image read failed")
    raise SystemExit

# 转灰度图
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 黑色背景接近 0，阈值后彩色图形成为白色前景
_, binary = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY)

# 提取最外层轮廓
contours, _ = cv2.findContours(
    binary.copy(),
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 分别用于绘制不同结果
axis_box_image = image.copy()
rotated_box_image = image.copy()
approx_image = image.copy()

min_area = 200

for contour in contours:
    area = cv2.contourArea(contour)

    # 跳过太小的区域
    if area < min_area:
        continue

    # 计算轮廓周长
    perimeter = cv2.arcLength(contour, True)

    # 根据周长设置近似误差
    epsilon = 0.005 * perimeter

    # 得到近似后的关键顶点
    approx = cv2.approxPolyDP(contour, epsilon, True)

    # 绘制普通边界矩形
    x, y, width, height = cv2.boundingRect(contour)
    cv2.rectangle(
        axis_box_image,
        (x, y),
        (x + width, y + height),
        (0, 0, 255),
        2
    )

    # 计算并绘制最小旋转矩形
    rotated_rect = cv2.minAreaRect(contour)
    box_points = cv2.boxPoints(rotated_rect)
    box_points = np.intp(box_points)

    cv2.drawContours(
        rotated_box_image,
        [box_points],
        0,
        (0, 255, 0),
        2
    )

    # 绘制轮廓近似结果
    cv2.drawContours(
        approx_image,
        [approx],
        -1,
        (255, 255, 0),
        2
    )

    print(
        f"Area: {area:.1f}, "
        f"Original points: {len(contour)}, "
        f"Approx points: {len(approx)}"
    )

cv2.imshow("Binary", binary)
cv2.imshow("Axis Aligned Boxes", axis_box_image)
cv2.imshow("Rotated Boxes", rotated_box_image)
cv2.imshow("Approximated Contours", approx_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
