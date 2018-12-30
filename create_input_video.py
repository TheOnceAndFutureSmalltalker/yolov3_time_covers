# -*- coding: utf-8 -*-
"""
This script builds input_video.mp4 based on project_video.mp4 by placing
Time magazine covers in the video as if they are moving along the road
with traffic.

Created on Sat Dec 29 13:25:01 2018

@author: Tim
"""


from moviepy.editor import VideoFileClip
from ytc_utils import *

# puts 2 different time covers into video such that they are following 
# along the same paths as the cars in the video
class FrameModifier:
    def __init__(self, time_cover_file='time_covers/optimists-final-cover.jpg', scale=0.2):
        self.frame_number = 0;
        self.scale = scale
        self.time_cover_image_1 = mpimg.imread(time_cover_file)
        self.time_cover_image_1 = scaleImage(self.time_cover_image_1, 0.3)
        self.time_cover_image_2 = mpimg.imread('time_covers/g9510-20_ford-cover.jpg')
        self.time_cover_image_2 = scaleImage(self.time_cover_image_2, 0.4)
        
    def addTimeCover(self, frame):
        new_frame = frame.copy()
        
        if self.frame_number > 100:
            col = 10 + int(self.frame_number) - 100
            row = new_frame.shape[0] - self.time_cover_image_1.shape[0] - 10 - int(self.frame_number * 0.5) + 50 
            new_frame = placeCover(self.time_cover_image_1, new_frame, row, col)
            
        if self.frame_number > 300:
            col = new_frame.shape[1]- self.time_cover_image_2.shape[1] - 10 - int(self.frame_number) + 300
            row = new_frame.shape[0] - self.time_cover_image_2.shape[0] - 80 - int(self.frame_number * 0.2)
            new_frame = placeCover(self.time_cover_image_2, new_frame, row, col)
        
        self.frame_number += 1
        return new_frame;
    
    # add time covers to each frame of video
# and re-assemble into new video
# source: project_video.mp4 from Udacity
def addTimeCoversToVideo():
    print("Adding time covers to project_video.mp4 and saving as input_video.mp4")
    fm = FrameModifier(scale=0.4)
    in_clip = VideoFileClip("project_video.mp4")
    print(in_clip.filename)
    print (in_clip.fps)
    #print ( [frame[0,:,0].max() for frame in in_clip.subclip(0,1).iter_frames()])
    #in_clip.save_frame('test.jpg', t=0, withmask=True)
    out_clip = in_clip.fl_image(fm.addTimeCover).subclip(0,30)
    out_clip.write_videofile('input_video.mp4', audio=False)
    in_clip.reader.close()
    
    
    
addTimeCoversToVideo()
