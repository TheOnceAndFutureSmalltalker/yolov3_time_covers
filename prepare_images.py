# -*- coding: utf-8 -*-
"""
This script creates training images by placing time cover magazines into
background images acquired from http://cvcl.mit.edu/database.htm and from
video frames from project_video.mp4.

Created on Fri Dec 28 20:15:54 2018

@author: Tim
"""
#! /usr/bin/python
import cv2;
import glob
import random
from moviepy.editor import VideoFileClip
from ytc_utils import *

def createInternetTrainingImages():
    print("Creating training images from internet images.")
    time_cover_images = readTimeCovers()
    image_files = [file_name for file_name in glob.glob("images/*.jpg")]
    for image_number, image_file in enumerate(image_files):
        image = cv2.imread(image_file)
        if image is None or image.size == 0:
            print('zero sized file')
            continue
        if image_number % 20 != 0:
            time_cover_image = randomlySelectCover(time_cover_images)
            if image_number % 2 == 0:
                # resize to 512 X 288,  0.1 to 0.3
                image = cv2.resize(image,(512,288))
                time_cover_image = randomlyScaleImage(time_cover_image, 0.08, 0.3)
            else:
                # keep as 256X256, 0.05 to 0.2
                time_cover_image = randomlyScaleImage(time_cover_image, 0.05, 0.2)
            #time_cover_image = randomlyRotateImage(time_cover_image)
            row, col, prepared_image = randomlyPlaceCover(time_cover_image, image) 
        else:
            prepared_image = image     
        #prepared_file = image_file.replace('internet_images', 'images')
        cv2.imwrite(image_file, prepared_image) 
        
        # add line to train.txt/val.txt for locating image file
        line = "yolov3_time_covers/" + image_file.replace("\\", "/") + "\n"
        if image_number % 5 == 0:
            # line goes to val.txt
            with open("val.txt", "a") as val_file:
                val_file.write(line)
        else:
            # line goes to train.txt
            with open("train.txt", "a") as train_file:
                train_file.write(line)

        # create labels file for image
        if image_number % 20 != 0:
            dw = 1.0 / image.shape[1]
            dh = 1.0 / image.shape[0]
            w = time_cover_image.shape[1] * dw
            h = time_cover_image.shape[0] * dh
            x = (col + time_cover_image.shape[1] / 2) * dw
            y = (row + time_cover_image.shape[0] / 2) * dh
            prepared_text_file_info = '0 {0} {1} {2} {3}\n'.format(x, y, w, h)
        else:
            prepared_text_file_info = ''
        prepared_text_file = image_file.replace('.jpg', '.txt')
        prepared_text_file = prepared_text_file.replace('images', 'labels')
        writeTextFile(prepared_text_file, prepared_text_file_info)
        
def createVideoFrameTrainingImages():
    print("Creating training images from video frames.")
    row = 0
    col = 0
    time_cover_images = readTimeCovers()
    in_clip = VideoFileClip("project_video.mp4")
    image_number = 0

    for image in in_clip.subclip(0,30).iter_frames():
        if image is None or image.size == 0:
            print('zero sized file')
            continue
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if image_number % 20 != 0:
            time_cover_image = randomlySelectCover(time_cover_images)
            time_cover_image = randomlyScaleImage(time_cover_image, 0.25, 0.45)
            row = random.randint(250, 720 - 5 - time_cover_image.shape[0]) 
            col = random.randint(5, 1280 - 5 - time_cover_image.shape[1]) 
            prepared_image = placeCover(time_cover_image, image, row, col) 
        else:
            prepared_image = image     
        prepared_file = 'images/vid_frame_{:04d}.jpg'.format(image_number)
        cv2.imwrite(prepared_file, prepared_image) 
        
        # add line to train.txt/val.txt for locating image file
        line = "yolov3_time_covers/" + prepared_file + "\n"
        if image_number % 5 == 0:
            # line goes to val.txt
            with open("val.txt", "a") as val_file:
                val_file.write(line)
        else:
            # line goes to train.txt
            with open("train.txt", "a") as train_file:
                train_file.write(line)
                
        # create labels file for image
        if image_number % 20 != 0:
            dw = 1.0 / image.shape[1]
            dh = 1.0 / image.shape[0]
            w = time_cover_image.shape[1] * dw
            h = time_cover_image.shape[0] * dh
            x = (col + time_cover_image.shape[1] / 2) * dw
            y = (row + time_cover_image.shape[0] / 2) * dh
            prepared_text_file_info = '0 {0} {1} {2} {3}\n'.format(x, y, w, h)
        else:
            prepared_text_file_info = ''
            
        prepared_text_file = prepared_file.replace('.jpg', '.txt')
        prepared_text_file = prepared_text_file.replace('images', 'labels')
        writeTextFile(prepared_text_file, prepared_text_file_info)
        
        image_number += 1

        
createInternetTrainingImages()
createVideoFrameTrainingImages()
        
