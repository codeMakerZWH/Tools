import os
from matplotlib import pyplot as plt
import cv2
from PIL import Image
import numpy as np

def testRotate(im, num):
    # 指定逆时针旋转的角度
    im_rotate = im.transpose(Image.ROTATE_90)
    # im_rotate = im.rotate(num)
    return im_rotate

def testScal(im, size):
    # 原图像缩放为128x128
    im_resized = im.resize(size)
    return im_resized

def testCrop(im, list1):
    region = im.crop(list1)
    #  ## 0,0表示要裁剪的位置的左上角坐标，50,50表示右下角。
    # region.show()
    return region

def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + ' 创建成功')

        return True
    else:
        print(path + ' 目录已存在')
        return False


list1 = [166,0,307,329]
list2 = [326,0,468,328]
list3 = [189,342,518,486]
size = [307 - 166,329]
file_path = r'F:\7-17视频demo'
files = os.listdir(file_path)
for file in files:
    if file == 'VIS.mp4':
        # 将文件名和后缀分成两部分
        dir_path1 = file_path+'\\' +'VIS'
        realPath = file_path + '\\' + file
        mkdir(dir_path1)


        cap = cv2.VideoCapture(realPath)  # 获取视频对象
        isOpened = cap.isOpened  # 判断是否打开
        # 视频信息获取
        fps = cap.get(cv2.CAP_PROP_FPS)
        print(fps)
        imageNum = 0
        sum = 9999999
        timef = 1  # 隔1帧保存一张图片
        frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print(1)
        while (isOpened):

            sum += 1

            (frameState, frame) = cap.read()  # 记录每帧及获取状态

            if frameState == True:

                frame = Image.fromarray(np.uint8(frame))
                # plt.subplot(1, 2, 1), plt.title("frame")
                # plt.imshow(frame), plt.axis('off')
                # plt.show()
                frame.save(dir_path1 + '\\' + str(imageNum) + '.bmp', 'bmp')

                #
                # print(dir_path1 + str(imageNum)+ " successfully write in")  # 输出存储状态
                # print(dir_path2 + str(imageNum)+ " successfully write in")  # 输出存储状态
                imageNum = imageNum + 1
            elif frameState == False:
                break

        print('finish!')
        cap.release()
