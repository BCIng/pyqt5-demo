import sys
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QTextEdit,QLabel,QLineEdit,QGridLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        title = QLabel("title")
        author = QLabel("author")
        review = QLabel("review")

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit  = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)






        self.setGeometry(300,300,450,400)
        self.setWindowTitle("Review")
        self.show()
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex =Example()
    sys.exit(app.exec_())


    pass

    