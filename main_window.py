from ui_files.ui_window import Ui_MainWindow
from tables.application_table import Table, LocationException
from tables.intermediate_table import InterTable
from PyQt5 import QtWidgets


class OPMainWindow(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.button_group = QtWidgets.QButtonGroup()
        self.button_group.addButton(self.radioButton_add)
        self.button_group.addButton(self.radioButton_substract)
        self.button_group.addButton(self.radioButton_multiply)
        self.button_group.addButton(self.radioButton_divide)
        self.button_group.addButton(self.radioButton_comp)
        self.button_group.addButton(self.radioButton_subs)
        self.button_group.addButton(self.radioButton_cos)
        self.button_group.addButton(self.radioButton_sin)
        self.button_group.addButton(self.radioButton_tan)
        self.button_group.addButton(self.radioButton_pow)

        # TODO: Create a class that takes the Two table objects and add events to them directly without copying the
        # properties as done below
        geometry = self.tableWidget_func.geometry(), self.tableWidget_inter.geometry()
        frame_shape = self.tableWidget_func.frameShape(), self.tableWidget_inter.frameShape()
        edit_triggers = self.tableWidget_func.editTriggers(), self.tableWidget_inter.editTriggers()
        drag_enabled = self.tableWidget_func.dragEnabled(), self.tableWidget_inter.dragEnabled()
        drag_drop_mode = self.tableWidget_func.dragDropMode(), self.tableWidget_inter.dragDropMode()
        altenating_row_colors = self.tableWidget_func.alternatingRowColors(), self.tableWidget_inter.alternatingRowColors()
        corner_button_enabled = self.tableWidget_func.isCornerButtonEnabled(), self.tableWidget_inter.isCornerButtonEnabled()
        row_count = self.tableWidget_func.rowCount(), self.tableWidget_inter.rowCount()
        column_count = self.tableWidget_func.columnCount(), self.tableWidget_inter.columnCount()
        object_name = self.tableWidget_func.objectName(), self.tableWidget_inter.objectName()

        # Create a new Table object and overide our existing table
        # Set its properties with those copied above
        self.tableWidget_func = Table(self.groupBox_appfunc)
        self.tableWidget_func.setGeometry(geometry[0])
        self.tableWidget_func.setFrameShape(frame_shape[0])
        self.tableWidget_func.setEditTriggers(edit_triggers[0])
        self.tableWidget_func.setDragEnabled(drag_enabled[0])
        self.tableWidget_func.setDragDropMode(drag_drop_mode[0])
        self.tableWidget_func.setAlternatingRowColors(altenating_row_colors[0])
        self.tableWidget_func.setCornerButtonEnabled(corner_button_enabled[0])
        self.tableWidget_func.setRowCount(row_count[0])
        self.tableWidget_func.setColumnCount(column_count[0])
        self.tableWidget_func.setObjectName(object_name[0])

        self.tableWidget_inter = InterTable(self.groupBox_interResult)
        self.tableWidget_inter.setGeometry(geometry[1])
        self.tableWidget_inter.setFrameShape(frame_shape[1])
        self.tableWidget_inter.setEditTriggers(edit_triggers[1])
        self.tableWidget_inter.setDragEnabled(drag_enabled[1])
        self.tableWidget_inter.setDragDropMode(drag_drop_mode[1])
        self.tableWidget_inter.setAlternatingRowColors(altenating_row_colors[1])
        self.tableWidget_inter.setCornerButtonEnabled(corner_button_enabled[1])
        self.tableWidget_inter.setRowCount(row_count[1])
        self.tableWidget_inter.setColumnCount(column_count[1])
        self.tableWidget_inter.setObjectName(object_name[1])

    def retranslateUi(self, MainWindow):
        super().retranslateUi(MainWindow)

