import sys
from PyQt6.QtWidgets import QApplication,  QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6 import uic
import random
from PyQt6.QtCore import Qt


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.do_paint = False
        self.setGeometry(0, 0, 800, 600)
        self.pushButton = QPushButton("Ахалай-Махалай!", self)
        self.pushButton.resize(301, 81)
        self.pushButton.move(240, 270)
        self.pushButton.setStyleSheet("background-color: rgb(255, 215, 0); border-radius: 25px; font-weight: bold; font-size: 20px;")
        self.setStyleSheet("background-color: black")
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()


    def draw_flag(self, qp):
        size = self.size()
        for i in range(random.randint(1, 30)):
            qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            x = random.randint(1, size.width()-10)
            y = random.randint(1, size.height()-10) 
            r = random.randint(5, 200)
            qp.drawEllipse(x, y, r, r)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())