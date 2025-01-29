import sys
from PyQt5.QtWidgets import *
from Answers import WindowAnswer
from DBUshow import WindowDBshow
from DBUacces import restart as restartDBU,check

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        
        self.button_begin = QPushButton("Rozpocznij",self)
        self.button_begin.move(50,200)
        self.button_begin.clicked.connect(self.button_begin_clicked)

        self.button_reset = QPushButton("Wyczyść dane", self)
        self.button_reset.move(140,200)
        self.button_reset.clicked.connect(self.button_reset_clicked)

        self.button_data = QPushButton("Wprowadzone dane", self)
        self.button_data.move(250, 200)
        self.button_data.clicked.connect(self.button_data_clicked)

        self.button_close = QPushButton("Zamknij Aplikacje", self)
        self.button_close.clicked.connect(self.close)
        self.button_close.move(410, 200)

        
        self.setGeometry(500, 550, 600, 400)
        self.setWindowTitle("Menu")
        self.show()
        
    def button_begin_clicked(self):
        if check():
            restartDBU()
        self.w = WindowAnswer()
        self.w.show()
        
    def button_reset_clicked(self):
        restartDBU()

    def button_data_clicked(self):
        self.w = WindowDBshow()
        self.w.show()


    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = Window()
    sys.exit(app.exec_())
