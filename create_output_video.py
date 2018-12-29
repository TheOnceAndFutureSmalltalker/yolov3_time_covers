# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:26:11 2018

@author: Tim
"""

import cv2;
import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.image as mpimg
import glob
import random
import os
from moviepy.editor import ImageSequenceClip
from ytc_utils import *

file_names = ("frames_out/" + fn for fn in os.listdir('frames_out') if fn.endswith('.jpg'))
file_names = sorted(file_names)
for f in file_names:
    print(f)
clip = ImageSequenceClip(file_names, fps=25)
clip.write_videofile("output_video.mp4") 

