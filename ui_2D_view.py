# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2D_view.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_2D(object):
    def setupUi(self, Dialog_2D):
        Dialog_2D.setObjectName("Dialog_2D")
        Dialog_2D.setWindowModality(QtCore.Qt.NonModal)
        Dialog_2D.setEnabled(True)
        Dialog_2D.resize(400, 230)
        Dialog_2D.setMinimumSize(QtCore.QSize(400, 220))
        Dialog_2D.setSizeIncrement(QtCore.QSize(0, 0))
        Dialog_2D.setAcceptDrops(False)
        Dialog_2D.setSizeGripEnabled(False)
        Dialog_2D.setModal(False)
        self.tableWidget = QtWidgets.QTableWidget(Dialog_2D)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 211, 192))
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(187)
        self.pushButton_del_row = QtWidgets.QPushButton(Dialog_2D)
        self.pushButton_del_row.setGeometry(QtCore.QRect(260, 10, 111, 31))
        self.pushButton_del_row.setObjectName("pushButton_del_row")
        self.pushButton_save_changes = QtWidgets.QPushButton(Dialog_2D)
        self.pushButton_save_changes.setGeometry(QtCore.QRect(260, 60, 111, 31))
        self.pushButton_save_changes.setObjectName("pushButton_save_changes")
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_2D)
        self.pushButton_cancel.setGeometry(QtCore.QRect(260, 110, 111, 31))
        self.pushButton_cancel.setObjectName("pushButton_cancel")

        self.retranslateUi(Dialog_2D)
        self.pushButton_cancel.clicked.connect(Dialog_2D.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog_2D)

    def retranslateUi(self, Dialog_2D):
        _translate = QtCore.QCoreApplication.translate
        Dialog_2D.setWindowTitle(_translate("Dialog_2D", "Dialog"))
        self.pushButton_del_row.setText(_translate("Dialog_2D", "Delete row"))
        self.pushButton_save_changes.setText(_translate("Dialog_2D", "Save Changes"))
        self.pushButton_cancel.setText(_translate("Dialog_2D", "Cancel"))

