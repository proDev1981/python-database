from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class App(QMainWindow):
    def _init_(self,parent=None,*arg):
        super(App,self)._init_(parent=parent)
        self.setWindowTitle("hola")


app = QApplication([])
win = App()
win.show()
app.exec_()
