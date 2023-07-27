import cv2
import os

def split_video_to_images(video_path, output_folder, frame_interval):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("无法打开视频文件.")
        return

    output_folder = os.path.join(output_folder, video_path.split("\\")[-1][0:-4])
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("输出文件夹:", output_folder)

    frame_count = 0
    index = 0
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # 每隔 frame_interval 帧保存一张图片
        if frame_count % frame_interval == 0:
            output_file = os.path.join(output_folder, f"frame_{index:04d}.bmp")
            cv2.imwrite(output_file, frame)
            index += 1
        frame_count += 1

    cap.release()
    print(f"\t视频已拆分为 {index} 张图片.")


def get_video_frame_count_and_fps(video_path):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 确保视频文件被成功打开
    if not cap.isOpened():
        print("无法打开视频文件.")
        return

    # 获取视频帧数
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # 获取视频帧率（FPS）
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 释放视频对象
    cap.release()

    return frame_count, fps


def calculate_frames_per_second(frame_count, fps):
    frames_per_second = frame_count / fps
    return frames_per_second





def getInfo(video_path_list):
    for video_path in video_path_list:
        frame_count, fps = get_video_frame_count_and_fps(video_path)
        frames_per_second = calculate_frames_per_second(frame_count, fps)
        print(f"{video_path}:\n\t视频帧数: {frame_count}")
        print(f"\t视频帧率 (FPS): {fps}")
        print(f"\t每秒拆分图片数: {frames_per_second:.2f}")

def video2img(video_path_list, output_folder,frame_interval_list):
    for i, video_path in enumerate(video_path_list):
        split_video_to_images(video_path, output_folder, frame_interval_list[i])


if __name__ == '__main__':
    # 使用示例 路径严格按照 r":\" 格式书写
    video_path_list = [r"F:\7-18视频\red\VIS\vis.mp4",
                       r"F:\7-18视频\red\IR\ir.mp4"
                       ]

    getInfo(video_path_list)

    name = input("输出文件夹名称：")
    output_folder = os.path.join("",name)

    frame_interval_list = []

    for i in range(len(video_path_list)):
        frame_interval_list.append(eval(input("每个视频的间隔抽帧")))

    video2img(video_path_list, output_folder, frame_interval_list)

