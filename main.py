import sys
from time import sleep,localtime
from os import popen
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore
#import Ui_mainWindow
import Ui_shutWindow

Times=['8:10','9:0','10:5','10:55','11:45','14:20','15:10','16:0','16:50','21:30']

class shutWindow(QMainWindow,Ui_shutWindow.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_shutWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.WindowMinimizeButtonHint)
        self.timer=QtCore.QTimer()
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
        if s in Times and tick.tm_sec==30:
            self.show()
            popen('shutdown -s -t 30')

if __name__=='__main__':
    app=QApplication(sys.argv)

    # 关闭所有窗口,也不关闭应用程序
    QApplication.setQuitOnLastWindowClosed(False)

    swin=shutWindow()

    sys.exit(app.exec_())

