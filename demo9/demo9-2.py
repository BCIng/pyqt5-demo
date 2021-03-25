import sys
import random

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        pass

    def initUI(self):

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle("Points")
        self.show()

    def paintEvent(self, ev):
        qp = QPainter()
        qp.begin(self)
        self.drawPoint(qp)
        qp.end()
        pass

    def drawPoint(self, qp):
        qp.setPen(Qt.red)
        size = self.size()

        for i in range(10000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height() - 1)
            qp.drawPoint(x, y)
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
