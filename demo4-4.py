import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1",self)
        btn1.move(15,15)

        btn2 = QPushButton("Button 2",self)
        btn2.move(45,50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Event sender")
        self.show()
        pass

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text()+"was pressed")
        pass







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex =Example()
    sys.exit(app.exec_())
    pass