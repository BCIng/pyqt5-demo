import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QCheckBox,QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        pass

    def initUI(self):

        cb = QCheckBox("Show title",self)
        cb.move(15,15)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)




        self.setGeometry(300,300,450,250)
        self.setWindowTitle("Check box")
        self.show()
        pass

    def changeTitle(self,state):
        if state ==Qt.Checked:
            self.setWindowTitle("Check ok")
        else:
            self.setWindowTitle("Check no")
        pass



if __name__ == '__main__':
    app =QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
    