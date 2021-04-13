#!/usr/bin/python
"""
Script for loading an image with text, drawing a rectangular ROI around the middle of the image, crop the image to contain only the ROI, perform Canny edge detection and draw green contours around each letter. Each step (expect Canny) will output an .jpg-file.

"""

# Load libraries
import os
import sys
sys.path.append(os.path.join("..", ".."))
import cv2
import numpy as np

# Defining function for writing images
def save_image(image, image_name):
    outpath = os.path.join("out", f"{image_name}.jpg")
    cv2.imwrite(outpath, image)

    
# Defining main function which performs all tasks
def main():
    # Reading image
    image = cv2.imread(os.path.join("..","..","data","assignment3", "_We_Hold_These_Truths__at_Jefferson_Memorial_IMG_4729.jpeg"))
     
    # 1) Drawing a green rectangle around ROI 
    x1, x2, y1, y2 = 1400, 2860, 870, 2800 #defining coordinates for start and end point of rectangle
    image_with_ROI = cv2.rectangle(image.copy(), (x1, y1), (x2, y2), (0,255,0), 3) #drawing rectangle
    save_image(image_with_ROI, "image_with_ROI") #saving roi image
    

    # 2) Cropping image to contain only the ROI
    image_cropped = image[y1:y2, x1:x2] #slicing based on the coordinates from the ROI
    save_image(image_cropped, "image_cropped") #saving cropped image
    
    
    # 3) Apply Canny edge detection
    grey = cv2.cvtColor(image_cropped, cv2.COLOR_BGR2GRAY) #turning image to greyscale
    blurred = cv2.GaussianBlur(grey, (5,5), 0) #blurring the image to remove noise. Here, we use Gaussian blur
    canny = cv2.Canny(blurred, 100, 150) #canny edge detection with a min threshold of 100 and max threshold of 150
    
   
    # 4) Draw green contours around letters in the cropped image
    (cnts, _) = cv2.findContours(canny.copy(),        #finding contours
                             cv2.RETR_EXTERNAL, 
                             cv2.CHAIN_APPROX_SIMPLE)
    image_letters = cv2.drawContours(image_cropped.copy(), cnts, -1, (0, 255, 0), 1) #drawing contours on copy of original image
    save_image(image_letters, "image_letters") #saving image with contours
    
    
    
# Define behaviour when called from command line
if __name__=="__main__":
    main()