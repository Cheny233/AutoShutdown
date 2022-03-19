from pickle import ADDITEMS
import sys
from time import sleep,localtime
from os import popen
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,QTimer,QSettings
from Ui_mainWindow import Ui_mainWindow
import Ui_mainWindow
import Ui_shutWindow

settings=QSettings('config.ini',QSettings.IniFormat)

TIMES=settings.value('SETUP/TIMES')
DELAY=int(settings.value('SETUP/DELAY'))
SEC=int(settings.value('SETUP/SEC'))

class mainWindow(QMainWindow,Ui_mainWindow.Ui_mainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_mainWindow.Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.spinBox.setValue(SEC)
        self.ui.spinBox_2.setValue(DELAY)
        self.setWindowIcon(QIcon("wendi.ico"))
        self.Update_List()

    def Pop(self):
        self.box=QMessageBox.information(self,'提示','设置成功！',QMessageBox.Ok)
    
    def Update_List(self):
        self.ui.listWidget.clear()
        for i in TIMES:
            self.ui.listWidget.addItem(i)

    def Add_Time(self):
        T=self.ui.timeEdit.time()
        Add=str(T.hour())+':'+str(T.minute())
        if Add not in TIMES:
            TIMES.append(Add)
            settings.setValue('SETUP/TIMES',TIMES)
            self.Update_List()
        self.Pop()
    
    def Delete_Time(self):
        item=self.ui.listWidget.currentRow()
        del TIMES[item]
        settings.setValue('SETUP/TIMES',TIMES)
        self.Update_List()
        self.Pop()

    def Reset_Delay(self):
        DELAY=self.ui.spinBox_2.value()
        self.ui.spinBox_2.setValue(DELAY)
        settings.setValue('SETUP/DELAY',DELAY)
        self.Pop()
    
    def Reset_Sec(self):
        SEC=self.ui.spinBox.value()
        self.ui.spinBox.setValue(SEC)
        settings.setValue('SETUP/SEC',SEC)
        self.Pop()


class shutWindow(QMainWindow,Ui_shutWindow.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_shutWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("wendi.ico"))
        self.setWindowFlags(Qt.WindowStaysOnTopHint|Qt.WindowMinimizeButtonHint)
        self.timer=QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.run)
        self.timer.setSingleShot(False)
        self.timer.start()
    
    def Quit(self):
        self.hide()
        popen('shutdown -a')
    
    def run(self):
        tick=localtime()
        s=str(tick.tm_hour)+':'+str(tick.tm_min)
        if s in TIMES and tick.tm_sec==SEC:
            self.show()
            popen('shutdown -s -t 30')

if __name__=='__main__':
    app=QApplication(sys.argv)

    # 关闭所有窗口,也不关闭应用程序
    QApplication.setQuitOnLastWindowClosed(False)

    mwin=mainWindow()

    swin=shutWindow()
    
    mwin.show()

    sys.exit(app.exec_())

