# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 615)
        MainWindow.setMinimumSize(QtCore.QSize(805, 610))
        MainWindow.setToolTipDuration(2)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_operators = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_operators.setGeometry(QtCore.QRect(10, 30, 171, 321))
        self.groupBox_operators.setFocusPolicy(QtCore.Qt.TabFocus)
        self.groupBox_operators.setObjectName("groupBox_operators")
        self.tabWidget_operators = QtWidgets.QTabWidget(self.groupBox_operators)
        self.tabWidget_operators.setGeometry(QtCore.QRect(10, 20, 151, 291))
        self.tabWidget_operators.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.tabWidget_operators.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_operators.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget_operators.setObjectName("tabWidget_operators")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.radioButton_add = QtWidgets.QRadioButton(self.tab)
        self.radioButton_add.setGeometry(QtCore.QRect(10, 20, 71, 19))
        self.radioButton_add.setObjectName("radioButton_add")
        self.radioButton_substract = QtWidgets.QRadioButton(self.tab)
        self.radioButton_substract.setGeometry(QtCore.QRect(10, 50, 101, 20))
        self.radioButton_substract.setObjectName("radioButton_substract")
        self.radioButton_multiply = QtWidgets.QRadioButton(self.tab)
        self.radioButton_multiply.setGeometry(QtCore.QRect(10, 80, 91, 19))
        self.radioButton_multiply.setObjectName("radioButton_multiply")
        self.radioButton_divide = QtWidgets.QRadioButton(self.tab)
        self.radioButton_divide.setGeometry(QtCore.QRect(10, 110, 81, 19))
        self.radioButton_divide.setObjectName("radioButton_divide")
        self.radioButton_pow = QtWidgets.QRadioButton(self.tab)
        self.radioButton_pow.setGeometry(QtCore.QRect(10, 140, 111, 19))
        self.radioButton_pow.setObjectName("radioButton_pow")
        self.tabWidget_operators.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.radioButton_comp = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_comp.setGeometry(QtCore.QRect(0, 20, 121, 19))
        self.radioButton_comp.setObjectName("radioButton_comp")
        self.radioButton_subs = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_subs.setGeometry(QtCore.QRect(0, 60, 100, 19))
        self.radioButton_subs.setObjectName("radioButton_subs")
        self.tabWidget_operators.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.radioButton_cos = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_cos.setGeometry(QtCore.QRect(10, 20, 51, 19))
        self.radioButton_cos.setObjectName("radioButton_cos")
        self.radioButton_sin = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_sin.setGeometry(QtCore.QRect(10, 60, 51, 19))
        self.radioButton_sin.setObjectName("radioButton_sin")
        self.radioButton_tan = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_tan.setGeometry(QtCore.QRect(10, 88, 51, 31))
        self.radioButton_tan.setObjectName("radioButton_tan")
        self.tabWidget_operators.addTab(self.tab_3, "")
        self.groupBox_appfunc = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_appfunc.setGeometry(QtCore.QRect(190, 30, 611, 321))
        self.groupBox_appfunc.setObjectName("groupBox_appfunc")
        self.tableWidget_func = QtWidgets.QTableWidget(self.groupBox_appfunc)
        self.tableWidget_func.setGeometry(QtCore.QRect(10, 20, 471, 291))
        self.tableWidget_func.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget_func.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_func.setDragEnabled(True)
        self.tableWidget_func.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget_func.setAlternatingRowColors(True)
        self.tableWidget_func.setCornerButtonEnabled(True)
        self.tableWidget_func.setRowCount(4)
        self.tableWidget_func.setColumnCount(4)
        self.tableWidget_func.setObjectName("tableWidget_func")
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/arrow.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item.setIcon(icon)
        item.setFlags(QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.tableWidget_func.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_func.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_func.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_func.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_func.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_func.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_func.setItem(3, 0, item)
        self.tableWidget_func.horizontalHeader().setDefaultSectionSize(104)
        self.tableWidget_func.horizontalHeader().setMinimumSectionSize(24)
        self.pushButton_delete_row = QtWidgets.QPushButton(self.groupBox_appfunc)
        self.pushButton_delete_row.setGeometry(QtCore.QRect(490, 60, 111, 31))
        self.pushButton_delete_row.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_delete_row.setObjectName("pushButton_delete_row")
        self.pushButton_delete_column = QtWidgets.QPushButton(self.groupBox_appfunc)
        self.pushButton_delete_column.setGeometry(QtCore.QRect(490, 100, 111, 31))
        self.pushButton_delete_column.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.pushButton_delete_column.setObjectName("pushButton_delete_column")
        self.pushButton_delete_cell = QtWidgets.QPushButton(self.groupBox_appfunc)
        self.pushButton_delete_cell.setGeometry(QtCore.QRect(490, 140, 111, 31))
        self.pushButton_delete_cell.setObjectName("pushButton_delete_cell")
        self.pushButton_create = QtWidgets.QPushButton(self.groupBox_appfunc)
        self.pushButton_create.setGeometry(QtCore.QRect(490, 180, 111, 31))
        self.pushButton_create.setObjectName("pushButton_create")
        self.pushButton_2d = QtWidgets.QPushButton(self.groupBox_appfunc)
        self.pushButton_2d.setGeometry(QtCore.QRect(490, 20, 111, 31))
        self.pushButton_2d.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.pushButton_2d.setToolTipDuration(-1)
        self.pushButton_2d.setStatusTip("")
        self.pushButton_2d.setObjectName("pushButton_2d")
        self.pushButton_meaning = QtWidgets.QPushButton(self.groupBox_appfunc)
        self.pushButton_meaning.setGeometry(QtCore.QRect(490, 220, 111, 31))
        self.pushButton_meaning.setToolTipDuration(5)
        self.pushButton_meaning.setObjectName("pushButton_meaning")
        self.groupBox_interResult = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_interResult.setGeometry(QtCore.QRect(10, 350, 791, 221))
        self.groupBox_interResult.setObjectName("groupBox_interResult")
        self.tableWidget_inter = QtWidgets.QTableWidget(self.groupBox_interResult)
        self.tableWidget_inter.setGeometry(QtCore.QRect(10, 20, 641, 192))
        self.tableWidget_inter.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_inter.setDragEnabled(True)
        self.tableWidget_inter.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget_inter.setRowCount(6)
        self.tableWidget_inter.setColumnCount(6)
        self.tableWidget_inter.setObjectName("tableWidget_inter")
        self.pushButton_del_inter_cell = QtWidgets.QPushButton(self.groupBox_interResult)
        self.pushButton_del_inter_cell.setGeometry(QtCore.QRect(660, 17, 111, 31))
        self.pushButton_del_inter_cell.setObjectName("pushButton_del_inter_cell")
        self.pushButton_clear_inter_cell = QtWidgets.QPushButton(self.groupBox_interResult)
        self.pushButton_clear_inter_cell.setGeometry(QtCore.QRect(660, 57, 111, 31))
        self.pushButton_clear_inter_cell.setObjectName("pushButton_clear_inter_cell")
        self.pushButton_export_exp = QtWidgets.QPushButton(self.groupBox_interResult)
        self.pushButton_export_exp.setGeometry(QtCore.QRect(660, 100, 111, 31))
        self.pushButton_export_exp.setObjectName("pushButton_export_exp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 805, 19))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_New = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/filenew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_New.setIcon(icon1)
        self.action_New.setObjectName("action_New")
        self.action_Open = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/fileopen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon2)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/filesave.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save.setIcon(icon3)
        self.action_Save.setObjectName("action_Save")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/filequit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon4)
        self.action_Exit.setObjectName("action_Exit")
        self.actionAbout_Software = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/editzoom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout_Software.setIcon(icon5)
        self.actionAbout_Software.setObjectName("actionAbout_Software")
        self.action_SaveAs = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/filesaveas.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_SaveAs.setIcon(icon6)
        self.action_SaveAs.setObjectName("action_SaveAs")
        self.action_User_Manual = QtWidgets.QAction(MainWindow)
        self.action_User_Manual.setIcon(icon5)
        self.action_User_Manual.setObjectName("action_User_Manual")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/undo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon7)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/redo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon8)
        self.actionRedo.setObjectName("actionRedo")
        self.menuFile.addAction(self.action_New)
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addAction(self.action_SaveAs)
        self.menuFile.addAction(self.action_Exit)
        self.menuHelp.addAction(self.actionAbout_Software)
        self.menuHelp.addAction(self.action_User_Manual)
        self.menu_Edit.addAction(self.actionUndo)
        self.menu_Edit.addAction(self.actionRedo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget_operators.setCurrentIndex(0)
        self.pushButton_clear_inter_cell.clicked.connect(self.tableWidget_inter.clearContents)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>Select any result field to view it in 2D mode</p></body></html>"))
        self.groupBox_operators.setTitle(_translate("MainWindow", "Operators"))
        self.radioButton_add.setText(_translate("MainWindow", "Add ( + )"))
        self.radioButton_substract.setText(_translate("MainWindow", "substract ( - )"))
        self.radioButton_multiply.setText(_translate("MainWindow", "Multiply ( * )"))
        self.radioButton_divide.setText(_translate("MainWindow", "Divide ( / )"))
        self.radioButton_pow.setText(_translate("MainWindow", "Pow ( ** )"))
        self.tabWidget_operators.setTabText(self.tabWidget_operators.indexOf(self.tab), _translate("MainWindow", "Artihmetic"))
        self.radioButton_comp.setText(_translate("MainWindow", "Composition ( ∘ )"))
        self.radioButton_subs.setText(_translate("MainWindow", "Substitution"))
        self.tabWidget_operators.setTabText(self.tabWidget_operators.indexOf(self.tab_2), _translate("MainWindow", "Algebraic"))
        self.radioButton_cos.setText(_translate("MainWindow", "cos"))
        self.radioButton_sin.setText(_translate("MainWindow", "sin"))
        self.radioButton_tan.setText(_translate("MainWindow", "tan"))
        self.tabWidget_operators.setTabText(self.tabWidget_operators.indexOf(self.tab_3), _translate("MainWindow", "Trigonometric"))
        self.groupBox_appfunc.setTitle(_translate("MainWindow", "Application of functions"))
        __sortingEnabled = self.tableWidget_func.isSortingEnabled()
        self.tableWidget_func.setSortingEnabled(False)
        item = self.tableWidget_func.item(0, 1)
        item.setText(_translate("MainWindow", "g(y1,y2)"))
        item = self.tableWidget_func.item(0, 2)
        item.setText(_translate("MainWindow", "h(y1)"))
        item = self.tableWidget_func.item(0, 3)
        item.setText(_translate("MainWindow", "n"))
        item = self.tableWidget_func.item(1, 0)
        item.setText(_translate("MainWindow", "f(x1,x2)"))
        item = self.tableWidget_func.item(2, 0)
        item.setText(_translate("MainWindow", "k(x1)"))
        item = self.tableWidget_func.item(3, 0)
        item.setText(_translate("MainWindow", "m"))
        self.tableWidget_func.setSortingEnabled(__sortingEnabled)
        self.pushButton_delete_row.setText(_translate("MainWindow", "Delete row"))
        self.pushButton_delete_row.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.pushButton_delete_column.setText(_translate("MainWindow", "Delete column"))
        self.pushButton_delete_column.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.pushButton_delete_cell.setText(_translate("MainWindow", "Delete cell"))
        self.pushButton_delete_cell.setShortcut(_translate("MainWindow", "Del"))
        self.pushButton_create.setText(_translate("MainWindow", "Create Function"))
        self.pushButton_2d.setText(_translate("MainWindow", "2D view of cell"))
        self.pushButton_meaning.setToolTip(_translate("MainWindow", "Click Me"))
        self.pushButton_meaning.setText(_translate("MainWindow", "Assign Meaning"))
        self.groupBox_interResult.setTitle(_translate("MainWindow", "Intermediate results"))
        self.pushButton_del_inter_cell.setText(_translate("MainWindow", "Delete cell"))
        self.pushButton_clear_inter_cell.setText(_translate("MainWindow", "Clear all"))
        self.pushButton_export_exp.setText(_translate("MainWindow", "Export expression"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.action_New.setText(_translate("MainWindow", "&New"))
        self.action_New.setToolTip(_translate("MainWindow", "Create a grid data file"))
        self.action_New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.action_Exit.setText(_translate("MainWindow", "&Exit"))
        self.action_Exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAbout_Software.setText(_translate("MainWindow", "About Software"))
        self.action_SaveAs.setText(_translate("MainWindow", "&SaveAs"))
        self.action_User_Manual.setText(_translate("MainWindow", "&User Manual"))
        self.action_User_Manual.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Z"))

import resources_rc