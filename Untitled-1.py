import sys
from PyQt6.QtWidgets import QApplication,  QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6 import uic
import random
from PyQt6.QtCore import Qt


class MyNotes(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.do_paint = False
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
        qp.setBrush(QColor(255, 215, 0))
        size = self.size()
        for i in range(random.randint(1, 30)):
            x = random.randint(1, size.width()-10)
            y = random.randint(1, size.height()-10) 
            r = random.randint(5, 200)
            qp.drawEllipse(x, y, r, r)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())