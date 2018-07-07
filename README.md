# OPERATOR AND EXPRESSION GENERATOR


## Overview

This project provides a platform for generating operators and expressions that can be use for various purposes in 
systems external to the platform. It thus, construct arbitrary mathematical functions and maps, their composition and 
application, which expressions are given via the interface (GUI/TUI) and then simplified, evaluated or otherwise 
interpreted. It uses event-driven programming and its tools and interpretation exploits pattern matching.

This project is a final year course project provided by the University of Buea, Cameroon.
It is a BSc in Computer Science project done by **_Molinge Lyonga Jr_**.


## Installation of software

Most Linux and MacOS systems comes with Python 3 installed. Ensure that Python 3 is installed in your system otherwise
install it.
```
$ python --version
$ pip --version
```
If Python or Pip is not installed, you can check the official Python website at [www.python.org](https://www.python.org/)

#### Create a virtual environment

`$ python -m venv <name of virtual env>`

Once you've created a virtual environment, you may activate it.
* On Windows, run:
`$ <path of virtual env>\Scripts\activate`
* On Unix or MacOS, run:
`$ source <path of virtual env>/bin/activate` 

#### Install requirements
`$ pip3 install -r requirements.txt` 

#### How to run software
* GUI mode `$ python main.py`
* Console mode `$ python console.py`

#### How to generate standalone application
**Standalone executables** can be generated using **PyInstaller** package as follows:
```
$ pip install pyinstaller
$ pyinstaller  --window main.py
$ pyinstaller --window console.py
```
