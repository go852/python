from PIL import Image, ImageDraw, ImageFont

# 创建画布
img = Image.new('RGB', (800, 600), (173, 216, 230))
draw = ImageDraw.Draw(img)

# 添加文字
font = ImageFont.truetype("SimSun.ttf", 40)
draw.text((300, 50), "数理编程", fill=(0, 0, 139), font=font)

# 添加公式
draw.text((50, 200), "a² + b² = c²", fill=(51, 51, 51), font=font)

# 添加代码
code = "#include <iostream>\nint main() {\n    std::cout << \"Hello, world!\" << std::endl;\n    return 0;\n}"
draw.text((400, 200), code, fill=(0, 0, 0), font=ImageFont.truetype("Consolas.ttf", 20))

# 保存图片
img.save("math_programming.png")