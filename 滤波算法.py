import cv2
import numpy as np


import cv2
import numpy as np

##双边滤波算法
def bilateralFilter(img, d, sigmaColor, sigmaSpace):
    return cv2.bilateralFilter(img, d, sigmaColor, sigmaSpace)
#
def laplacian_filter(image):
    # 应用Laplacian滤波器
    filtered_image = cv2.Laplacian(image, cv2.CV_64F)
    filtered_image = np.uint8(np.absolute(filtered_image))
    return filtered_image

def sobel_filter(image, dx, dy, ksize):
    # 应用Sobel滤波器
    filtered_image = cv2.Sobel(image, cv2.CV_64F, dx, dy, ksize)
    filtered_image = cv2.convertScaleAbs(filtered_image)
    return filtered_image

def scharr_filter(image, dx, dy):
    # 应用Scharr滤波器
    filtered_image = cv2.Scharr(image, cv2.CV_64F, dx, dy)
    filtered_image = cv2.convertScaleAbs(filtered_image)
    return filtered_image

def gaussian_filter(image, kernel_size, sigma):
    # 应用高斯滤波器
    filtered_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)
    return filtered_image

def median_filter(image, kernel_size):
    # 应用中值滤波器
    filtered_image = cv2.medianBlur(image, kernel_size)
    return filtered_image

import numpy as np

def grabcut_segmentation(image):
    # 创建一个与图像大小相同的掩膜
    mask = np.zeros(image.shape[:2], np.uint8)

    # 定义背景和前景模型
    background_model = np.zeros((1, 65), np.float64)
    foreground_model = np.zeros((1, 65), np.float64)

    # 定义感兴趣区域（ROI）
    rectangle = (50, 50, image.shape[1]-50, image.shape[0]-50)

    # 执行GrabCut算法
    cv2.grabCut(image, mask, rectangle, background_model, foreground_model, 5, cv2.GC_INIT_WITH_RECT)

    # 创建一个掩膜，将确定的前景和可能的前景设置为1，其他区域设置为0
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

    # 将原始图像与掩膜相乘以突出人体轮廓
    segmented_image = image * mask2[:, :, np.newaxis]
    return segmented_image


def adaptive_histogram_equalization(image, clip_limit, tile_size):
    # 将图像转换为8位灰度图像
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 将图像转换为8位无符号整数
    image = cv2.convertScaleAbs(image)

    # 应用自适应直方图均衡化
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_size, tile_size))
    equalized_image = clahe.apply(image)
    return equalized_image


def createWindow(window_title, img):
    # 设置窗口标题
    window_title = window_title

    # 创建并设置窗口
    cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)  # 使用cv2.WINDOW_NORMAL以允许调整窗口大小

    # 设置窗口大小
    cv2.resizeWindow(window_title, 800, 600)  # 替换为你想要的窗口大小

    # 显示原始模糊图像
    cv2.imshow(window_title, img)

def main():
    # 加载模糊图片
    image_path = './img/ir.bmp'  # 替换为实际的图片路径
    img = cv2.imread(image_path)

    if img is None:
        print("img not found")
        return

    ##双边滤波算法
    # filterdImg = bilateralFilter(img, 9, 75, 75)#双边滤波算法
    # filterdImg = laplacian_filter(img)#拉普拉斯滤波算法
    # filterdImg = sobel_filter(img, 1, 1, 3)#sobel滤波算法
    # filterdImg = scharr_filter(img, 1, 0) #scharr滤波算法
    # filterdImg = adaptive_histogram_equalization(img, 2.0, 8) #自适应直方图均衡化
    # filterdImg = gaussian_filter(img, 5, 1.5) #高斯滤波
    # filterdImg = median_filter(img, 5) #中值滤波
    filterdImg = grabcut_segmentation(img) #grabcut分割算法



    createWindow('original image', img)
    createWindow('filterd image', filterdImg)

if __name__ == "__main__":
    main()
    # 等待按键按下，然后关闭所有打开的窗口
    cv2.waitKey(0)
    cv2.destroyAllWindows()
