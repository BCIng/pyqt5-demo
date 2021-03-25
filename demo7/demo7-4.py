import sys
from PyQt5.QtWidgets import QApplication ,QWidget,QLabel,QComboBox

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        pass

    def initUI(self):

        self.lbl = QLabel("WINDOWS",self)

        combo  =QComboBox(self)
        combo.addItem("WINDOWS")
        combo.addItem("UBUNTU")
        combo.addItem("MACOS")

        combo.move(50,50)
        self.lbl.move(50,80)

        combo.activated[str].connect(self.onActivated)



        self.setGeometry(300,300,450,200)
        self.setWindowTitle("QComboBox")
        self.show()

        pass

    def onActivated(self,text):
        self.lbl.setText(text)
        self.lbl.adjustSize()



if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex =Example()
    sys.exit(app.exec_())
    pass
    