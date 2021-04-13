# Assignment 5
The structure of the files belonging to this assignment is as follows:  
  - Data: File too big to push to github. Download [here](https://www.kaggle.com/delayedkarma/impressionist-classifier-data) and upload to _../../data/assignment5/_ if you want to run the script.
  - Code: _cnn-artists.py_  
  - Results: _out/_

### Cloning repo and installing dependencies 
To run the script, I recommend cloning this repository and installing relevant dependencies in a virtual ennvironment:

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

### Running script
After updating the repo (see above), you can run the .py-file from the command-line by writing the following:
``` bash
$ cd CDS-spring-2021-visual
$ source frille-vis/bin/activate
$ cd src/assignment5
$ python3 cnn-artists.py
```
 
The script take different optional arguments that can be specified in the command-line if you feel like it :-) . Before running the scripts, you can check which arguments can be parsed for each script by running:
``` bash
$ python3 cnn-artists.py --help
```
