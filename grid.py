# File name: grid.py
# This contains our application of functions Grid data structure

"""
This module is responsible for the main grid on the GUI/Text app.
It controls the grid responsible for applications of functions and generation of expressions.
It contains classes that have methods for saving and loading our grid from a special file format.
"""
import pickle
import gzip
from PyQt5.QtCore import *


class Grid:
    """
    This represents a grid which contains functions their application outputs at their intersections.
    It provides methods for manipulating the grid.
    It also provide methods for saving and retrieving the grid from a file using the Pickle object.
    """
    def __init__(self):
        """
        This is a constructor that initializes our class Grid and set it's default attributes.
        """
        self._filename = ''    # This contains the name of the file name in which the grid would be stored
        self._grid = [['->']]  # This holds elements in our grid
        self._dirty = False    # This flags indicates whether there're any unsaved changes
        self._funNames = []    # This holds all the names of the functions in the grid

    def clear(self, clearFileName=True):
        """
        This resets the grid to its default settings 
        """
        self._grid = [['->']]
        self._funNames.clear()
        if clearFileName:
            self._filename = ""

    def isDirty(self):
        """
        This returns the dirty flag which is either true or false.
        """
        return self._dirty

    def setDirty(self, dirty=True):
        """
        This class sets the dirty flag
        """
        self._dirty = dirty

    def add_row(self, func):
        """
        This method adds a row to our grid along with a function at the zeroth position.
        It also validates if the function already exist in the grid
        """
        if func in self._funNames:
            return False
        else:
            if len(self._grid[0]) == 1:
                self._grid.extend([[func]])
            elif len(self._grid[0]) > 1:
                row = [[] for _ in range(len(self._grid[0])-1)]
                row.insert(0, func)
                self._grid.extend([row])
            self._funNames.append(func)
            self._dirty = True
            return True

    def add_column(self, func):
        """
        This method adds a column to the grid with the function set at the column in the first row added.
        It also validates if the function already exist
        """
        if func in self._funNames:
            return False
        else:
            if len(self._grid) == 1:
                self._grid[0].append(func)
                self._funNames.append(func)
            elif len(self._grid) > 1:
                self._grid[0].append(func)
                self._funNames.append(func)
                for i in range(1, len(self._grid)):
                    self._grid[i].append([])
            self._dirty = True
            return True

    def add_item(self, item, *pos):
        """
        This adds an item at a given position in the grid
        """
        r, c = pos
        if (r == 0) or (c == 0):
            return False
        else:
            self._grid[r][c].append(item)
        self._dirty = True
        return True

    def get_item(self, *pos):
        """This method returns a data at a given position(row & column)"""
        r, c = pos
        return self._grid[r][c]

    def clear_item_contents(self, *pos):
        """
            This clears an item found at a given position 
        """
        try:
            r, c = pos
            if (r == 0) or (c == 0):
                return False
            else:
                self._grid[r][c].clear()
            self._dirty = True
            return True
        except IndexError:
            return False

    def delete_item(self, *pos):
        """
        This deletes an item found at a given position 
        """
        try:
            r, c = pos
            if (r == 0) or (c == 0):
                return False
            else:
                del self._grid[r][c]
            self._dirty = True
            return True
        except IndexError:
            return False

    def delete_row(self, pos=None):
        """
        This deletes a row from the grid and also deletes the function found at that row
        from the list of function names attribute
        """
        try:
            if pos is None:
                self._funNames.remove(self._grid.pop()[0])
            else:
                self._funNames.remove(self._grid[pos][0])
                del self._grid[pos]
            self._dirty = True
            return True
        except (IndexError, ValueError):
            return False

    def delete_column(self, pos=None):
        """
        This deletes a column from the grid and also deletes the function found at that column
        from the list of function names attribute 
        """
        try:
            if pos is None:
                for i in range(len(self._grid)):
                    if i == 0:
                        self._funNames.remove(self._grid[i].pop())
                    else:
                        self._grid[i].pop()
            else:
                for i in range(len(self._grid)):
                    self._funNames.remove(self._grid[i][pos])
                    del self._grid[i][pos]
            self._dirty = True
            return True
        except (IndexError, ValueError):
            return False

    def get_grid(self):
        """This returns our raw grid"""
        return self._grid

    def display_grid(self):
        """This displays the grid in a more understandable maner i.e. row by row"""
        for i in self._grid:
            print(i)

    def __len__(self):
        """This returns the length of our grid. i.e how many rows"""
        return len(self._grid)

    def setFilename(self, filename):
        """This sets the file name"""
        self._filename = filename

    def filename(self):
        """This returns the file name"""
        return self._filename

    @staticmethod
    def formats():
        """This contains the available formats of the file name"""
        return "*.mpb"

    def save(self, filename=""):
        """
        This saves the grid into a file with a given file name.
        It does so by calling the class savePickel method
        """
        if filename:
            self._filename = filename
        if self._filename.endswith(".mpb"):
            return self.savePickle()
        return False, "Failed to save: invalid file extension"

    def load(self, filename=""):
        """This loads the grid from the file by calling the loadPickle method"""
        if filename:
            self._filename = filename
        if self._filename.endswith(".mpb"):
            return self.loadPickle()
        return False, "Failed to load: invalid file extension"

    def savePickle(self):
        """This method does the actual saving of the grid into a file"""
        error = None
        fh = None
        try:
            fh = gzip.open(self._filename, "wb")
            pickle.dump(self._grid, fh, 2)
        except EnvironmentError as e:
            error = "Failed to save: {}".format(e)
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                return False, error
            self._dirty = False
            return True, "Saved {} grid records to {}".format(
                len(self._grid),
                QFileInfo(self._filename).fileName())

    def loadPickle(self):
        """This does the actual loading of the grid from a file"""
        error = None
        fh = None
        try:
            fh = gzip.open(self._filename, "rb")
            self.clear(False)
            self._grid = pickle.load(fh)

            # This saves the Horizontal functions in the funName attribute
            for value in self._grid[0]:
                if value == '->':
                    pass
                else:
                    self._funNames.append(value)

            # This saves the Vertical functions in the funName attribute
            for row in self._grid:
                if row[0] == '->':
                    pass
                else:
                    self._funNames.append(row[0])
        except EnvironmentError as e:
            error = "Failed to load: {}".format(e)
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                return False, error
            self._dirty = False
            return True, "Loaded {} grid records from {}".format(
                len(self._grid),
                QFileInfo(self._filename).fileName())
