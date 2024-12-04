from PIL import Image

# 打开图像
image = Image.open("output_image_white.png").convert("RGBA")

# 获取图像数据
data = image.getdata()

# 定义新颜色
black = (0, 0, 0, 255)
yellow = (255, 255, 255, 255)

# 替换黑色为黄色
new_data = []
for item in data:
    if item[:3] == black[:3] and item[3] == 255:  # 只替换完全不透明的黑色
        new_data.append(yellow)  # 替换为黄色
    else:
        new_data.append(item)  # 保持原样

# 更新图像数据
image.putdata(new_data)

# 保存新的图像
image.save("output_image_white.png")

print("图片已处理完成并保存为 output_image_white.png")

