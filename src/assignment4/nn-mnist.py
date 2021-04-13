#!/usr/bin/python

# Import necessary libraries/modules
import sys,os
sys.path.append(os.path.join("..", ".."))
import argparse
import numpy as np
from utils.neuralnetwork import NeuralNetwork
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets


class NeuralNetworkMNIST():
    """This is a class for performing a Neural Network classification on the MNIST dataset.
    """
    def __init__(self, digits, args):
        self.args = args
        self.X = digits.data.astype("float") #extracting data
        self.y = digits.target               #extracting labels
        
    def split(self):
        """ Function for splitting MNIST dataset into train and test sets. 
        """
        
        # Normalize (MinMax regularization)
        self.X = (self.X - self.X.min())/(self.X.max() - self.X.min())
        
        # Split into train and test set
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, 
                                                               self.y,  
                                                               train_size=1-self.args['test_size'], 
                                                               test_size=self.args['test_size']) 
     
    def train_model(self):
        """Function for training the Neural Network classifier.   
        """
        # Convert labels from integers to vectors
        self.y_train = LabelBinarizer().fit_transform(self.y_train)
        self.y_test = LabelBinarizer().fit_transform(self.y_test)
        
        # Creating a numpy array with layers for the neural network based on the hidden layer values parsed in the command-line
        layers = [] #empty list
        layers.append(self.X_train.shape[1]) #appending input layer
        [layers.append(self.args['hidden_layers'][x]) for x in range(len(self.args['hidden_layers']))] #appending hidden layers
        layers.append(10) #appending output layer
        layers = np.array(layers) #turn into numpy array
        
        # Training neural network and fitting it to data
        print("\n[INFO] Training network... \n")
        nn = NeuralNetwork(layers)
        print(f"[INFO] {nn}")
        nn.fit(self.X_train, self.y_train, epochs=self.args['epochs'])
        
        return nn
        
        
    def calc_eval_metrics(self, nn):
        """Function for calculating evaluation metrics.
        Input:
            nn: trained neural network
        """
        # Take the trained model and use to predict test class
        predictions = nn.predict(self.X_test) 
        predictions = predictions.argmax(axis=1) 
        
        # Calculate evaluation metrics
        cm = classification_report(self.y_test.argmax(axis=1), predictions)
        
        return cm

    
    def save_eval_metrics(self, cm):
        """Function for saving file with evaluation metrics.
        Input:
            cm: evaluation metrics
        """
        # Specifying output path
        outpath = os.path.join("out", f"{self.args['filename']}.txt")
        # Writing file
        with open(outpath, "w", encoding="utf-8") as file:
            file.write(cm)
    
    def run_classifier(self):
        """Function for running all functions within the class in the correct order.
        """
        # Splitting data
        self.split()
        # Train model
        nn = self.train_model()
        # Calculate evaluation metrics
        cm = self.calc_eval_metrics(nn)
        # Print evaluation metrics
        print(f"\n EVALUATION METRICS: \n {cm}")
        # Save evaluation metrics
        self.save_eval_metrics(cm)

# Creating a function that checks whether a given value is between 0 and 1 and return an error if it is not. This is used to ensure that only a test_size-argument within the correct range can be parsed in the command-line. 
def percentFloat(string):
    value = float(string)
    if value < 0 or value > 1:
        raise argparse.ArgumentTypeError('Value has to be between 0 and 1')
    return value           

    
def main():
    ap = argparse.ArgumentParser(description="[INFO] This script uses the full MNIST data set, trains a Neural Network Classifier, and prints and saves the evaluation metrics to the terminal.") 
    # Argument for specifying size of test set
    ap.add_argument("-ts", 
            "--test_size", 
            required=False, 
            type=percentFloat, 
            default=0.2, 
            help="float, proportional size of test set (must be number between 0 and 1)") 
    # Argument for specifying number and values of hidden layers
    ap.add_argument("-hl",  
                "--hidden_layers", 
                required=False,  
                nargs="+",
                type=list,
                default=[32],
                help="int, values for hidden layers (insert with spaces between values, e.g.: '-hl 32 16')")
    # Argument for specifying number of epochs
    ap.add_argument("-e", 
                "--epochs", 
                required=False, 
                type=int, 
                default=1000, 
                help="int, number of epochs") 
    # Argument for specifying filename of evaluation metrics
    ap.add_argument("-fn", 
                "--filename", 
                required=False, 
                type=str, 
                default="evaluation_metrics_NN", 
                help="str, filename for saving the evaluation metrics")   
    
    args = vars(ap.parse_args())

    # Loading data
    digits = datasets.load_digits()
    
    # Turn into NeuralNetworkMNIST object
    neural_network = NeuralNetworkMNIST(digits, args)
    
    # Perform classification
    neural_network.run_classifier()
    

# Define behaviour when called from command line
if __name__=="__main__":
    main()
    print("[INFO] The evaluation metrics has been saved in 'out/'.")
    
        