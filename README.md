**OPERATOR AND EXPRESSION GENERATOR**
===================================

Overview
--------
This is a simple software that generates expressions and operators after applying functions and/or constants together.
It provides both a GUI(Graphical User Interface) and a TUI(Text User Interface).

This project is a final year course project provided by the University of Buea, Cameroon.
It is a BSC in Computer Science project given to Molinge Lyonga Jr.

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
This system [Operator and Expression Generator] provides a graphical user interface and a text user interface [for 
usage of some back-end functions] that allows users to carryout computations [by applying functions and/or constants together] to produce expressions as 
results. These results can also be in the intermediate[incomplete] form which can still be manipulated to produce the 
desire result or expression. Functions and Constants are provided or displayed on a grid table, where options for 
manipulating the grid’s display and structure are also provided along with those for creating functions/constants. 
Options for choosing desired operators are given on the interface under various categories. An operator chosen can be 
applied on arguments [functions/constants on grid] by performing some actions [like drag-and-drop, right-clicking]. 
There’s also a grid provided for intermediate results for further manipulations. The expression generated can be 
outputted into a file in a chosen format [like reverse polish, prefix, or infix notations] by means of a back-end 
function provided by the system through the Text user interface. The resulting expressions are displayed on a cell 
[on the grid] found at the intersection of the operator’s arguments [functions/constants and functions/constants on 
the grid]. Repeated application of two arguments with different operators result in different expressions saved on 
the arguments intersection cell [cell is of 2D format] and provide an option for viewing this cell as a 2D format. 
The systems also provide means [file menu] of saving and loading the grid on to our application from a file in a unique
format.

How to run software
-------------------
In order to execute the software, you can perform the following operations based on the operating system in use:

**Windows**
- Double click on the "main.py" file to run the GUI of the software.
- Or go to the terminal and navigate to the directory and type **"python3 main.py"**
- Double click on the "console.py" file to have access to the backend functions directly in a text user interface.

**Ubuntu/Linux**
- Navigate to the directory in your terminal and type **"python3 main.py"**
- To access the backend directly type **"python3 console.py"**
