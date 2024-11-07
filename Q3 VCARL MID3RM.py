import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton

class Ques_No3(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "MIDTERM IN 00P_09"
        self.x = 400
        self.y = 400
        self.width = 500
        self.height = 250
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(2, 1)

        self.Label1 = QLabel('ENTER YOUR FULLNAME: ')
        self.layout.addWidget(self.Label1, 0, 0)

        self.Entry4 = QLineEdit()
        self.layout.addWidget(self.Entry4, 0, 1)

        self.button = QPushButton("CLICK TO DISPLAY YOUR FULLNAME", self)
        self.button.clicked.connect(self.showFullname)
        self.layout.addWidget(self.button, 1, 0)
        self.Entry5 = QLineEdit()
        self.layout.addWidget(self.Entry5, 1, 1)

        self.displayLabel = QLabel('')
        self.layout.addWidget(self.displayLabel, 1, 1)

    def showFullname(self):
        fullname = self.Entry4.text()
        self.displayLabel.setText(fullname)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ques_No3()
    sys.exit(app.exec_())