import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QAction, QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
        exitAct = QAction(QIcon("web.png"), "Exit", self)
        exitAct.setShortcut("Ctrl+Q")
        exitAct.setStatusTip("Exit Application")
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar("&Exit")
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Main Window")
        self.show()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
