from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox, QLabel,
 QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit)
class okno1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Название окна')
        self.resize(500,500)
        self.move(400,100)
        self.l1 = QLabel('Буквы 1')
        self.l2 = QLabel('Буквы 2')
        self.btn = QPushButton('Кнопка 1')
        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.l1)
        self.v1.addWidget(self.l2)
        self.v1.addWidget(self.btn)
        self.setLayout(self.v1)
        self.show()
        self.btn.clicked.connect(self.next)
    def next(self):
        self.hide()
        self.win = okno2()
class okno2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Название окна')
        self.resize(500,500)
        self.move(400,100)
        self.l1 = QLabel('Буквы 1')
        self.l2 = QLabel('Буквы 2')
        self.btn = QPushButton('Кнопка 1')
        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.l1)
        self.v1.addWidget(self.l2)
        self.v1.addWidget(self.btn)
        self.setLayout(self.v1)
        self.show()
        self.btn.clicked.connect(self.next)
    def next(self):
        self.hide()
        self.win = okno3()
class okno3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Название окна')
        self.resize(500,500)
        self.move(400,100)
        self.l1 = QLabel('Буквы 1')
        self.l2 = QLabel('Буквы 2')
        self.btn = QPushButton('Кнопка 1')
        self.v1 = QVBoxLayout()
        self.v1.addWidget(self.l1)
        self.v1.addWidget(self.l2)
        self.v1.addWidget(self.btn)
        self.setLayout(self.v1)
        self.show()
app = QApplication([])
window = okno1()
app.exec_()


