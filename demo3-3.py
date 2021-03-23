import sys

from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QPushButton,QGridLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        names = ['Cls', 'Bck', '', 'Close',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+']

        positions  = [(i,j) for i in range(5) for j in range(4)]
        print(positions)

        for position ,name in zip(positions,names):
            if name =="":
                continue
            button  = QPushButton(name)
            grid.addWidget(button,*position)


        




        self.move(300, 150)
        self.setWindowTitle("Calculator")
        self.show()
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
    