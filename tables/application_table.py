# Filename: application_table.py

"""
This module contains classes responsible for controlling what happens on 
the tables(grid) on the GUI. The grid found in the Application of functions/constants
All the events and errors that occurs on that grid are managed by this module.
"""

from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class LocationException(Exception):
    """This exception is raised when a drop action is done at restricted cells"""
    pass


class Table(QTableWidget):
    """
    This class simply inherits from QTableWidget class and defines its event functions
    """
    def __init__(self, parent=None):
        """
        This simply set some attributes 
        """
        super(Table, self).__init__(parent)
        self.text_into = ''
        self.text_from = ''
        # used to store two important rows used in setting our outputs in result tables
        self.list = []
        self.msg = QMessageBox()
        self.double_cliked_item = []

    def dragEnterEvent(self, e):
        """
        Handles when a dragEnterEvent occurs and prevent a drop event from
        being performed at certain cells 
        """
        if self.currentColumn() == 0:
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, event):
        """
        Gets the two items that are involved in the drop i.e. the item being draged
        and the item being droped on.
        It also append two import rows in a list to be used by module main's OpExpGen class
        """
        row1 = self.currentRow()
        column1 = self.currentColumn()
        index = self.indexAt(event.pos())
        row2, column2 = index.row(), index.column()
        self.text_from = self.item(row1, column1)
        self.text_into = self.item(row2, column2)

        # Add these to rows to be used by our MainWindow to set the outputs in that location
        self.list.append((row1, column1))
        self.list.append((row2, column2))

        # This raise an exception if a drop is done on the first column or on a row
        # other than the first row
        if ((column2 == 0) and (self.text_into is not None)) or (row2>0):
            raise LocationException
        print(self.list)

    def cellDoubleClicked(self, row: int, column: int):
        """This saves the a cell's row and column that has been double clicked. 
        It saves it in the double_cliked_item's attribute"""
        if row <= 0 or column <= 0:
            pass
        else:
            self.double_cliked_item.clear()
            self.double_cliked_item.append(row)
            self.double_cliked_item.append(column)


    def mouseDoubleClickEvent(self, e: QtGui.QMouseEvent):
        loc = self.indexAt(e.pos())
        self.cellDoubleClicked(loc.row(), loc.column())

    def contextMenuEvent(self, event):
        # create context menu
        self.popMenu = QMenu(self)
        a = QAction('Select function', self)
        arg_menu = self.popMenu.addMenu('Select arg')
        b = QAction('1', self)
        c = QAction('2', self)
        self.addActions(arg_menu, (b, c))
        self.popMenu.addSeparator()
        d = QAction('Delete', self)
        self.addActions(self.popMenu, (a, d))
        a.triggered.connect(lambda: self.perform_action(event))
        self.popMenu.popup(QtGui.QCursor.pos())

    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)

    def perform_action(self, event):
        # get the selected row and column
        row = self.currentRow()
        col = self.currentColumn()
        # get the selected cell
        cell = self.item(row, col)
        # get the text inside selected cell (if any)
        cellText = cell.text()
        print("Function: ", cellText)
