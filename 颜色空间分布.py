from PIL import Image
import matplotlib.pyplot as plt

def plot_color_histogram(image_path):
    # 打开图片
    image = Image.open(image_path)

    # 获取图片像素数据
    pixels = image.getdata()

    # 分离RGB通道
    red = [pixel[0] for pixel in pixels]
    green = [pixel[1] for pixel in pixels]
    blue = [pixel[2] for pixel in pixels]

    # 绘制颜色直方图
    plt.figure(figsize=(10, 6))

    plt.subplot(3, 1, 1)
    plt.hist(red, bins=256, range=(0, 255), color='red', alpha=0.5)
    plt.title('Red Channel')

    plt.subplot(3, 1, 2)
    plt.hist(green, bins=256, range=(0, 255), color='green', alpha=0.5)
    plt.title('Green Channel')

    plt.subplot(3, 1, 3)
    plt.hist(blue, bins=256, range=(0, 255), color='blue', alpha=0.5)
    plt.title('Blue Channel')

    plt.tight_layout()
    plt.show()

# 示例图片路径（请替换为您自己的图片路径）
image_path = 'img/vis.png'

plot_color_histogram(image_path)
