# File name: intermediate.py
# This file contains our intermediate Grid data structure
__author__ = 'Molinge'


class IntermediateGrid:
    """
    This class represents a grid for storing information which can be manipulated on
    It's purpose is for displaying and manipulating intermediate data.
    """
    def __init__(self):
        """Constructor initializes the grid"""
        self._grid = [[None]]

    def __len__(self):
        """This returns the length of our grid. i.e how many rows"""
        return len(self._grid)

    def clear(self):
        """Sets the grid to it's default format"""
        self._grid = [[None]]

    def add_row(self):
        """This method adds a row at the end of the grid"""
        if len(self._grid) == 0 or len(self._grid[0]) == 1:
            self._grid.append([None])
        elif len(self._grid[0]) > 1:
            row = [None for _ in range(len(self._grid[0]))]
            self._grid.append(row)
        return True

    def add_column(self):
        """This method adds a column at the end of each row"""
        if len(self._grid) == 1:
            self._grid[0].append(None)
        elif len(self._grid) > 1:
            for i in range(len(self._grid)):
                self._grid[i].append(None)
        return True

    def add_data(self, data):
        """
        This method search for the first ocurance of a column in any row containing
        a None data. It then insert the data parameter into that cell.
        """
        for i, row in enumerate(self._grid):
            for j, column in enumerate(row):
                if self._grid[i][j] is None:
                    self._grid[i][j] = data
                    return True
        return False

    def set_data(self, data, *pos):
        """This method sets a data at a given position(row & column)"""
        r, c = pos
        self._grid[r][c] = data

    def delete_data(self, *pos):
        """This method deletes a data at a given position(row & column)"""
        r, c = pos
        self._grid[r][c] = None

    def get_data(self, *pos):
        """This method returns a data at a given position(row & column)"""
        r, c = pos
        return self._grid[r][c]

    def delete_row(self, pos):
        """This method deletes a row at a given position(row)"""
        del self._grid[pos]

    def delete_column(self, pos):
        """This method deletes all column at a particular position(column) from all rows"""
        for i in range(len(self._grid)):
            del self._grid[i][pos]

    def get_grid(self):
        """This returns the grid"""
        return self._grid