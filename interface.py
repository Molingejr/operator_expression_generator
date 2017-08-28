# File name: interface.py

from grid import Grid
from intermediate import IntermediateGrid
from operators import Operators
from create_func_const import CreateFuncConst
import processing

__author__ = 'Molinge'


class Interface:
    def __init__(self):
        self._grid = Grid()
        self._intermediate = IntermediateGrid()
        self._operators = Operators()
        self._func_const_create = CreateFuncConst()

    def display_grid(self):
        self._grid.display_grid()

    def get_grid(self):
        self.get_grid()

    def display_intermediate(self):
        self._intermediate.display_grid()

    def get_intermediate(self):
        self._intermediate.get_grid()

    def display_operators(self):
        self._operators.display_operators()

    def get_operators(self):
        self._operators.get_operators()