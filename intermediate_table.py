# File name: intermediate_table.py

from PyQt5.QtWidgets import *

__author__ = 'Molinge'


class InterTable(QTableWidget):
    """
    This class simply inherits from QTableWidget class and defines its event functions
    """
    def __init__(self, parent=None):
        """
        This simply set some attributes 
        """
        super(InterTable, self).__init__(parent)
        self.text_into = ''
        self.text_from = ''
        # used to store two important rows used in setting our outputs in result table
        self.list = []
        self.msg = QMessageBox()

    def dropEvent(self, event):
        """
        Gets the two items that are involved in the drop i.e. the item being dragged
        and the item being dropped on.
        It also append two import rows in a list to be used by module main's OpExpGen class 
        """
        sender = event.source()
        row1, column1 = (sender.currentRow(), sender.currentColumn())  # where the drag came from

        # position where the drop occurred
        index = self.indexAt(event.pos())
        row2, column2 = index.row(), index.column()

        self.text_from = sender.item(row1, column1)
        self.text_into = self.item(row2, column2)

        '''
        if str(sender.__class__) == "<class 'application_table.Table'>":
            if self.text_into is None:
                self.setItem(row2, column2, QTableWidgetItem(self.text_from))
        elif str(sender.__class__) == "<class 'intermediate_table.InterTable'>":
            pass
        '''

        # Add these to rows to be used by our MainWindow to set the outputs in that location
        self.list.append((row1, column1))
        self.list.append((row2, column2))
        print(self.list)