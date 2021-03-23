import sys
from PyQt5.QtWidgets import QMainWindow,QAction,qApp,QApplication

from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon("web.png"),"&Exit",self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit Application")
        exitAct.triggered.connect(qApp.quit)


        self.statusBar()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(exitAct)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Simple menu")
        self.show()
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    main()
    