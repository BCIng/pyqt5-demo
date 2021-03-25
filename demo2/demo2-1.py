import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.statusBar().showMessage("Ready")
        self.setGeometry(300,300,250,150)
        self.setWindowTitle("StatusBar")
        self.show()

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
    
    