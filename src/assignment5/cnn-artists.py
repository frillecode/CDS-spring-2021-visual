#!/usr/bin/python

import os
import cv2
import argparse
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (Conv2D, 
                                     MaxPooling2D, 
                                     Activation, 
                                     Flatten, 
                                     Dense)
from tensorflow.keras.utils import plot_model
from tensorflow.keras.optimizers import SGD
from tensorflow.keras import backend as K


class convolutionalNeuralNetwork():
    '''This is a class for creating and fitting a convoloutional neural network
    '''
    def __init__(self, args):
        self.args = args
    
    def preprocessing(self, train_folder, test_folder): 
        '''This function loads and preprocesses the train and test data set
        Input:
            train_folder: path to folder with train data
            test_folder: path to folder with test data
        '''
        # Empty list for labels and for images
        labelNames = []
        trainY = []
        trainX = []
        testY = []
        testX = []
        
        # Loop through train data
        for subfolder in Path(train_folder).glob("*"):
            # Extract name of folder to use for label
            artist = os.path.basename(subfolder)
            labelNames.append(artist) #create list of possible labels
            # Take the current subfolder
            for pic in Path(subfolder).glob("*.jpg"):
                pic_array = cv2.imread(str(pic)) #load image
                compressed = cv2.resize(pic_array, 
                                        (self.args['resizing_values'], self.args['resizing_values']), #size of resized image
                                        interpolation = cv2.INTER_AREA)
                trainX.append(compressed) #append image to list
                trainY.append(artist) #append label to list

        # Loop through test data
        for subfolder in Path(test_folder).glob("*"):
            # Extract name of folder to use for label
            artist = os.path.basename(subfolder)
            # Take the current subfolder
            for pic in Path(subfolder).glob("*.jpg"):
                pic_array = cv2.imread(str(pic)) #load image
                compressed = cv2.resize(pic_array, #
                                        (self.args['resizing_values'], self.args['resizing_values']), #size of resized image
                                        interpolation = cv2.INTER_AREA) 
                testX.append(compressed) #append image to list
                testY.append(artist) #append label to list
        
        # Turn into numpy arrays (this is the format that we need for the model) and assign to self
        self.labelNames = labelNames
        self.trainX = np.array(trainX)
        self.trainY = np.array(trainY)
        self.testX = np.array(testX)
        self.testY = np.array(testY)
        
        # Normalization
        self.trainX = self.trainX.astype("float") / 255.
        self.testX = self.testX.astype("float") / 255.
        
        # Label binarization
        lb = LabelBinarizer()
        self.trainY = lb.fit_transform(self.trainY)
        self.testY = lb.fit_transform(self.testY)

        
        
    def create_model(self):
        '''This function initializes and compiles the model for the convolutional neural network
        '''
        # Define model
        self.model = Sequential() #initialise model

        #define CONV => RELU layer
        self.model.add(Conv2D(self.args['neurons_in_hidden_layer'], (3, 3), #first argument = neurons, second = kernel size
                         padding="same", #adding a layer of 0 
                         input_shape=(self.args['resizing_values'], self.args['resizing_values'], 3)))
        #activation function
        self.model.add(Activation("relu"))

        #softmax classifier
        self.model.add(Flatten())
        self.model.add(Dense(10))
        self.model.add(Activation("softmax"))
        
        # Compile model
        opt = SGD(lr =.01) #learning rate
        self.model.compile(loss="categorical_crossentropy", #loss function
                          optimizer=opt, #specifying optimizer
                          metrics=["accuracy"])
        
        return self.model.summary()
    
    def fit_model(self):
        '''This function fits the model to the data and returns the classification report
        '''
        # Fit model
        self.H = self.model.fit(self.trainX, self.trainY, 
                                validation_data=(self.testX, self.testY), 
                                batch_size=32,
                                epochs=self.args['epochs'],    
                                verbose=1)
        
        # Get predictions
        self.predictions = self.model.predict(self.testX, batch_size=32) 
        
        # Comparing predictions to our test labels
        class_rep = classification_report(self.testY.argmax(axis=1),
                                          self.predictions.argmax(axis=1),
                                          target_names=self.labelNames)
        
        # Save classification report   
        outpath = os.path.join("out", "evaluation_metric.txt")
        with open(outpath, "w", encoding="utf-8") as file:
            file.write(class_rep)
        
        return class_rep
    
    def plot_history(self): 
        ''' Plot of the model as it learns 
        '''
        # Visualize performance
        plt.style.use("fivethirtyeight")
        plt.figure()
        plt.plot(np.arange(0, self.args['epochs']), self.H.history["loss"], label="train_loss")
        plt.plot(np.arange(0, self.args['epochs']), self.H.history["val_loss"], label="val_loss")
        plt.plot(np.arange(0, self.args['epochs']), self.H.history["accuracy"], label="train_acc")
        plt.plot(np.arange(0, self.args['epochs']), self.H.history["val_accuracy"], label="val_acc")
        plt.title("Training Loss and Accuracy")
        plt.xlabel("Epoch #")
        plt.ylabel("Loss/Accuracy")
        plt.legend()
        plt.tight_layout()
        plt.show()
        
        # Save plot
        plot_path = os.path.join("out", "performance.png")
        plt.savefig(plot_path, dpi=300, bbox_inches="tight")
        
# Define main function    
def main():
    ap = argparse.ArgumentParser(description="[INFO]  This script takes image data, trains a convolutional Neural Network model, and prints the classification report to the terminal. ")
    # Argument for specifying pixel values for resizing images
    ap.add_argument("-r", 
                "--resizing_values", 
                required=False, 
                type=int,
                default=200,
                help="int, pixel size for resizing images (e.g. if you write 28, the images will be resized to 28x28 pixels)") 
    # Argument for specifying number of neurons in hidden layer
    ap.add_argument("-n",  
                "--neurons_in_hidden_layer", 
                required=False, 
                type=int, 
                default=32, 
                help="int, value for hidden layers")
    # Argument for specifying number of epochs
    ap.add_argument("-e", 
                "--epochs", 
                required=False, 
                type=int, 
                default=40, 
                help="int, number of epochs") 

    
    args = vars(ap.parse_args())
    
    # Run 
    convNN = convolutionalNeuralNetwork(args)
    print("[INFO] Loading and preprocessing data")
    convNN.preprocessing(train_folder = os.path.join("..", "..", "data", "assignment5", "training", "training"), 
                         test_folder = os.path.join("..", "..", "data", "assignment5", "validation", "validation"))
    print("[INFO] Creating model")
    summary = convNN.create_model()
    print(summary)
    print("[INFO] Fitting model")
    classification_report = convNN.fit_model()
    print(f"[INFO] Classification report: \n {classification_report}")
    convNN.plot_history()
    

# Define behaviour when called from command line
if __name__=="__main__":
    main()
    print("[INFO] DONE! You can find the results of the performance of the model in the output-folder")