import os
import shutil
from threading import Thread

def copy_images(source_dir, dest_dir, images):
    for image in images:
        image_path = os.path.join(source_dir, image)
        dest_path = os.path.join(dest_dir, image)
        shutil.copy(image_path, dest_path)

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    # source_dir = r'G:\YXD\STL10\GT_stl10_allimages\GT_stl10_allimages'
    source_dir = r'G:\YXD\carton\anime_GT\animaface'
    train_dir = r'G:\ZWH\Dataset\OT\Carton\train\sharp'
    test_dir = r'G:\ZWH\Dataset\OT\Carton\test\sharp'
    valid_dir = r'G:\ZWH\Dataset\OT\Carton\valid\sharp'
    train = 100000
    test = 5000
    valid = 1000

    create_directory(train_dir)
    create_directory(test_dir)
    create_directory(valid_dir)

    # 获取所有图片文件名
    image_files = os.listdir(source_dir)
    image_count = len(image_files)

    # 选取前100000个图片拷贝到训练目录
    train_images = image_files[:train]
    train_thread = Thread(target=copy_images, args=(source_dir, train_dir, train_images))
    train_thread.start()

    # 选取接下来的10000个图片拷贝到测试目录
    test_images = image_files[train:train+test]
    test_thread = Thread(target=copy_images, args=(source_dir, test_dir, test_images))
    test_thread.start()

    valid_images = image_files[train+test:train+test+valid]
    copy_images(source_dir, valid_dir, valid_images)

    # 等待训练线程完成
    train_thread.join()
    test_thread.join()
    print('拷贝完成！')

if __name__ == '__main__':
    main()
