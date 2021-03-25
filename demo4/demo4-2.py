import sys

from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):


        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event handler')
        self.show()
        pass

    #重新函数
    def keyPressEvent(self,event):
        if event.key() ==Qt.Key_Escape:  # 按 Esc 键退出
            self.close()
        else:
            pass
        pass


if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
    