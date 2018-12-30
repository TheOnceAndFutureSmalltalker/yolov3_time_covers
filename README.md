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

This demonstration uses the fork of darknet found at https://github.com/AlexeyAB/darknet because it includes some useful enhancements:
1. Saves the model every 100 iterations
2. Performs detection on an entire folder of images
3. Calculates mAP

Get the darknet project by executing the following:

    >git clone https://github.com/AlexeyAB/darknet.git

Then switch to darknet directory.

    >cd darknet
    
Then edit Makefile and set `CDU=1` (around line ??) so that darknet compiles with CUDA and uses the GPU (otherwise training will take days!!!) and save your changes.

Now compile darknet using the following command:

    >make
    
To make sure everything compiled correctly, execute the following:

    >./darknet
    
you should get the following output.

    >usage: ./darknet <function>
    
For any problems or for more on compiling darknet, see https://pjreddie.com/darknet/install/.



### Acquiring & Preparing Training Images

Now get this project by executing the command:

    >git clone https://github.com/TheOnceAndFutureSmalltalker/yolov3_time_covers.git

Now switch to the yolov3_time_covers folder.  

    >cd yolov3_time_covers

Image prep and video operations will be handled in this directory.  Training and other darknet commands will be executed from the darknet directory.

Training images are acquired from http://cvcl.mit.edu/database.htm.  From the yolov3_time_covers directory, run the following shell script to download all of the images and copy them to the images directory.

    >./get_images.sh
    
You should now have an images directory with 1500 or so images.  

Now run the following Python script to insert Time magazine covers into these training images.  In addition, frames from the example video, project_video.mp4, are extracted and used as training images as well.

    >python prepare_images.py 

If you inspect some of these images, you will see that most have a Time magazine cover inserted in them somewhere (a few do not).  An example is shown below.


Also notice that there is a labels directory.  For each training image in images directory, there is a corresponding .txt file that indicates the size and location of the Time cover in the image.  Each of these files is just one line long since there is only one Time cover in each image.  An example of one of these files is shown below.

    0 0.0615234375 0.2638888888888889 0.060546875 0.14583333333333331

Finally, two files, train.txt and val.txt were created.  These files reference the various images that are used for training or validation respectively.

You are now ready to train the model.

### Training the Model


### Creating Example Video


