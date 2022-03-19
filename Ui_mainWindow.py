# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\py\定时关机\mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(986, 421)
        mainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(570, 0, 421, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("e:\\py\\定时关机\\prpr.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(340, 30, 231, 71))
        self.label_2.setStyleSheet("font: 20pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 110, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(400, 130, 110, 30))
        self.timeEdit.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setObjectName("timeEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 133, 80, 23))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 310, 110, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 203, 80, 23))
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 273, 80, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 128, 41, 30))
        self.label_3.setStyleSheet("font: 15pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(285, 198, 101, 31))
        self.label_4.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(285, 263, 101, 41))
        self.label_5.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(400, 200, 110, 30))
        self.spinBox.setMinimumSize(QtCore.QSize(110, 30))
        self.spinBox.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setSuffix("")
        self.spinBox.setPrefix("")
        self.spinBox.setMaximum(60)
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(400, 270, 110, 30))
        self.spinBox_2.setStyleSheet("font: 12pt \"微软雅黑\";")
        self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_2.setMaximum(300)
        self.spinBox_2.setObjectName("spinBox_2")
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        self.pushButton.clicked.connect(mainWindow.Add_Time) # type: ignore
        self.pushButton_3.clicked.connect(mainWindow.Reset_Sec) # type: ignore
        self.pushButton_4.clicked.connect(mainWindow.Reset_Delay) # type: ignore
        self.pushButton_2.clicked.connect(mainWindow.Delete_Time) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "这里是Cheny的关机小助手"))
        self.label_2.setText(_translate("mainWindow", "关机小助手的设置"))
        self.pushButton.setText(_translate("mainWindow", "添加"))
        self.pushButton_2.setText(_translate("mainWindow", "删除"))
        self.pushButton_3.setText(_translate("mainWindow", "保存"))
        self.pushButton_4.setText(_translate("mainWindow", "保存"))
        self.label_3.setText(_translate("mainWindow", "时间"))
        self.label_4.setText(_translate("mainWindow", "提醒延迟（秒）"))
        self.label_5.setText(_translate("mainWindow", "关机延迟（秒）"))
