import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QFrame,QSplitter,QStyleFactory
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QHBoxLayout(self)

        topLeft  = QFrame(self)
        topLeft.setFrameShape(QFrame.StyledPanel)

        topRight  = QFrame(self)
        topRight.setFrameShape(QFrame.StyledPanel)

        bottom  = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1  =QSplitter(Qt.Horizontal)
        splitter1.addWidget(topLeft)
        splitter1.addWidget(topRight)


        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)


        self.setGeometry(300,300,450,450)
        self.setWindowTitle("QSplitter")
        self.show()
        pass



if __name__ == '__main__':
    app  =QApplication(sys.argv)
    ex  =Example()
    sys.exit(app.exec_())
    pass
    