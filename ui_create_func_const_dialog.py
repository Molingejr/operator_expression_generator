# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_func_const_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_create_fc(object):
    def setupUi(self, Dialog_create_fc):
        Dialog_create_fc.setObjectName("Dialog_create_fc")
        Dialog_create_fc.resize(273, 251)
        self.groupBox_createfunconst = QtWidgets.QGroupBox(Dialog_create_fc)
        self.groupBox_createfunconst.setGeometry(QtCore.QRect(10, 10, 251, 221))
        self.groupBox_createfunconst.setObjectName("groupBox_createfunconst")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_createfunconst)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 215, 141))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboBox_1 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.pushButton_save)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_clear)
        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)

        self.retranslateUi(Dialog_create_fc)
        QtCore.QMetaObject.connectSlotsByName(Dialog_create_fc)

    def retranslateUi(self, Dialog_create_fc):
        _translate = QtCore.QCoreApplication.translate
        Dialog_create_fc.setWindowTitle(_translate("Dialog_create_fc", "Dialog"))
        self.groupBox_createfunconst.setTitle(_translate("Dialog_create_fc", "Create Function/Constant"))
        self.label_2.setText(_translate("Dialog_create_fc", "Type"))
        self.comboBox_1.setItemText(0, _translate("Dialog_create_fc", "Constant"))
        self.comboBox_1.setItemText(1, _translate("Dialog_create_fc", "Function"))
        self.label_3.setText(_translate("Dialog_create_fc", "Number of args"))
        self.label_4.setText(_translate("Dialog_create_fc", "Section"))
        self.comboBox_2.setItemText(0, _translate("Dialog_create_fc", "Vertical"))
        self.comboBox_2.setItemText(1, _translate("Dialog_create_fc", "Horizontal"))
        self.pushButton_save.setText(_translate("Dialog_create_fc", "Save"))
        self.pushButton_clear.setText(_translate("Dialog_create_fc", "Clear"))
        self.label_1.setText(_translate("Dialog_create_fc", "Input Name"))

