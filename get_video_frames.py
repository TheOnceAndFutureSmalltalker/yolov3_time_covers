# -*- coding: utf-8 -*-
"""
save all frames from input_video.mp4 created with create_input_video.py
these frames will be labeled using yolo and then re-assembled into a final video

Created on Sat Dec 29 13:39:10 2018

@author: Tim
"""

import cv2;
import os
from moviepy.editor import VideoFileClip
from ytc_utils import *


def saveTimeCoverFrames():
    if os.path.isdir(os.path.join(os.getcwd(), 'frames_in')):
        print("delete frames_in folder contents")
        deleteFiles('frames_in/*')
    else:
        print("create frames_in and frames_out folders")
        os.mkdir("frames_in")
        os.mkdir("frames_out")
        
    print("Creating frames from input_video.mp4")
    in_clip = VideoFileClip("input_video.mp4")
    frame_number = 0
    for frame in in_clip.subclip(0,30).iter_frames():
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imwrite('frames_in/vid_frame_{:04d}.jpg'.format(frame_number), frame)
        frame_number += 1

    in_clip.reader.close()

    print("done")
    
saveTimeCoverFrames()