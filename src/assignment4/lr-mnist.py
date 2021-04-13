#!/usr/bin/python

# Import necessary libraries/modules
import os
import sys
sys.path.append(os.path.join("..", ".."))
import argparse
import numpy as np
from sklearn import metrics
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


class LogRegMNIST():
    """This is a class for performing a Logistic Regression classification on the MNIST dataset.
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
                                                               random_state=self.args['random_state'], 
                                                               train_size=1-self.args['test_size'], 
                                                               test_size=self.args['test_size']) 
        
    def train_model(self):
        """Function for training the Logistic Regression classifier.
        
        """
        # Initialise model and fit that model to the training data and labels
        clf = LogisticRegression(penalty='none', 
                                 tol=0.1, 
                                 solver='saga',
                                 multi_class='multinomial').fit(self.X_train, self.y_train)
        return clf
    
    def calc_eval_metrics(self, clf):
        """Function for calculating evaluation metrics.
        Input:
            clf: trained Logistic Regression classifier
        """
        # Take the trained model and use to predict test class
        self.y_pred = clf.predict(self.X_test)
        # Calculate evaluation metrics
        cm = metrics.classification_report(self.y_test, self.y_pred)
        
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
        clf = self.train_model()
        # Calculate evaluation metrics
        cm = self.calc_eval_metrics(clf)
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
    ap = argparse.ArgumentParser(description="[INFO] This script uses the full MNIST data set, trains a Logistic Regression Classifier, and prints and saves the evaluation metrics to the terminal.") 
    # Argument for specifying a random-state value
    ap.add_argument("-rs",  
                "--random_state", 
                required=False,  
                type=int,
                default=9,
                help="int, value for random state of model")
    # Argument for specifying size of test set
    ap.add_argument("-ts", 
                "--test_size", 
                required=False, 
                type=percentFloat, #here I use the function I created above
                default=0.2, 
                help="float, proportional size of test set (must be number between 0 and 1)") 
    # Argument for specifying filename of evaluation metrics
    ap.add_argument("-fn", 
                "--filename", 
                required=False, 
                type=str, 
                default="evaluation_metrics_LR", 
                help="str, filename for saving the evaluation metrics") 

    args = vars(ap.parse_args())

    # Loading data
    digits = datasets.load_digits()
    
    # Turning into LogRegMNIST object (the class I created above)
    logreg = LogRegMNIST(digits, args)
    
    # Perform classification
    logreg.run_classifier()

    
# Define behaviour when called from command line
if __name__=="__main__":
    main()
    print("[INFO] The evaluation metrics has been saved in 'out/'.")
    
        