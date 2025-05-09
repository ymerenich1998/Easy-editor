# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 9, 681, 441))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.row = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.row.setContentsMargins(0, 0, 0, 0)
        self.row.setObjectName("row")
        self.col1 = QtWidgets.QVBoxLayout()
        self.col1.setObjectName("col1")
        self.btn_dir = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_dir.setObjectName("btn_dir")
        self.col1.addWidget(self.btn_dir)
        self.lw_files = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.lw_files.setObjectName("lw_files")
        self.col1.addWidget(self.lw_files)
        self.row.addLayout(self.col1)
        self.col2 = QtWidgets.QVBoxLayout()
        self.col2.setObjectName("col2")
        self.lb_image = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lb_image.setEnabled(True)
        self.lb_image.setMinimumSize(QtCore.QSize(0, 400))
        self.lb_image.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lb_image.setObjectName("lb_image")
        self.col2.addWidget(self.lb_image)
        self.row_tools = QtWidgets.QHBoxLayout()
        self.row_tools.setObjectName("row_tools")
        self.btn_left = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_left.setObjectName("btn_left")
        self.row_tools.addWidget(self.btn_left)
        self.btn_right = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_right.setObjectName("btn_right")
        self.row_tools.addWidget(self.btn_right)
        self.btn_flip = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_flip.setObjectName("btn_flip")
        self.row_tools.addWidget(self.btn_flip)
        self.btn_sharp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_sharp.setObjectName("btn_sharp")
        self.row_tools.addWidget(self.btn_sharp)
        self.btn_bw = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_bw.setObjectName("btn_bw")
        self.row_tools.addWidget(self.btn_bw)
        self.col2.addLayout(self.row_tools)
        self.row.addLayout(self.col2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Image Editor"))
        self.btn_dir.setText(_translate("MainWindow", "Папка"))
        self.lb_image.setText(_translate("MainWindow", "Картинка"))
        self.btn_left.setText(_translate("MainWindow", "Вліво"))
        self.btn_right.setText(_translate("MainWindow", "Вправо"))
        self.btn_flip.setText(_translate("MainWindow", "Дзеркало"))
        self.btn_sharp.setText(_translate("MainWindow", "Різкість"))
        self.btn_bw.setText(_translate("MainWindow", "Ч/Б"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
