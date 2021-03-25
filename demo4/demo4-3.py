import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget,QGridLayout,QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x=0
        y=0

        self.text = "x:{0},y:{1}".format(x,y)
        self.label = QLabel(self.text,self)
        grid.addWidget(self.label,0,0,Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300,300,450,150)
        self.setWindowTitle("Event Object")
        self.show()



        pass
    
    # 获取鼠标的位置
    def mouseMoveEvent(self,event):
        x = event.x()
        y  = event.y()
        text = "x:{0},y:{1}".format(x,y)
        self.label.setText(text)
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass