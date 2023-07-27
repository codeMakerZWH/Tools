import cv2


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


# 使用示例

#video_path list
# video_path_list = [r"F:\7-17视频demo\GT.mp4",
#               r"F:\7-17视频demo\IR_2023-07-17-19-44-45.mp4",
#               r"F:\7-17视频demo\VISIBLE_2023-07-17-19-44-45.mp4"
#             ]
video_path_list = [r"F:\7-18视频\red\VIS\vis.mp4",
              r"F:\7-18视频\red\IR\ir.mp4"
            ]
#get info of video
for video_path in video_path_list:
    frame_count, fps = get_video_frame_count_and_fps(video_path)
    frames_per_second = calculate_frames_per_second(frame_count, fps)
    print(f"{video_path}:\n\t视频帧数: {frame_count}")
    print(f"\t视频帧率 (FPS): {fps}")
    print(f"\t每秒拆分图片数: {frames_per_second:.2f}")
