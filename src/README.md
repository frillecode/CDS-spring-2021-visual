## Weekly assignments
Each week I will upload my answers to the given assignments here under the following names:
- __Assignment 1:__   
  - Data: _../data/assignment1/_ 
  - Code: _assignment1/basic\_image\_processing.ipynb_  
  - Results: _assignment1/out/_  
- __Assignment 2:__  
  - Data: _../data/assignment2/_ 
  - Code: _assignment2/image\_search.py_   
  - Results: _assignment2/out/_  
- __Assignment 3:__  
  - Data: _../data/assignment3/_ 
<<<<<<< HEAD
  - Code: _assignment3/edge\_detection.py_
  - Results: _assignment3/out/_  
- __Assignment 4:__  
  - Data: inbuilt 'mnist'-dataset from ```sklearn```  
  - Code: _assignment4/nn-mnist.py_ , _assignment4/lr-mnist.py_  
  - Results: _assignment4/out/_  
- __Assignment 5:__  
  - Data: File too big to push to github. Download [here](https://www.kaggle.com/delayedkarma/impressionist-classifier-data) and upload to _../data/assignment5/_ if you want to run the script.
  - Code: _assignment5/cnn-artists.py_  
  - Results: _assignment5/out/_
=======
  - Code: _edge\_detection.py_
  - Results: _out/assignment3/_  
- __Assignmetn 4:__  
  - Data: inbuild _mnist_-dataset from ```sklearn```  
  - Code: _nn-mnist.py_ , _lr-mnist.py_  
  - Results: _out/assignment4/_  
>>>>>>> parent of ef78815c... updated readme


### Cloning repo and installing dependencies 
To run the scripts, I recommend cloning this repository and installing relevant dependencies in a virtual ennvironment:

```bash
$ git clone https://github.com/frillecode/CDS-spring-2021-visual.git
$ cd CDS-spring-2021-visual
$ bash ./create_venv.sh
````
If you run into issues with some libraries/modules not being installed correctly when creating the virtual environment, install these manually by running the following:  
```bash
$ cd CDS-spring-2021-visual
$ source frille-vis/bin/activate
$ pip install {module_name}
$ deactivate
```

### Running scripts
After updating the repo (see above), you can run the .py-files from the command-line by writing the following:
``` bash
$ cd CDS-spring-2021-visual
$ source frille-vis/bin/activate
$ cd src/assignment{number}
$ python3 {filename}.py
```
