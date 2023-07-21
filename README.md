# 2D Sand Simulation 

This project is being done as a hobby so that I can introduce myself to the universe of physical simulations in two dimensions and cellular automata

## Requirements to run the project:
- have all the packages from the requirements.txt file installed;
- using at least Python 3.10.

## How to run:
1. create the virtual environment:
    - Linux: ```python3 -m venv venv```
    - Windows: ```python -m venv venv```
2. open the virtual environment:
    - Linux: ```source  ./venv/bin/activate```
    - Windows: ```venv\Scripts\activate```
3. install requirements: ```pip install -r requirements.txt```
4. run the project: ```python main.py```

## Done:
- Open the window;
- Create Cells;
- Draw the grid;
- Read mouse and keyboard events;
- Draw on the grid;
- Allow increasing and decreasing the brush radius;
- Save the grid as JSON;
- Load the save from JSON;
- Add menu;
- Get cell neighbors;

## To do:
- perform the simulations and cellular automata.

## Known bugs:

## Initial state:
- initial state of the selected cell is SAND;
- initial state of the circumference radius is 1.

## Events:
- right-click: paint the area (circumference) with the selected Cell;
- left-click: clean the area (paint with the VOID Cell);
- scrolling up: expand the radius of the circumference;
- scrolling down: reduce the radius of the circumference.

## Available cells:
- WOOD:
    - gravity: False
    - color: BROWN
    - colision: True
    - density: 3
- SAND:
    - gravity: TRUE
    - color: YELLOW
    - colision: True
    - density: 3
- WATER:
    - gravity: TRUE
    - color: GREEN
    - colision: True
    - density: 2
- WATER:
    - gravity: TRUE
    - color: CYAN
    - colision: True
    - density: 1
- FIRE:
    - gravity: TRUE
    - color: RED
    - colision: False
    - density: 0
- GAS:
    - gravity: TRUE
    - color: GRAY
    - colision: True
    - density: 0
- BLOCK:
    - gravity: FALSE
    - color: BLACK
    - colision: True
    - density: -1 --> Can't move using density difference
- VOID:
    - gravity: None
    - color: WHITE
    - colision: None
    - density: None