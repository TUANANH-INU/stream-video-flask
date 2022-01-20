import cv2
from base_camera import BaseCamera
import numpy as np
import time

class Camera(BaseCamera):
    video_source1 = './video/a.mp4'
    video_source2 = './video/b.mp4'
    video_source3 = './video/c.mp4'
    video_source4 = './video/d.mp4'

    @staticmethod
    def set_video_source(sources):
        Camera.video_source1 = sources[0]
        Camera.video_source2 = sources[1]
        Camera.video_source1 = sources[2]
        Camera.video_source2 = sources[3]

    @staticmethod
    def frames():
        camera1 = cv2.VideoCapture(Camera.video_source1)
        camera2 = cv2.VideoCapture(Camera.video_source2)
        camera3 = cv2.VideoCapture(Camera.video_source3)
        camera4 = cv2.VideoCapture(Camera.video_source4)
        
        prev_frame_time = 0
        new_frame_time = 0
        if not (camera1.isOpened() or camera2.isOpened() or camera3.isOpened() or camera4.isOpened()):
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img1 = camera1.read()
            _, img2 = camera2.read()
            _, img3 = camera3.read()
            _, img4 = camera4.read()
            
            img1 = cv2.resize(img1, (360, 240))
            img2 = cv2.resize(img2, (360, 240))
            img3 = cv2.resize(img3, (360, 240))
            img4 = cv2.resize(img4, (360, 240))
            
            new_frame_time = time.time()
            fps = 1/(new_frame_time-prev_frame_time)
            prev_frame_time = new_frame_time
            fps = str(int(fps)) 

            cv2.putText(img1, fps, (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 3, cv2.LINE_AA)

            img_1 = np.hstack((img1, img2))
            img_2 = np.hstack((img3, img4))
            img = np.vstack((img_1, img_2))

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
