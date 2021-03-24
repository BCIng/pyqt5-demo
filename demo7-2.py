import sys

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        pass

    def initUI(self):

        self.lbl = QLabel(self)
        self.lbl.move(60,40)


        qle = QLineEdit(self)
        qle.move(60,100)

        qle.textChanged[str].connect(self.onChange)
        


      

        self.setGeometry(300,300,500,500)
        self.setWindowTitle("Red Rock")
        self.show()
        pass

    def onChange(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

        pass


if __name__ == '__main__':

    app  =QApplication(sys.argv)
    ex  =Example()
    sys.exit(app.exec_())
    pass
    