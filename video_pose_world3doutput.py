import cv2
import mediapipe as mp
import time
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
        min_detection_confidence=0.5,
         min_tracking_confidence=0.5,
        model_complexity=1
        ) 
import numpy as np

import os
import cv2
import math
import vg


def video_pose2npy(video_path):
    total_list = []

    cap = cv2.VideoCapture(video_path)
    while True:
        ret,frame = cap.read()
        if not ret:
            break
        landmarks_worlld = []
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        height, width, _ = image.shape
        
        results = pose.process(image)
        # self.mp_drawing.draw_landmarks(
        #     image,
        #     results.pose_landmarks,
        #     mp_pose.POSE_CONNECTIONS,
        #     landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        if results.pose_landmarks is not None:
           
                    
                    # Append the landmark into the list.
            total_list.append(results.pose_world_landmarks)
            
        # print(landmarks)
        
        print(len(total_list))
    return total_list
        # label = self.classifyPose(landmarks)
        # fig ,ax= plot_landmarksplot_landmarks(results.pose_world_landmarks, mp_pose.POSE_CONNECTIONS)
        # return image,label,landmarks,fig,ax
        # return image,label,landmarks




if __name__ == "__main__":
    video_path='./video/video4.mp4'
    total_list = video_pose2npy(video_path)
    nptotal = np.array(total_list)
    np.save('video4_world', nptotal)
    # a=np.load('video1_world.npy',allow_pickle=True)
    # print(len(a))
    # print(a[0])