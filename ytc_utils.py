# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:38:07 2018

@author: Tim
"""

import cv2;
import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.image as mpimg
import glob
import random
import os
#from moviepy.editor import VideoFileClip

def placeCover(cover_image, background_image, row=0, col=0):
    # copy background image
    background_image = background_image.copy()

    # create ROI of background image where rotated cover is going
    rows,cols,channels = cover_image.shape
    roi = background_image[row:row+rows, col:col+cols ]

    # create a mask of cover image and create its inverse mask also
    # mask is required since cover has been rotated within a larger image of black pixels
    cover_image_gray = cv2.cvtColor(cover_image,cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(cover_image_gray, 0, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # black-out the area of rotated cover in ROI
    background_image_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

    # Take only region of rotated cover from image.
    cover_image_fg = cv2.bitwise_and(cover_image,cover_image,mask = mask)

    # Put logo in ROI and modify the main image
    dst = cv2.add(background_image_bg, cover_image_fg)
    background_image[row:row+rows, col:col+cols ] = dst
    
    return background_image    

# randomly place the cover image on the background image
def randomlyPlaceCover(cover_image, background_image):
    # randomly determine where cover will be placed
    row = random.randint(0, background_image.shape[0]-cover_image.shape[0])
    col = random.randint(0, background_image.shape[1]-cover_image.shape[1])
    
    result_image = placeCover(cover_image, background_image, row, col)
    
    return (row, col, result_image)

def readTimeCovers():
    time_cover_files = [file_name for file_name in glob.glob("time_covers/*.jpg")]
    time_cover_images = []
    for file_name in time_cover_files:
        next_img = cv2.imread(file_name)
        time_cover_images.append(next_img)
    return time_cover_images

def scaleImage(img, scale=1.0):
    newX = int(img.shape[1] * scale)
    newY = int(img.shape[0] * scale)
    scaled_image = cv2.resize(img, (newX, newY))
    return scaled_image    

# randomly scale image
def randomlyScaleImage(img, smallest_scale=0.1, largest_scale=1.0):
    scale = random.uniform(smallest_scale, largest_scale)
    scaled_image = scaleImage(img, scale)
    return scaled_image

# randomly select next Time cover image
def randomlySelectCover(time_cover_images):
    index = random.randint(0,len(time_cover_images)-1)
    return time_cover_images[index]

# delete contents of folder
def deleteFiles(folder):
    files = glob.glob(folder)
    for f in files:
        os.remove(f)
        
def writeTextFile(fname, text):
    file = open(fname, 'w')
    file.write(text)
    file.close()   