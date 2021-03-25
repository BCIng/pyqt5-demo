import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit


class Button(QPushButton):

    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.setAcceptDrops(True)


    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore() 

    def dropEvent(self, e):

        self.setText(e.mimeData().text()) 


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        pass

    def initUI(self):

        edit = QLineEdit("",self)
        edit.setDragEnabled(True)
        edit.move(30,30)
        button  =Button("Button",self)
        button.move(80,80)




        self.setGeometry(300,300,450,300)
        self.setWindowTitle("Simple drag and drop")
        self.show()
        pass






if __name__ == '__main__':
    app =QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
    