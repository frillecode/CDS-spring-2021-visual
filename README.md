# Visual Analytics - Spring 2021
This is my personal repository with code and data related to the Spring 2021 module _Visual Analytics_ as part of the bachelor's tilvalg in [Cultural Data Science](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/) at Aarhus University.

This repository is in active development, with new material being pushed on a weekly basis. 

## Technicalities
Each week I will upload my answers to the given assignment. These can be found in the folder, _src_, along with a description of how to run them. 

To run scripts within this repository, I recommend cloning the repository and installing relevant dependencies in a virtual ennvironment:

```bash
$ git clone https://github.com/frillecode/CDS-spring-2021-visual.git
$ cd CDS-spring-2021-visual
$ bash ./create_venv.sh
```
From then on, every time you use it, make sure to update the repository and install any new dependencies:
```bash
$ cd CDS-spring-2021-visual
$ git pull origin main
$ bash ./create_venv.sh
```
If you run into issues with some libraries/modules not being installed correctly when creating the virtual environment, install these manually by running the following:
```bash
$ cd CDS-spring-2021-visual
$ source frille-vis/bin/activate
$ pip install {module_name}
$ deactivate
```


## Repo structure

This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```data```| A folder to be used for datasets that I use in assignments.
```src``` | For Python scripts developed in class and as part of assignments.
```utils``` | Utility functions that are written by Ross, and which we'll use in class.

## Acknowledgements
Credits for the original repository structure goes to [Ross Deans Kristensen-McLachlan](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html).
