import os

blur_folder = r"G:\ZWH\Dataset\OT\Carton\train\blur"
sharp_folder = r"G:\ZWH\Dataset\OT\Carton\train\sharp"

# 获取blur文件夹和sharp文件夹中的文件名列表
blur_files = os.listdir(blur_folder)
sharp_files = os.listdir(sharp_folder)
cnt = 0
# 检查文件名是否一一对应
if len(blur_files) != len(sharp_files):
    print("文件数量不匹配")

else:
    for blur_file, sharp_file in zip(blur_files, sharp_files):
        if blur_file != sharp_file:
            print("文件名不匹配: {} 和 {}".format(blur_file, sharp_file))
        else:
           cnt+=1

print(f'共有{cnt}')