import sys

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter,QColor,QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        pass

    def initUI(self):
        self.text="adhasdhqiowehqioenaijieqoadadjsadjaijo"
        self.setGeometry(300,300,450,300)
        self.setWindowTitle('Drawing text')
        self.show()

        pass

    def paintEvent(self,ev):
        qp = QPainter()
        qp.begin(self)
        self.drawText(ev,qp)
        pass

    def drawText(self,ev,qp):
        qp.setPen(QColor(160,45,6))
        qp.setFont(QFont("Decorative",10))
        qp.drawText(ev.rect(),Qt.AlignCenter,self.text)
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    pass
    