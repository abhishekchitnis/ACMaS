# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SIMSR.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(840, 631)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Abhishek Chitnis/Music/OnePiece/Apps/USB Icon/mba.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.SemNo = QtWidgets.QComboBox(Dialog)
        self.SemNo.setGeometry(QtCore.QRect(120, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.SemNo.setFont(font)
        self.SemNo.setEditable(False)
        self.SemNo.setObjectName("SemNo")
        self.SemNo.addItem("")
        self.SemNo.addItem("")
        self.SemNo.addItem("")
        self.SemNo.addItem("")
        self.SemNo.addItem("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(390, 10, 441, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("sasmira logo.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.SeltSemt = QtWidgets.QLabel(Dialog)
        self.SeltSemt.setGeometry(QtCore.QRect(20, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.SeltSemt.setFont(font)
        self.SeltSemt.setObjectName("SeltSemt")
        self.SeltStrm = QtWidgets.QLabel(Dialog)
        self.SeltStrm.setGeometry(QtCore.QRect(240, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.SeltStrm.setFont(font)
        self.SeltStrm.setObjectName("SeltStrm")
        self.StrmNam = QtWidgets.QComboBox(Dialog)
        self.StrmNam.setGeometry(QtCore.QRect(320, 130, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.StrmNam.setFont(font)
        self.StrmNam.setEditable(False)
        self.StrmNam.setObjectName("StrmNam")
        self.StrmNam.addItem("")
        self.StrmNam.addItem("")
        self.StrmNam.addItem("")
        self.StrmNam.addItem("")
        self.StrmNam.addItem("")
        self.StrmNam.addItem("")
        self.SeltOptnSubj = QtWidgets.QLabel(Dialog)
        self.SeltOptnSubj.setGeometry(QtCore.QRect(450, 130, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.SeltOptnSubj.setFont(font)
        self.SeltOptnSubj.setObjectName("SeltOptnSubj")
        self.StrmNam_2 = QtWidgets.QComboBox(Dialog)
        self.StrmNam_2.setGeometry(QtCore.QRect(670, 130, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.StrmNam_2.setFont(font)
        self.StrmNam_2.setEditable(False)
        self.StrmNam_2.setObjectName("StrmNam_2")
        self.StrmNam_2.addItem("")
        self.StrmNam_2.addItem("")
        self.StrmNam_2.addItem("")
        self.StrmNam_2.addItem("")
        self.StrmNam_2.addItem("")
        self.SemNo_2 = QtWidgets.QComboBox(Dialog)
        self.SemNo_2.setGeometry(QtCore.QRect(150, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.SemNo_2.setFont(font)
        self.SemNo_2.setEditable(False)
        self.SemNo_2.setObjectName("SemNo_2")
        self.SemNo_2.addItem("")
        self.SemNo_2.addItem("")
        self.SemNo_2.addItem("")
        self.SemNo_2.addItem("")
        self.SemNo_2.addItem("")
        self.SeltSemt_2 = QtWidgets.QLabel(Dialog)
        self.SeltSemt_2.setGeometry(QtCore.QRect(20, 190, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(12)
        self.SeltSemt_2.setFont(font)
        self.SeltSemt_2.setObjectName("SeltSemt_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SIMSR Result Generator"))
        self.SemNo.setItemText(0, _translate("Dialog", "Select..."))
        self.SemNo.setItemText(1, _translate("Dialog", "Sem 1"))
        self.SemNo.setItemText(2, _translate("Dialog", "Sem 2"))
        self.SemNo.setItemText(3, _translate("Dialog", "Sem 3"))
        self.SemNo.setItemText(4, _translate("Dialog", "Sem 4"))
        self.label.setText(_translate("Dialog", "SIMSR Results Generator"))
        self.SeltSemt.setText(_translate("Dialog", "Semester :"))
        self.SeltStrm.setText(_translate("Dialog", "Stream :"))
        self.StrmNam.setItemText(0, _translate("Dialog", "Select..."))
        self.StrmNam.setItemText(1, _translate("Dialog", "Finance"))
        self.StrmNam.setItemText(2, _translate("Dialog", "Marketing"))
        self.StrmNam.setItemText(3, _translate("Dialog", "Operation"))
        self.StrmNam.setItemText(4, _translate("Dialog", "HR"))
        self.StrmNam.setItemText(5, _translate("Dialog", "System"))
        self.SeltOptnSubj.setText(_translate("Dialog", "Select Optional Subject :"))
        self.StrmNam_2.setItemText(0, _translate("Dialog", "Select..."))
        self.StrmNam_2.setItemText(1, _translate("Dialog", "Maths"))
        self.StrmNam_2.setItemText(2, _translate("Dialog", "History"))
        self.StrmNam_2.setItemText(3, _translate("Dialog", "Geography"))
        self.StrmNam_2.setItemText(4, _translate("Dialog", "Science"))
        self.SemNo_2.setItemText(0, _translate("Dialog", "Select..."))
        self.SemNo_2.setItemText(1, _translate("Dialog", "Sem 1"))
        self.SemNo_2.setItemText(2, _translate("Dialog", "Sem 2"))
        self.SemNo_2.setItemText(3, _translate("Dialog", "Sem 3"))
        self.SemNo_2.setItemText(4, _translate("Dialog", "Sem 4"))
        self.SeltSemt_2.setText(_translate("Dialog", "Enter Seat No. :"))

