# File name: processing.py

"""
This module contains classes responsible for controlling and managing our Text-user
console application.
It uses other classes from different modules to run our console app.
It provides some backend methods and also uses other backend methods allowing text console
users a high degree of flexibility and control over the application.
"""
from operators import *
from create_func_const import *
from grid import Grid

__author__ = 'Molinge'


class Console:
    """
    This classes contains methods[mostly static] for our console application (Non-GUI).
    It allows the user to carry out main functionality of the GUI in a console app(terminal
    based).
    """
    def __init__(self):
        """Creates our grid class and runs our application"""
        self.app_grid = Grid()      # create a grid object
        self.interface()

    def interface(self):
        """
        This controls the Console application and use's most of the other static
        methods in order to do so.
        """
        ops = ['', 'add', 'substract', 'multiply', 'divide', 'substitute', 'compose', 'cos', 'sin', 'tan']

        choice = self.menu()
        while choice != 5:
            if choice == 1:
                self.app_grid.display_grid()
            elif choice == 2:
                n = input("Enter function's/constant's name: ")
                t = input("Enter it's type(Function/Constant): ")
                a = int(input("Enter Number of arguments: "))
                s = input("Enter section: ")
                f = self.create_func(n, t, a, s)
                if s == 'Vertical':
                    self.app_grid.add_row(f.get_function())
                elif s == 'Horizontal':
                    self.app_grid.add_column(f.get_function())
            elif choice == 3:
                # Get the operator number from user and assign the corresponding operator in the ops list
                # into the operator variable
                operator = ops[self.display_operators()]

            elif choice == 4:
                # Display the grid and get the two functions to apply from the user
                func1 = input("Enter a function position from at vertical location on the grid: ")
                func2 = input("Enter a function position from the horizontal location on the grid: ")

                print("The resulting computation is as follows:")
                item = self.calculate(operator, self.app_grid.get_item(func1),
                                      self.app_grid.get_item(func2))
                self.app_grid.add_item(item, func1[0], func2[1])

            print()
            choice = self.menu()

    @staticmethod
    def calculate(operator, string1, string2):
        """
        This does the calculations by performing the operations on its arguments.
        And returning the corresponding result.
        """
        if operator == 'add':
            return Arithmetic.add(string1, string2)
        elif operator == 'subtract':
            return Arithmetic.substract(string1, string2)
        elif operator == 'multiply':
            return Arithmetic.multiply(string2)
        elif operator == 'divide':
            return Arithmetic.divide(string2)
        elif operator == 'substitute':
            return Algebraic.substitute(string2)
        elif operator == 'compose':
            return Algebraic.compose(string1, string2)

    @staticmethod
    def create_func(func_name, func_type, num_args, section):
        """This method returns an object of a created function."""
        func = CreateFuncConst()
        func.set_name(func_name)
        func.set_type(func_type)
        func.set_args(num_args)
        func.set_section(section)
        func.create_function()
        return func

    @staticmethod
    def menu():
        """
        This displays the main menu of the console app.
        It then collects and returns the choice of the user.
        """
        print("\nChoose which operation to carryout")
        print("----------------------------------\n")
        print("1. Display Grid")
        print("2. Create Function/Constant")
        print("3. Choose operator")
        print("4. Perform calculation")
        print("5. Exit\n")
        choice = int(input("Enter your choice: "))
        return choice

    @staticmethod
    def display_operators():
        """
        This displays the list of available operators.
        It then collects and returns the choice of the user.
        """
        print("Available operators are")
        print("Arithmetic\n\t1.Addition\n\t2.Subtract\n\t3.Multiplication\n\t4.Division\n")
        print("Algebraic\n\t5.Substitution\n\t6.Composition")
        print("Trigonometric\n\t7.cos\n\t8.sin\n\t9.tan")

        choice = int(input("Enter an Operator number to choose: "))
        return choice


if __name__ == '__main__':
    Console()