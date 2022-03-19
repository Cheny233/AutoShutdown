from fnmatch import translate
from pickle import ADDITEMS
import sys
from time import sleep,localtime
from os import popen
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from PyQt5.QtWidgets import QSystemTrayIcon,QMenu,QAction
from PyQt5.QtGui import QIcon,QCursor
from PyQt5.QtCore import Qt,QTimer,QSettings
from PyQt5.QtCore import QCoreApplication
from Ui_mainWindow import Ui_mainWindow
import Ui_mainWindow
import Ui_shutWindow

settings=QSettings('config.ini',QSettings.IniFormat)

TIMES=settings.value('SETUP/TIMES')
DELAY=int(settings.value('SETUP/DELAY'))
SEC=int(settings.value('SETUP/SEC'))

class tray(QSystemTrayIcon):

    def __init__(self):
        super().__init__()
        self.setIcon(QIcon("wendi.ico"))
        self.activated.connect(self.click)
        self.menu=QMenu()
        self.action1=QAction('设置(settings)',self,triggered=self.Setting)
        self.action2=QAction('退出(exit)',self,triggered=self.Quit)

        self.menu.addAction(self.action1)
        self.menu.addAction(self.action2)
        self.setContextMenu(self.menu)

    
    def click(self):
        #self.menu.move(QCursor.pos())
        self.menu.show()


    def Setting(self):
        mwin.show()
    

    def Quit(self):
        app.quit()


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
        global DELAY
        DELAY=self.ui.spinBox_2.value()
        self.ui.spinBox_2.setValue(DELAY)
        settings.setValue('SETUP/DELAY',DELAY)
        swin.ui.label_5.setText(QCoreApplication.translate("MainWindow", str(DELAY)))
        self.Pop()
    

    def Reset_Sec(self):
        global SEC
        SEC=self.ui.spinBox.value()
        self.ui.spinBox.setValue(SEC)
        settings.setValue('SETUP/SEC',SEC)
        self.Pop()


class shutWindow(QMainWindow,Ui_shutWindow.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_shutWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label_5.setText(QCoreApplication.translate("MainWindow", str(DELAY)))
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
            popen('shutdown -s -t '+str(DELAY))


if __name__=='__main__':
    app=QApplication(sys.argv)

    # 关闭所有窗口,也不关闭应用程序
    QApplication.setQuitOnLastWindowClosed(False)

    mwin=mainWindow()

    tip=tray()
    tip.show()

    swin=shutWindow()

    sys.exit(app.exec_())

