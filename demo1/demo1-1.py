import sys
from PyQt5.QtWidgets import QApplication,QWidget
# https://maicss.gitbook.io/pyqt5-chinese-tutoral/hello_world
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(250,150) # 控制窗口大小
    w.move(300,300) # 移动窗口显示位置
    w.setWindowTitle("demo1")  # 设置窗口标题
    w.show() # show 窗口

    sys.exit(app.exec_())
    