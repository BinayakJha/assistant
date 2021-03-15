from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow,self).__init__(*args,**kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://youtube.com"))
        self.setCentralWidget(self.browser)
        self.show()
        self.setWindowTitle("Alexa Browser-Supported By Google")
        self.setWindowIcon(QIcon(r'C:\Users\Laptop-16\Desktop\python\logo.ico'))





app=QApplication(sys.argv)
app.setApplicationName('My Window')
app.setOrganizationName("My Window")
app.setOrganizationDomain('mywindow.org')

window =MainWindow()
window.show()
app.exec_()