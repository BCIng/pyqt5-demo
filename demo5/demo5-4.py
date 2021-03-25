import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow,QTextEdit,QAction,QFileDialog,QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit= QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()


        openFile =QAction(QIcon("web.png"),"Open",self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip("Open new File")
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openFile)




        self.setGeometry(300,300,450,150)
        self.setWindowTitle("File Dialog")
        self.show()
        pass

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self,"Open File","/home")
        if fname[0]:
            f = open(fname[0],'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass

    