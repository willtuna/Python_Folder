import cv2
import sys 
import numpy as np
import os

#default parameters
bin_n = 16  # number of bins

    # Image Reading
    imSrc = cv2.imread(argv[1])
    imSrc = np.float32(imSrc) / 255.0
    
def hog(img):    
    # Calculate Gradient
    gx = cv2.Sobel(img, cv2.CV_32F, 1 ,0, ksize = CV_SHARR(-1))
    gy = cv2.Sobel(img, cv2.CV_32F, 0, 1),ksize = CV_SHARR(-1)
    mag,angle = cv2.cartToPolar(gx,gy, angleInDegrees=True)
    bins = np.int32(bin_n*angle/2*np.pi) # convert ange to corresponding bins
    bin_cells = bins[:10,:10]


