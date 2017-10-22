# File name: create_func_const.py

"""
This module contains classes responsible for creating functions and constants
on the GUI or Text application.
"""

__author__ = 'Molinge'


class CreateFuncConst:
    """
    This class provides methods for collecting data about a function and settings it's attributes.
    It then provides a method that takes this data and create a function as a string
    """
    def __init__(self):
        self._name = None
        self._type = 'Constant'
        self._args = 0
        self._section = 'Vertical'
        self._function = None

    def set_name(self, name):
        if (not name.isalnum()) or (name[0].isnumeric()):
            print("Invalid function name.")
            return
        self._name = name

    def set_type(self, type):
        if type not in ['Constant', 'Function']:
            print("Invalid type. It can either be a Constant or Function")
            return
        self._type = type

    def set_args(self, args):
        if (not isinstance(args, int)) or (args < 0):
            print("Argument is either not an integer or less than 0.")
            print("Only integers > 0 are accepted")
            return
        self._args = args

    def set_section(self, section):
        if section in ['Vertical', 'Horizontal']:
            self._section = section
        else:
            print("Enter a valid section. either 'Vertical' or 'Horizontal'")
            return

    def create_function(self):
        if self._name is None:
            print("Function has no name or an invalid name")
            return
        if self._type == 'Constant':
            if self._args == 0:
                self._function = self._name
            else:
                print("Cannot create a constant with arguments")
                return
        else:
            if self._args >= 0:
                if self._section == 'Vertical':
                    variable = 'x'
                else:
                    variable = 'y'
                self._function = self._name + '('
                for num in range(self._args):
                    self._function += variable + str(num+1)
                    if num < (self._args - 1):
                        self._function += ','
                self._function += ')'
            else:
                print("A function should have an argument")

    def get_function(self):
        return self._function

