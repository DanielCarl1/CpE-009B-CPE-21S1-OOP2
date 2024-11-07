import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton

class Ques_No2(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "SPECIAL MIDTERM EXAM IN OOP_09"
        self.x = 500
        self.y = 450
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)

        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.layout.setColumnStretch(1, 1)
        self.button = QPushButton("CLICK TO CHANGE COLOR", self)
        self.button.clicked.connect(self.changeColor)
        self.layout.addWidget(self.button, 1, 1)

    def changeColor(self):
        self.button.setStyleSheet("background-color: yellow")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ques_No2()
    sys.exit(app.exec_())