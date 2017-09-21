# File name: operators.py

import re

__author__ = 'Molinge'


class Arithmetic:
    """
    This class handles all the arithmetic manipulations
    """
    @staticmethod
    def add(func1, func2):
        return '(' + func1 + '+' + func2 + ')'

    @staticmethod
    def substract(func1, func2):
        return '(' + func1 + '-' + func2 + ')'

    @staticmethod
    def multiply(func1, func2):
        return '(' + func1 + '*' + func2 + ')'

    @staticmethod
    def divide(func1, func2):
        return '(' + func1 + '/' + func2 + ')'


class Algebraic:
    """
    This class handles all the algebraic manipulations
    """
    @staticmethod
    def compose(func1, func2, arg=None):
        """This applies the second function into the first function"""
        if func1.find('x1') == -1:
            return None
        if arg is None:
            return '{0}o{1}'.format(func1, func2)
        elif arg == 1:
            regex1 = re.compile(r'[x y]1')
            obj1 = re.search(regex1, func2)
            if obj1 is None:
                return False
            string1 = func2[obj1.start():obj1.end()]
            return func2.replace(string1, '{0}o{1}'.format(func1, string1))
        elif arg == 2:
            regex2 = re.compile(r'[x y]2')
            obj2 = re.search(regex2, func2)
            if obj2 is None:
                return False
            string2 = func2[obj2.start():obj2.end()]
            return func2.replace(string2, '{0}o{1}'.format(func1, string2))

    @staticmethod
    def substitute(func1, func2, arg=None):
        """This replaces the second function's specified argument(s) with the first function"""

        try:
            regex1 = re.compile(r'[x y]1')
            obj1 = re.search(regex1, func2)
            string1 = func2[obj1.start():obj1.end()]

            regex2 = re.compile(r'[x y]2')
            obj2 = re.search(regex2, func2)
            string2 = func2[obj2.start():obj2.end()]

        except AttributeError:
            pass
        finally:
            if arg is None and (obj1 is not None):
                func2 = func2.replace(string1, func1)
                return func2.replace(string2, func1)
            elif arg is None and (obj2 is None):
                return func2.replace(string1, func1)
            elif arg == 1:
                return func2.replace(string1, func1)
            elif arg == 2:
                return func2.replace(string2, func1)
            else:
                return None


class Trigonometric:
    """
    This class handles all the trigonometric function manipulation
    """

    @staticmethod
    def cos(func):
        return 'cos({})'.format(func)

    @staticmethod
    def sin(func):
        return 'sin({})'.format(func)

    @staticmethod
    def tan(func):
        return 'tan({})'.format(func)


class Operators:
    """
    This class contains a set of operator types and their instances inside a dictionary
    And it provides methods for manipulating the dictionary's contents
    """
    def __init__(self):
        """Constructor initializes our list of operators and the chosen operator"""
        self._operators = {
            "Arithmetic": ['Add', 'Subtract', 'Multiply', 'Divide'],
            "Algebraic": ['Compose', 'Substitute'],
            "Trigonometric": ['cos', 'sin', 'tan']
        }

        self._chosen_op = self._operators['Arithmetic'][0]

    def get_chosen_op(self):
        return self._chosen_op

    def set_chosen_op(self, op_type, instance):
        if op_type in self._operators:
            if instance in self._operators[op_type]:
                self._chosen_op = instance

    def get_operators(self):
        return self._operators

    def add_operator(self, op_type, instance):
        if op_type in self._operators:
            self._operators[op_type].append(instance)
        else:
            self._operators[op_type] = [instance]

    def display_operators(self):
        for i in self._operators:
            print(i, ' : ', end='')
            for j in self._operators[i]:
                print(j)
            print()