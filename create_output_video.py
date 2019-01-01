# -*- coding: utf-8 -*-
"""
Script for creating output_video.mp4 from images contained in frames_out folder.

Created on Sat Dec 29 14:26:11 2018

@author: Tim
"""
#!/usr/bin/python
import os
from moviepy.editor import ImageSequenceClip
from ytc_utils import *

file_names = ("frames_out/" + fn for fn in os.listdir('frames_out') if fn.endswith('.png'))
file_names = sorted(file_names)
for f in file_names:
    print(f)
clip = ImageSequenceClip(file_names, fps=25)
clip.write_videofile("output_video.mp4") 

