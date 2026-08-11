import cv2

# 读取待搜索的大图
source = cv2.imread("images/geometric_shapes.png")

if source is None:
    print("Source image read failed")
    raise SystemExit

# 裁剪蓝色矩形及其周围区域，作为模板
template = source[80:200, 270:400]

# 模板不能为空
if template.size == 0:
    print("Template crop failed")
    raise SystemExit

# 转灰度，减少颜色通道带来的干扰
source_gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# 生成匹配得分图
score_map = cv2.matchTemplate(
    source_gray,
    template_gray,
    cv2.TM_CCOEFF_NORMED
)

# 对该匹配方法，最大值位置就是最佳匹配位置
min_value, max_value, min_location, max_location = cv2.minMaxLoc(score_map)

top_left = max_location
template_height, template_width = template_gray.shape[:2]

bottom_right = (
    top_left[0] + template_width,
    top_left[1] + template_height
)

# 在原图副本上画出最佳匹配区域
result = source.copy()

cv2.rectangle(
    result,
    top_left,
    bottom_right,
    (0, 0, 255),
    2
)

print(f"Best score: {max_value:.4f}")
print(f"Best location: {top_left}")

cv2.imshow("Source", source)
cv2.imshow("Template", template)
cv2.imshow("Template Match Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()