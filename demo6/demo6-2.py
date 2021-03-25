import sys
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        pass

    def initUI(self):
        self.col = QColor(0, 0, 0)

        redBtn = QPushButton("Red", self)
        redBtn.setCheckable(True)
        redBtn.move(10, 10)

        redBtn.clicked[bool].connect(self.setColor)

        greenBtn = QPushButton("Green", self)
        greenBtn.setCheckable(True)
        greenBtn.move(10, 60)

        greenBtn.clicked[bool].connect(self.setColor)

        buleBtn = QPushButton("Blue", self)
        buleBtn.setCheckable(True)
        buleBtn.move(10, 110)

        buleBtn.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet(
            "QWidget { background-color: %s }" % self.col.name())

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle("toggle button")
        self.show()

        pass

    def setColor(self, pressed):

        source = self.sender()
        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == 'Red':
            self.col.setRed(val)
            pass
        elif source.text() == "Green":
            self.col.setGreen(val)
            pass
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet(
            "QFrame {background-color: %s}" % self.col.name())

        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

    pass
