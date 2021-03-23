import sys

from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')    
        self.show()

    def contextMenuEvent(self,event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        openAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("quit")

        action  =cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()



        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
    pass