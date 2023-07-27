import os
import concurrent.futures
from PIL import Image

# 数据集路径
data_root = 'D:/learn/nlos/dataset/img_align_celeba'
# 新文件夹路径
new_folder = 'D:/learn/nlos/dataset/celeb128'
os.makedirs(new_folder, exist_ok=True)

# 处理单个图像的函数
def process_image(filename):
    if filename.endswith('.jpg'):
        # 加载图像
        image_path = os.path.join(data_root, filename)
        image = Image.open(image_path)
        # 调整图像大小为 128x128 像素
        resized_image = image.resize((128, 128))
        # 保存调整大小后的图像到新文件夹
        new_image_path = os.path.join(new_folder, filename)
        resized_image.save(new_image_path)

# 使用多线程处理图像
with concurrent.futures.ThreadPoolExecutor() as executor:
    # 遍历数据集文件夹中的图像文件
    image_files = [filename for filename in os.listdir(data_root) if filename.endswith('.jpg')]
    executor.map(process_image, image_files)

print("预处理完成！")
