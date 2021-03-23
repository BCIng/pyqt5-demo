
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Message  Box")
        self.show()

        pass

    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, "Message", "确定退出吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    pass
