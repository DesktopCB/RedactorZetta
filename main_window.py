# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.create_item = QtWidgets.QPushButton(self.centralwidget)
        self.create_item.setGeometry(QtCore.QRect(190, 420, 161, 61))
        self.create_item.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"font: 57 13pt \"UndertaleFont\";\n"
"border-radius : 12px;")
        self.create_item.setObjectName("create_item")
        self.create_task = QtWidgets.QPushButton(self.centralwidget)
        self.create_task.setGeometry(QtCore.QRect(440, 420, 161, 61))
        self.create_task.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"font: 57 13pt \"UndertaleFont\";\n"
"border-radius : 12px;")
        self.create_task.setObjectName("create_task")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 70, 271, 101))
        self.label.setStyleSheet("color: rgb(225, 225, 225);\n"
"font: 36pt \"Raleway\";\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Редактор информации"))
        self.create_item.setText(_translate("MainWindow", "Создать предмет"))
        self.create_task.setText(_translate("MainWindow", "Создать задание"))
        self.label.setText(_translate("MainWindow", " Zetta"))