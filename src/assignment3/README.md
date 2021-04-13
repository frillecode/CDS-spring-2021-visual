# Assignment 3
The structure of the files belonging to this assignment is as follows:  
  - Data: _../../data/assignment3/_ 
  - Code: _edge\_detection.py_
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

### Running scripts
After updating the repo (see above), you can run the .py-files from the command-line by writing the following:
``` bash
$ cd CDS-spring-2021-visual
$ source frille-vis/bin/activate
$ cd src/assignment3
$ python3 edge\_detection.py
```
 