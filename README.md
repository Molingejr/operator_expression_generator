**OPERATOR AND EXPRESSION GENERATOR**
===================================

Overview
--------
This is a simple software that generates expressions and operators after applying functions and/or constants together.
It provides both a GUI(Graphical User Interface) and a TUI(Text User Interface).

This project is a final year course project provided by the University of Buea, Cameroon.
It is a BSc in Computer Science project done by **_Molinge Lyonga Jr_**.

The development phases of this project is provided in other documents. This document will
contains information about the coding phase of the project and probably along with its
deployment.

Other documentations
--------------------
A lot of other documentations are found in each modules describing the modules and their
appropriate classes along with their methods and other key code fragments.

See docs directory for individual module documentations. Some links when click will show 404 error because they
require the internet to be displayed.

You can also use "pydoc -p 5000" to display an interactive web documentation on port 5000. Doesn't need the internet
to function.

Description
-----------
This system [Operator and Expression Generator] provides a graphical user interface
that allows users to carry out symbolic computations [by applying functions together] to
produce expressions as results. These results can also be in the intermediate [incomplete] form
which can still be manipulated to produce the desired result or expression. Functions are
provided or displayed on a grid table, where options for manipulating the grid’s display and
structure are also provided along with those for creating functions. Options for choosing
desired operators are given on the interface under various categories (for example Arithmetic,
Algebraic, Trigonometric). An operator chosen can be applied to arguments by performing
actions like drag-and-drop, right-clicking. There is also a separate grid provided for
intermediate results, which can be further manipulated. The expression generated can be output
into a file in one of three formats (reverse polish, prefix, or infix notations) via a back-end
function provided by the system. The resulting expressions are displayed on a grid cell found
at the intersection of the operator’s arguments. Repeated application of two arguments with
different operators results in different expressions saved on the arguments’ intersection cell and
provide an option for viewing this cell as a 2D format. The systems also provide means [file
menu] of saving and loading the grid on to our application from a file in a unique format. It
also provides a text user interface which does similar but limited functionalities as compared
to the GUI.

How to run software
-------------------
In order to execute the software, you can perform the following operations based on the operating system in use:

**Windows**
- Double click on the "main.py" file to run the GUI of the software.
- Or go to the terminal and navigate to the directory and type **"python3 main.py"**
- Double click on the "console.py" file to have access to the backend functions directly in a text user interface.

**Linux/MAC**
- Navigate to the directory in your terminal and type **"python3 main.py"**
- To access the backend directly type **"python3 console.py"**

NB: You can also generate a **standalone executable** file using PyInstaller as follows:
- Install PyInstaller with **"pip3 pyinstaller"**
- Run, **"pyinstaller --window main.py"** or **"pyinstaller --window console.py"** for both GUI and TUI.
