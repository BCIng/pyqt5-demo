import sys

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QHBoxLayout
from PyQt5.QtGui import QPixmap

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("web.png")

        lbl = QLabel(self)
        lbl.setPixmap(pixmap)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.setGeometry(300,300,500,500)
        self.setWindowTitle("Red Rock")
        self.show()
        pass


if __name__ == '__main__':

    app  =QApplication(sys.argv)
    ex  =Example()
    sys.exit(app.exec_())
    pass
    