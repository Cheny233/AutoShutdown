import sys
from time import sleep,localtime
from os import popen
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore
#import Ui_mainWindow
import Ui_shutWindow1

Times=['8:10','9:0','10:5','10:55','11:45','13:20','14:10','15:0','16:50','21:30']

'''
def monitor():
    global swin
    tick=localtime()
    s=str(tick.tm_hour)+':'+str(tick.tm_min)
    if s in Times and tick.tm_sec==45:
        swin.show()
        popen('shutdown -s -t 30')
    tr=Timer(0.3,monitor)
    tr.start()
 '''

class shutWindow(QMainWindow,Ui_shutWindow1.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.timer=QtCore.QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.run)
        self.timer.setSingleShot(False)
        self.timer.start()
    
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
    '''
    mwin=QMainWindow()
    mui=Ui_mainWindow.Ui_mainWindow()
    mui.setupUi(mwin)
    '''
    swin=shutWindow()
    sui=Ui_shutWindow1.Ui_MainWindow()
    sui.setupUi(swin)
    swin.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint|QtCore.Qt.WindowMinimizeButtonHint)

    sys.exit(app.exec_())

