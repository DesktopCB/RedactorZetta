# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'endtask.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EndTask(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showhere = QtWidgets.QPushButton(self.centralwidget)
        self.showhere.setGeometry(QtCore.QRect(60, 420, 681, 61))
        self.showhere.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"font: 57 13pt \"UndertaleFont\";\n"
"border-radius : 12px;")
        self.showhere.setObjectName("showhere")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 30, 271, 51))
        self.label.setStyleSheet("color: rgb(225, 225, 225);\n"
"font: 20pt \"Raleway\";\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.exporting = QtWidgets.QPushButton(self.centralwidget)
        self.exporting.setGeometry(QtCore.QRect(60, 500, 681, 61))
        self.exporting.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"font: 57 13pt \"raleway\";\n"
"border-radius : 12px;")
        self.exporting.setObjectName("exporting")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 100, 681, 301))
        self.textEdit.setStyleSheet("background-color: rgb(226, 226, 226);\n"
"font: 57 13pt \"Tahoma\";\n"
"border-radius : 12px;")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Закончить задание"))
        self.showhere.setText(_translate("MainWindow", "Показать тут"))
        self.label.setText(_translate("MainWindow", "Получить задание"))
        self.exporting.setText(_translate("MainWindow", "Экспортировать в JSON"))