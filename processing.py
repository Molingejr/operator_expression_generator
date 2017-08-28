# File name: processing.py

from operators import *
from create_func_const import *
from grid import Grid

__author__ = 'Molinge'


def calculate(operator, string1, string2):
    if operator == 'add':
        return Arithmetic.add(string1, string2)
    elif operator == 'subtract':
        return Arithmetic.substract(string1, string2)
    elif operator == 'multiply':
        return Arithmetic.multiply(string1, string2)
    elif operator == 'divide':
        return Arithmetic.divide(string1, string2)
    elif operator == 'substitute':
        pass
    elif operator == 'compose':
        pass


def save_func(func_name, func_type, num_args, section):
    func = CreateFuncConst()
    func.set_name(func_name)
    func.set_type(func_type)
    func.set_args(num_args)
    func.set_section(section)
    func.create_function()
    return func


def interface():
    grid = Grid()       # create a grid object
    ops = ['', 'add', 'substract', 'multiply', 'divide', 'substitute', 'compose', 'cos', 'sin', 'tan']

    # Display the available operators
    print("Available operators are")
    print("Arithmetic\n\t1.Addition\n\t2.Subtract\n\t3.Multiplication\n\t4.Division\n")
    print("Algebraic\n\t5.Substitution\n\t6.Composition")
    print("Trigonometric\n\t7.cos\n\t8.sin\n\t9.tan")

    # Get the operator number from user and assign the corresponding operator in the ops list
    # into the operator variable
    operator = ops[int(input("Enter an operator number to select: "))]

    # Display the grid and get the two functions to apply from the user
    grid.display_grid()
    func1 = input("Enter a function name from at vertical location on the grid: ")
    func2 = input("Enter a function name from the horizontal location on the grid: ")

    print("The resulting computation is as follows:")
    print(calculate(operator, func1, func2))