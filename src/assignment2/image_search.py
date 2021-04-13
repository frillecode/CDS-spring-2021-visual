#!/usr/bin/python

# Import libraries
import os
import sys
sys.path.append(os.path.join("..", ".."))
import cv2
import csv
import glob
import numpy as np
from utils.imutils import jimshow
from utils.imutils import jimshow_channel
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

# Function for reading image + calculating and normalizing 3D color histogram of image
def image_hist(image_path):
    image = cv2.imread(image_path)
    
    hist = cv2.calcHist([image], [0,1,2],None, [8,8,8],[0,256, 0,256, 0,256])  
    hist = cv2.normalize(hist, hist, 0,255, cv2.NORM_MINMAX)
    
    return hist


# Function that calculates distance from each image to the target image
def chisqd_distance(target_image, path_to_images):
    filename = [] #empty list for filenames
    distance = [] #empty list for distances
    
    # Calculate 3D color histogram of target image using the function defined above
    hist_target = image_hist(target_image)
    
    # Loop through images in specified path
    for filepath in Path(path_to_images).glob("*.jpg"):
        # Skipping target image
        if str(filepath) == target_image:
            pass
        # Loading rest of images
        else:
            # Extract filename
            this_filename = os.path.basename(filepath)
            this_filename = os.path.splitext(this_filename)[0]
            # Save filename
            filename.append(this_filename)
            
            # Apply function defined above to calculate 3D color histogram of image 
            hist = image_hist(str(filepath))

            # Calculate chi-squared distance to target image and round to 2 decimals
            distance.append(round(cv2.compareHist(hist_target, hist, cv2.HISTCMP_CHISQR), 2))

            # Turn lists of filename and distance into dataframe using zip()
            df = pd.DataFrame(zip(filename, distance))
            df.columns = ["filename", "distance"]
            
    return df

# Function for writing df to .csv-file
def write_csv(df):
        # Write dataframe to a .csv-file and save in folder "out"
        outpath = os.path.join("out", "distances.csv")
        df.to_csv(outpath)

        
# Defining main-function
def main():
    # Choose target image
    target_image_path = os.path.join("..", "..", "data", "assignment2", "jpg", "image_0399.jpg")  #specify path to target image
    
    # Apply function to calculate chi-squared distances to target image
    df = chisqd_distance(target_image = target_image_path, path_to_images = os.path.join("..","..", "data", "flower_data", "jpg")) 
    
    # Save dataframe to a .csv-file
    write_csv(df)
    
    # Print filename of image that has the smallest chi-squared distance from the target image
    #this returns the content of the column 'filename' for the min() value of the column 'distance'
    filename_smallest_distance = df.loc[df['distance'] == min(df['distance']), 'filename'].item() 
    #print
    return(print(f"'{filename_smallest_distance}' has the smallest distance ({min(df['distance'])}) to the target image"))


# Define behaviour when called from command line
if __name__=="__main__":
    main()