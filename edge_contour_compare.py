import cv2
from pathlib import Path

# 读取原始图像
image = cv2.imread("images/basics/test.jpg")

if image is None:
    print("Image read failed")
    raise SystemExit

# 转为灰度图并平滑，作为两种方法的共同输入
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Canny 输出每个亮度突变位置的边缘图
edges = cv2.Canny(blur, 50, 150)

# 使用反向 Otsu 阈值，使较暗的主体成为白色前景
_, binary = cv2.threshold(
    blur,
    0,
    255,
    cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
)

# 从白色前景中提取最外层轮廓
contours, _ = cv2.findContours(
    binary.copy(),
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 在原图副本上绘制筛选后的轮廓、外接框和面积
contour_image = image.copy()
min_area = 1000
valid_count = 0

for contour in contours:
    area = cv2.contourArea(contour)

    # 忽略面积很小的文本、噪声和细碎区域
    if area < min_area:
        continue

    x, y, width, height = cv2.boundingRect(contour)

    # 绿色表示轮廓本身，红色表示轮廓的外接矩形
    cv2.drawContours(contour_image, [contour], -1, (0, 255, 0), 2)

    cv2.rectangle(
        contour_image,
        (x, y),
        (x + width, y + height),
        (0, 0, 255),
        2
    )

    cv2.putText(
        contour_image,
        f"Area: {int(area)}",
        (x, max(y - 10, 25)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 0, 0),
        2
    )

    valid_count += 1

# 保存中间结果，便于逐张比较
Path("output/contours").mkdir(parents=True, exist_ok=True)
cv2.imwrite("output/contours/canny_edges.jpg", edges)
cv2.imwrite("output/contours/binary.jpg", binary)
cv2.imwrite("output/contours/contours.jpg", contour_image)

print(f"All contours: {len(contours)}")
print(f"Contours with area >= {min_area}: {valid_count}")

# 同时显示边缘图、二值前景图和轮廓分析结果
cv2.imshow("Original", image)
cv2.imshow("Canny Edges", edges)
cv2.imshow("Binary For Contours", binary)
cv2.imshow("Contours", contour_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
