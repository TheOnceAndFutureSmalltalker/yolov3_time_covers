YOLO v3 Time Magazine Covers Detection and Video
=========

This is a demonstration of how to create and train a darknet YOLO v3 model to detect time cover magazines embeded within background images and create a video where time magazine covers are tracked as they move through the video.  Complete instructions are given below.

File | Description
------------ | -------------
examples | Folder containing sample images
README.md | This readme file
create_input_video.py | Creates a copy of project_video.mp4 with Time magazine covers traveling through it
create_output_video.py | Creates outpu_video.mp4 from frames which have Time magazine covers detected and marked by model.
get_images.sh | script which downloads images from http://cvcl.mit.edu/database.htm that are used for training.
get_video_frames.py | Capatures frames from input_video.mp4 and copies them to a folder for darknet model detection.
prepare_images.py | Prepares training images by placing Time magazine covers in them.  Creates label files too.
project_video.mp4 | Video taken from camera mounted on self driving car as it drives down highway.  From Udacity.
time.cfg | Darknet config file for training model.  Defines model architecture, training parameters, etc,
time.data | Darknet file that points to other required files for training.
time.names | List of classes of detectable objects.  In our case, only one class - timecover.
time.weights | Final weights after training.
ytc_utils.py | Utilities supporting other scripts.




## Instructions
The instructions are divided into 4 parts:

1. Installing Darknet (YOLO software)
2. Acquiring & Preparing Training Images
3. Training the Model
4. Creating Example Video

**Prerequisites:**  You must have a unix/linux system with at least one GPU (otherwise training will take days!), Python 3.5 or higher with OpenCV, NumPy, and MoviePy.

### Installing Darknet 

Information on Darknet and YOLO can be found at https://pjreddie.com/darknet/.

This demonstration uses the fork of darknet found at https://github.com/AlexeyAB/darknet because it includes some useful enhancements.  It saves the model every 100 iterations, it performs detection on an entire filder of images, and it calculates mAP.

Get the darknet project by executing the following:

    >git clone https://github.com/AlexeyAB/darknet.git

Then switch to darknet directory.

    >cd darknet
    
Then edit Makefile and set `CDU=1` (around line ??) so that darknet compiles with CUDA and uses the GPU (otherwise training will take days!!!) and save your changes.

Now compile darknet using the following command:

    >make
    
To make sure everything compiled correctly, execute the following:

    >./darknet
    
for any problems or for more on compiling darknet, see https://pjreddie.com/darknet/install/.

### Acquiring & Preparing Training Images


### Training the Model


### Creating Example Video


