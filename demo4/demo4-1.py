import sys
from PyQt5.QtCore  import  Qt
from PyQt5.QtWidgets import QWidget,QApplication,QSlider,QLCDNumber,QVBoxLayout



class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        pass

    def initUI(self):
        lcd  =QLCDNumber(self)
        sld = QSlider(Qt.Horizontal,self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Signal and slot")
        self.show()
        pass
    pass

    




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
    