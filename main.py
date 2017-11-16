# File name: main.py
"""
This module contains classes responsible for our GUI.
It uses other modules in order to run our GUI.
It is the main module of the GUI project.
It contains the DragAt dialog class for our pop-up dialog when a drag is
performed.
It contains OpExGen Main Window class for controlling, managing and running
the GUI. 
It gives users a high degree of control and manipulation and abstracting the backend
functions from users.
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from operators import *
import ui_create_func_dialog
import ui_2D_view
from create_func import CreateFunc
import grid
import intermediate
import window
import ui_dragAt
import ui_export_expression
import expression_tree
# import browser

__author__ = 'Molinge'


class DragAt(QDialog):
    """
    This class inherit from QDialog and creates a dialog by using an object of
    class Ui_Dialog from module ui_dragAt
    """
    def __init__(self, parent=None, text_from='', text_into=''):
        """
        Constructor initializes the Dialog using the setupUi method from Ui_Dialog
        class found in ui_dragAt module.
        """
        super(DragAt, self).__init__(parent)
        self.ui = ui_dragAt.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setText(text_from)
        self.ui.lineEdit.setText(text_into)
        self.ui.lineEdit_3.setValidator(QIntValidator())  # restrict input to Integers


class TwoDView(QDialog):
    """
    This class displays a dialog containing a 2D view of the expressions generated.
    It also allows the user to delete an expression from that 2D view by deleting a row.
    The user has the ability to cancel which undo any delete action done.
    """
    def __init__(self, parent=None):
        """
        Constructor initializes the Dialog using setupUi method from Ui_Dialog_2D class
        found at the ui_2D_view module.
        """
        super(TwoDView, self).__init__(parent)
        self.ui = ui_2D_view.Ui_Dialog_2D()
        self.ui.setupUi(self)
        #self.ui.pushButton_del_row(self.del_row())


class CreateFuncDialog(QDialog):
    """
    This allows the user to create a function which updates the Creation of 
    Function palette.
    """
    def __init__(self, parent=None):
        """
        Constructor initializes the Dialog using setupUi method from ui_Dialog_create_fc
        class found at the ui_create_func_const_dialog.
        """
        super(CreateFuncDialog, self).__init__(parent)
        self.ui = ui_create_func_dialog.Ui_Dialog_create_fc()
        self.ui.setupUi(self)
        self.ui.lineEdit_2.setValidator(QIntValidator())  # restrict input to Integers
        self.ui.pushButton_clear.clicked.connect(self.default_palette)

    def default_palette(self):
        """ This sets the create function palette to its default"""
        self.ui.lineEdit.clear()
        self.ui.comboBox_1.setCurrentIndex(0)
        self.ui.lineEdit_2.clear()
        self.ui.comboBox_2.setCurrentIndex(0)


class ExportExpressionDialog(QDialog):
    """
    This dialog export an expression of user's desired format into an external
    file of his/her choice.
    """
    def __init__(self, parent=None):
        super(ExportExpressionDialog, self).__init__(parent)
        self.ui = ui_export_expression.Ui_Dialog()
        self.ui.setupUi(self)
        # self.ui.pushButton_cancel.clicked.connect()


class OpExpGen(QMainWindow):
    """"
    This class inherit from QMainWindow and instantiates the Main Window of
    our GUI by creating an object of class Ui_MainWindow from ui_operator_expression_gen_update
    file and calling its setupUi file to create the GUI.
    This class also provides functions used to manipulate the GUI's contents.
    """

    def __init__(self, parent=None):
        """ This constructor instantiate the GUI and call other functions in action
            It also defined some of our basic data structures used in the backend.
        """
        # QWidget.__init__(self, parent)
        super(OpExpGen, self).__init__(parent)
        self.ui = window.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(':/icon.png'))
        self.center()

        # This initializes our message box to be used through out the gui
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Warning)
        self.msg.setWindowTitle("Invalid Input")

        self.app_grid = grid.Grid()    # This contains our Grid data structure
        self.inter_grid = intermediate.IntermediateGrid()
        for _ in range(5):
            self.inter_grid.add_row()
            self.inter_grid.add_column()

        self.dragAt = DragAt(self)     # This represents a QDialog popup gui to be used in composition and substitution

        # This represents our pop-up dialog for creating functions/constants
        self.create_func_const_dialog = CreateFuncDialog(self)

        # This represents an object for displaying the cell's intersection in 2d
        self.view_2d_cell = TwoDView(self)

        # This represents an object for exporting expressions to a file
        self.export_exp = ExportExpressionDialog(self)

        # This defines our dictionary for storing functions and their attributes
        self.defined_functions = {}

        # They call associated functions when certain push buttons are clicked
        self.create_func_const_dialog.ui.pushButton_save.clicked.connect(self.save_func)
        self.ui.pushButton_delete_row.clicked.connect(self.remove_row)
        self.ui.pushButton_delete_column.clicked.connect(self.remove_column)
        self.ui.pushButton_delete_cell.clicked.connect(self.clear_cell)
        self.ui.pushButton_create.clicked.connect(self.create_func_const_dialog.exec_)
        self.ui.pushButton_2d.clicked.connect(self.display_2d)
        self.ui.pushButton_del_inter_cell.clicked.connect(self.clear_inter_cell)
        self.ui.pushButton_clear_inter_cell.clicked.connect(self.clear_inter_grid)
        self.ui.pushButton_export_exp.clicked.connect(self.export_expression)
        self.ui.pushButton_meaning.clicked.connect(self.meaning)

        # They call associated functions when certain menu actions are triggered
        self.ui.action_New.triggered.connect(self.file_new)
        self.ui.action_Open.triggered.connect(self.file_open)
        self.ui.action_Save.triggered.connect(self.file_save)
        self.ui.action_SaveAs.triggered.connect(self.file_save_as)
        self.ui.action_Exit.triggered.connect(self.close)
        self.ui.actionAbout_Software.triggered.connect(self.about)
        self.ui.action_User_Manual.triggered.connect(self.manual)

        # This enables the event filter at the application function and intermediate result table
        self.ui.tableWidget_func.viewport().installEventFilter(self)
        self.ui.tableWidget_inter.viewport().installEventFilter(self)

        self.ui.radioButton_add.setChecked(True)  # sets the default check button to radio button add

        # This fragment below handles what happens to the GUI upon startup
        # like maintaining the previous state of the GUI
        settings = QSettings()
        self.restoreGeometry(settings.value("OpExpGen/Geometry", QByteArray()))
        self.restoreState(settings.value("OpExpGen/State", QByteArray()))
        QTimer.singleShot(0, self.load_initial_file)
        self.setWindowTitle("Operator and Expression Generation")

    @staticmethod
    def meaning():
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Semantics of Symbols")
        msg.setText("This allows the User to add meaning to Symbols like \nfunction."
                    "\n\nThis Feature has not yet been implemented.\n")
        msg.exec_()

    def closeEvent(self, event):
        """This function handles when a user clicks the exit button"""
        if self.ok_to_continue():
            settings = QSettings()
            settings.setValue("LastFile", self.app_grid.filename())
            settings.setValue("OpExpGen/Geometry", self.saveGeometry())
            settings.setValue("OpExpGen/State", self.saveState())
        else:
            event.ignore()
    
    def eventFilter(self, source, event):
        """
        This handles when an event is being executed and then calls a function that process or
        handle the operation [outcome]. Some events like drop and mouse events are filtered and handled.
        """
        try:
            # handles drop event for tableWidget_fun i.e. application palette's grid
            if (event.type() == QtCore.QEvent.Drop) and \
                    (source is self.ui.tableWidget_func.viewport()):
                self.ui.tableWidget_func.dropEvent(event)
                self.calculate(self.ui.tableWidget_func, self.ui.tableWidget_func.list[0],
                               self.ui.tableWidget_func.list[1])
                self.ui.tableWidget_func.list.clear()
                if event.isAccepted():
                    print('eventFilter')
                return True
            # handles drop event for tableWidget_inter i.e. intermediate palette's grid
            elif (event.type() == QtCore.QEvent.Drop) and \
                 (source is self.ui.tableWidget_inter.viewport()):
                self.ui.tableWidget_inter.list.clear()
                self.ui.tableWidget_inter.dropEvent(event)

                if self.inter_grid.get_data(self.ui.tableWidget_inter.list[1][0],
                                            self.ui.tableWidget_inter.list[1][1]) is not None:
                    self.calculate(self.ui.tableWidget_inter, self.ui.tableWidget_inter.list[0],
                                   self.ui.tableWidget_inter.list[1])
                else:
                    self.inter_grid.set_data(self.ui.tableWidget_inter.text_from.text(),
                                             self.ui.tableWidget_inter.list[1][0],
                                             self.ui.tableWidget_inter.list[1][1])
                    self.update_inter_table()
                self.ui.tableWidget_inter.list.clear()
                return True

            # handles double click event on tableWidget_fun i.e. application palette's grid
            elif (event.type() == QMouseEvent.MouseButtonDblClick) and \
                    (source is self.ui.tableWidget_func.viewport()):
                self.ui.tableWidget_func.mouseDoubleClickEvent(event)
                r = self.ui.tableWidget_func.double_cliked_item[0]
                c = self.ui.tableWidget_func.double_cliked_item[1]
                print(self.app_grid.get_item(r, c))

            return QMainWindow.eventFilter(self, source, event)

        # This handles when a drop action is performed inside the grid area but
        # outside of any function i.e. areas where functions hasn't been defined yet
        except AttributeError:
            self.msg.setText("You can only drop in another function")
            self.msg.exec_()
            return True

        # This handles when a drop action is performed on a intersection layer of outputs
        # on the grid
        except window.LocationException:
            self.msg.setText("Cannot drop there")
            self.msg.exec_()
            return True

    def display_2d(self):
        """This displays the cells[containing expressions] in 2d format"""
        r = self.ui.tableWidget_func.currentRow()
        c = self.ui.tableWidget_func.currentColumn()
        if r == 0 or c == 0:
            return False
        elif (r == -1) and (c == -1):
            return False

        self.view_2d_cell.ui.tableWidget.clear()
        self.view_2d_cell.ui.tableWidget.setRowCount(len(self.app_grid.get_item(r, c)))
        self.view_2d_cell.ui.tableWidget.setColumnCount(1)
        self.view_2d_cell.show()
        for row_num, data in enumerate(self.app_grid.get_item(r, c)):
            item = QTableWidgetItem(data)
            self.view_2d_cell.ui.tableWidget.setItem(row_num, 0, item)

    def export_expression(self):
        try:
            r = self.ui.tableWidget_inter.currentRow()
            c = self.ui.tableWidget_inter.currentColumn()
            if (r == -1) and (c == -1):
                return False
            exp = self.inter_grid.get_data(r, c)
            if self.export_exp.exec_():
                my_file = self.export_exp.ui.lineEdit.text()
                print(my_file)
                file = open(my_file, "w")
                if self.export_exp.ui.comboBox.currentIndex() == 0:
                    file.write(expression_tree.expression_formats(exp, 'inorder'))
                elif self.export_exp.ui.comboBox.currentIndex() == 1:
                    file.write(expression_tree.expression_formats(exp, 'preorder'))
                elif self.export_exp.ui.comboBox.currentIndex() == 2:
                    file.write(expression_tree.expression_formats(exp, 'postorder'))
                file.close()
        except IOError as e:
            print("File name doesn't exist")

    def calculate(self, table, text_from_pos, text_into_pos):
        """This function does the calculation and test which operation has been chosen [i.e. 
        when radio button has been checked] before carryout the evaluation.
        It also stores the expression in the dictionary of artifacts.
        """

        arithmetic = Arithmetic()
        algebraic = Algebraic()
        trigonometric = Trigonometric()         # <--------- Not yet used ---------

        text_from = table.text_from.text()
        text_into = table.text_into.text()

        item = None
        # This checks the button clicked and generates the expression
        if self.ui.radioButton_add.isChecked():
            item = arithmetic.add(text_from, text_into)
        elif self.ui.radioButton_substract.isChecked():
            item = arithmetic.substract(text_from, text_into)
        elif self.ui.radioButton_multiply.isChecked():
            item = arithmetic.multiply(text_from, text_into)
        elif self.ui.radioButton_divide.isChecked():
            item = arithmetic.divide(text_from, text_into)
        elif self.ui.radioButton_pow.isChecked():
            item = arithmetic.pow(text_from, text_into)
        elif self.ui.radioButton_subs.isChecked():
            # This pop-up another dialog and checks which checkbox has been checked
            # It first sets the text in the dialog i.e. the two functions
            self.dragAt.ui.lineEdit_2.setText(text_from)
            self.dragAt.ui.lineEdit.setText(text_into)
            if self.dragAt.exec_():
                if text_into.find('y1') == -1:
                    item = None
                    self.msg.setText("Cannot do substitution with constant")
                    self.msg.exec_()
                elif text_into.find(self.dragAt.ui.lineEdit_3.text()) == -1:
                    item = None
                    self.msg.setText("Argument {} doesn't exist".format(self.dragAt.ui.lineEdit_3.text()))
                    self.msg.exec_()
                else:
                    item = algebraic.substitute(text_from, text_into, int(self.dragAt.ui.lineEdit_3.text()))

        elif self.ui.radioButton_comp.isChecked():
            self.dragAt.ui.lineEdit_2.setText(text_from)
            self.dragAt.ui.lineEdit.setText(text_into)
            if self.dragAt.exec_():
                if self.dragAt.ui.lineEdit_3.text() == '0':
                    item = algebraic.compose(text_from, text_into)
                    if item is None:
                        self.msg.setText("Cannot use constant to compose")
                        self.msg.exec_()
                        # item = algebraic.compose(text_from, text_into)
                else:
                    item = algebraic.compose(text_from, text_into, self.dragAt.ui.lineEdit_3.text())
                    if item is None:
                        self.msg.setText("Cannot use a constant to compose")
                        self.msg.exec_()
                    elif item is False:
                        item = None
                        self.msg.setText("Argument doesn't exit")

        if item is None:
            return False
        if table is self.ui.tableWidget_func:
            # This does the storing of the expression in the output table
            self.app_grid.add_item(item, text_from_pos[0], text_into_pos[1])
            self.update_table()
            self.inter_grid.add_data(item)
            self.update_inter_table()
        elif table is self.ui.tableWidget_inter:
            # This does the storing of the expression in the intermediate table
            self.inter_grid.set_data(item, text_into_pos[0], text_into_pos[1])
            self.update_inter_table()

    def save_func(self):
        """ 
            This function is called when the pushButton_save is clicked.
            It does some testing ensuring that all the fields in the save pallet
            are filled and in it's right combination.
            It then updates the output table and the available function table
        """

        # This code snipes does the testing and assertions
        if self.create_func_const_dialog.ui.lineEdit.text() == '':
            self.msg.setText("function name cannot be left empty")
            self.msg.exec_()
        if (not self.create_func_const_dialog.ui.lineEdit.text().isalnum()) or \
           (self.create_func_const_dialog.ui.lineEdit.text()[0].isnumeric()):
            self.msg.setText("Function name is invalid")
            self.msg.exec_()
        elif self.create_func_const_dialog.ui.comboBox_1.currentText() == 'Constant' and \
                (int(self.create_func_const_dialog.ui.lineEdit_2.text()) > 0):
            self.msg.setText("A Constant cannot have an argument")
            self.msg.exec_()
        elif int(self.create_func_const_dialog.ui.lineEdit_2.text()) < 0:
            self.msg.setText("A Function cannot have a negative argument")
            self.msg.exec_()

        else:
            # This code segment collects info from the create function palette
            func_name = self.create_func_const_dialog.ui.lineEdit.text()
            func_type = self.create_func_const_dialog.ui.comboBox_1.currentText()
            num_args = int(self.create_func_const_dialog.ui.lineEdit_2.text())
            section = self.create_func_const_dialog.ui.comboBox_2.currentText()

            # Here we create an object of CreateFunc class and set it's
            # values to those collected in the above segment.
            func = CreateFunc()
            func.set_name(func_name)
            func.set_type(func_type)
            func.set_args(num_args)
            func.set_section(section)
            func.create_function()

            # This code snipe uses a temporal dictionary to check if the function to be created
            # has the same name and exact number of attributes exist and prevent it from being
            # created

            temp_dict = dict()
            temp_dict[func_name] = [func_type, num_args, section]

            # checks if function exist already
            if func_name in self.defined_functions:
                if temp_dict[func_name][1] == self.defined_functions[func_name][1]:
                    self.msg.setText("Function already exist")
                    self.msg.exec_()
                    return

            self.defined_functions[func_name] = [func_type, num_args, section]  # update dictionary

            # This code snipe saves the function name in the application of functions/constant table and appends
            # its number of argument in a string form to let the user know the amount of arguments
            # It checks and ensures each function or constant is saved in their respective row or column
            if self.defined_functions[func_name][2] == 'Vertical':
                self.app_grid.add_row(func.get_function())
            elif self.defined_functions[func_name][2] == 'Horizontal':
                self.app_grid.add_column(func.get_function())
            self.update_table()

    def remove_row(self):
        """
        This function checks the current activated row and deletes it.
        It prevents the first row from being deleted
        """
        r = self.ui.tableWidget_func.currentRow()
        if r == 0:
            pass
        elif r == -1:
            return False
        else:
            self.app_grid.delete_row(r)
        self.update_table()

    def remove_column(self):
        """
        This function checks the current activated column and deletes it.
        It prevents the first column from being deleted
        """
        c = self.ui.tableWidget_func.currentColumn()
        if c == 0:
            pass
        elif c == -1:
            return False
        else:
            self.app_grid.delete_column(c)
        self.update_table()

    def clear_cell(self):
        """This handles the delete of cell contents in the application of functions grid"""
        r = self.ui.tableWidget_func.currentRow()
        c = self.ui.tableWidget_func.currentColumn()
        if r == 0 or c == 0:
            pass
        elif (r == -1) and (c == -1):
            return False
        else:
            self.app_grid.clear_item_contents(r, c)
        self.update_table()

    def clear_inter_cell(self):
        """This handles the delete of cell contents in the intermediate result grid"""
        r = self.ui.tableWidget_inter.currentRow()
        c = self.ui.tableWidget_inter.currentColumn()
        self.inter_grid.delete_data(r, c)
        self.update_inter_table()

    def clear_inter_grid(self):
        """
        This clears all contents in intermediate grid
        """
        self.inter_grid.clear()
        for _ in range(5):      # add rows and columns to grid
            self.inter_grid.add_row()
            self.inter_grid.add_column()
        self.update_inter_table()

    def ok_to_continue(self):
        """ Prompt the user with a dialog during exist"""
        if self.app_grid.isDirty():
            reply = QMessageBox.question(self,
                                         "Unsaved Changes",
                                         "Do you want to save?",
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Yes:
                return self.file_save()
        return True

    def load_initial_file(self):
        """
        This function is responsible for loading our previous settings and files that
        where lastly opened files reloaded into our grid.
        """
        settings = QSettings()
        filename = settings.value("LastFile")
        if filename and QFile.exists(filename):
            ok, msg = self.app_grid.load(filename)
            self.statusBar().showMessage(msg, 5000)
        self.update_table()

    def center(self):
        """This function centralises the widget"""
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

    def about(self):
        """This function displays a message box containing info about the software."""
        QMessageBox.about(self.msg, "Operator and Expression Generator",
                          "Software Version: 1.0\n\n"
                          "Author: Molinge Lyonga Jr\n\n"
                          "Description: This is a simple application of functions.\n"
                          "It generates Operators and Expressions.\n"
                          "It was built using python3.5, PyQt5 binding, and \nQt5 designer.\n\n"
                          "It is built for academic, personal and commercial \nusages.")

    @staticmethod
    def manual():
        """This is to display the user manual in the browser module"""
        pass

    def update_table(self):
        """
        This function updates our grid each time changes are being made.
        It does so by loading the updated contents of our internal grid [class Grid's object]
        into the grid represented on the GUI.
        """

        # This code segment clear our GUI grid and set its row and column count to that
        # of our class Grid's object.
        self.ui.tableWidget_func.clear()
        self.ui.tableWidget_func.setRowCount(len(self.app_grid))
        self.ui.tableWidget_func.setColumnCount(len(self.app_grid.get_grid()[0]))

        # This code segment iterates through our Grid object and load each of its content
        # into the grid on our GUI
        for row_num, row in enumerate(self.app_grid.get_grid()):
            for column_num, data in enumerate(row):
                if data == '->':
                    item = QTableWidgetItem()
                    icon = QIcon()
                    icon.addPixmap(QPixmap(":/arrow.svg"), QIcon.Normal, QIcon.On)
                    item.setIcon(icon)
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    self.ui.tableWidget_func.setItem(0, 0, item)
                else:
                    if type(data) is list and (len(data) == 0):
                        item = QTableWidgetItem(None)
                    elif type(data) is list and (len(data) > 0):
                        item = QTableWidgetItem(data[0])
                    else:
                        item = QTableWidgetItem(data)
                    self.ui.tableWidget_func.setItem(row_num, column_num, item)
        # This sets the main windows title and appending the name of the file containing the
        # Grid object
        self.setWindowTitle("Operator and Expression Generator {}".format(self.app_grid.filename()))
        self.app_grid.display_grid()    # This displays our grid on the terminal
        print()

    def update_inter_table(self):
        """This function is responsible for updating our intermediate result grid"""
        self.ui.tableWidget_inter.clear()
        self.ui.tableWidget_inter.setRowCount(len(self.inter_grid))
        self.ui.tableWidget_inter.setColumnCount(len(self.inter_grid.get_grid()[0]))
        for row_num, row in enumerate(self.inter_grid.get_grid()):
            for column_num, data in enumerate(row):
                item = QTableWidgetItem(data)
                self.ui.tableWidget_inter.setItem(row_num, column_num, item)
        print(self.inter_grid.get_grid(), '\n')

    def file_new(self):
        """This updates clears the contents of our Grid object and calls the corresponding
        update functions of our GUI grids to clear their contents"""
        if not self.ok_to_continue():
            return
        self.app_grid.clear()  # clears grid to default
        self.inter_grid.clear()  # clears grid to default
        for _ in range(5):      # add rows and columns to grid
            self.inter_grid.add_row()
            self.inter_grid.add_column()
        self.statusBar().clearMessage()
        self.update_table()
        self.update_inter_table()

    def file_open(self):
        """
        This function is responsible for opening a grid file and loading it's contents
        into our GUI grid. It displays a file dialog allowing the user to chose his/her file
        which is then loaded into our Grid object and the GUI grid as well.
        """
        if not self.ok_to_continue():
            return
        path = (QFileInfo(self.app_grid.filename()).path()
                if self.app_grid.filename() else ".")
        filename = QFileDialog.getOpenFileName(self, "My Grid - Load Grid Data", path,
                                               "My Grid data files ({})".format(self.app_grid.formats()))
        if filename:
            ok, msg = self.app_grid.load(filename[0])
            self.statusBar().showMessage(msg, 5000)
            self.update_table()

    def file_save(self):
        """
        This function saves the contents of our Grid object into a file.
        If the file doesn't exist yet it calls the fileSaveAs function to save the new file
        else if it exist already, it just overwrite its contents
        """
        if not self.app_grid.filename():
            return self.file_save_as()
        else:
            ok, msg = self.app_grid.save()
            self.statusBar().showMessage(msg, 5000)
            return ok

    def file_save_as(self):
        """
        This function saves the Grid object into a file name given by the user. The file
        format is .mpb
        """
        filename = (self.app_grid.filename() if self.app_grid.filename() else ".")
        filename = QFileDialog.getSaveFileName(self, "My Grid - Save Grid Data", filename,
                                               "My Grid data files ({})".format(self.app_grid.formats()))
        if filename:
            if '.' not in filename[0]:
                filename = filename[0] + ".mpb", filename[1]
            ok, msg = self.app_grid.save(filename[0])
            self.statusBar().showMessage(msg, 5000)
            return ok
        return False


# This code snipes is ran when the user runs the code.
# It instantiate our Application and make our Main Window visible
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = OpExpGen()
    form.show()
    sys.exit(app.exec_())
