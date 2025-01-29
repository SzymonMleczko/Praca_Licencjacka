from PyQt5.QtWidgets import *

from DBQacces import read
from DBUacces import readDBU,update,current,next,prev

from DBUshow import WindowDBshow


class WindowAnswer(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        x=current()

        record = read(x)

        self.label = QLabel(self)
        self.label.setText(record['question'])
        self.label.resize(800,20)
        self.label.move(20,80)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 100)
        self.textbox.resize(280,40)
        self.textbox.hide()

        self.check_group = QButtonGroup()
        self.yescheckbox = QCheckBox('tak',self)
        self.yescheckbox.setChecked(False)
        self.yescheckbox.move(20,100)
        self.check_group.addButton(self.yescheckbox,1)

        self.nocheckbox = QCheckBox('nie',self)
        self.nocheckbox.setChecked(True)
        self.nocheckbox.move(80,100)
        self.check_group.addButton(self.nocheckbox,2)


        self.label1 = QLabel(self)
        self.label1.setText("A Małżonek/Małżonka?")
        self.label1.move(20,160)
        self.label1.hide()

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20, 180)
        self.textbox1.resize(280,40) 
        self.textbox1.hide()

        self.check_group1 = QButtonGroup()
        self.yescheckbox1 = QCheckBox('tak',self)
        self.yescheckbox1.setChecked(False)
        self.yescheckbox1.move(20,180)
        self.yescheckbox1.hide()
        self.check_group1.addButton(self.yescheckbox1,1)

        self.nocheckbox1 = QCheckBox('nie',self)
        self.nocheckbox1.setChecked(True)
        self.nocheckbox1.move(80,180)
        self.nocheckbox1.hide()
        self.check_group1.addButton(self.nocheckbox1,2)


        self.button_ready = QPushButton('Gotowe', self)
        self.button_ready.move(180,300)
        self.button_ready.clicked.connect(self.on_click_ready)

        self.button_check = QPushButton('Wprowadzone wartości', self)
        self.button_check.move(228,400)
        self.button_check.clicked.connect(self.on_click_DBUshow)

        self.button_prev = QPushButton('Poprzednie', self)
        self.button_prev.move(400,400)
        self.button_prev.clicked.connect(self.on_click_prev)

        self.button_next = QPushButton('Następne', self)
        self.button_next.move(500,400)
        self.button_next.clicked.connect(self.on_click_next)
        


        self.show()
        self.setGeometry(500, 550, 800, 550)
        self.setWindowTitle("Zapytania")
        self.show()
        if x != 1:
            update('current',prev(x))
            self.on_click_next()
    
    def on_click_next(self):

        x=next(current())
        update('current',x)

        record=read(x)
       
        self.label.setText(record['question'])
        mar = readDBU('2')
        if mar == 1:
            if record['type'] == 'B':
                self.yescheckbox1.show()
                self.nocheckbox1.show()
                self.nocheckbox1.setChecked(True)
                self.label1.show()
                self.textbox1.hide()
            elif record['type'] == 'W':
                self.yescheckbox1.hide()
                self.nocheckbox1.hide()
                self.label1.hide()
                self.textbox1.hide()
            else:
                self.yescheckbox1.hide()
                self.nocheckbox1.hide()
                self.label1.show()
                self.textbox1.show()
        if record['type'] == 'B':
            self.yescheckbox.show()
            self.nocheckbox.show()
            self.nocheckbox.setChecked(True)
            self.label.show()
            self.textbox.hide()
        else:
            self.yescheckbox.hide()
            self.nocheckbox.hide()
            self.label.show()
            self.textbox.show()

        
        self.label.update()
        self.update()

        
    
    def on_click_ready(self):
        x=int(current())
        mari = readDBU('2')

        record = read(x)
        
        textboxValue = self.textbox.text()
        textboxValue1= self.textbox1.text()
        if record['type'] == 'B':
            if self.yescheckbox.isChecked():

                if self.yescheckbox1.isChecked():
                    update(str(x),1)
                    update(str(x+1),1)
                     
                else:   
                    update(str(x),1)
                    update(str(x+1),0)

            else:
                if self.yescheckbox1.isChecked() :
                    update(str(x),0)
                    update(str(x+1),1)
                     
                else:   
                    update(str(x),0)
                    update(str(x+1),0)
            self.on_click_next()
        else:
            if textboxValue.isnumeric():
                
                update(str(x),textboxValue)

                if mari == 1:
                    if textboxValue1.isnumeric():
                        if x in range(52-86):
                            update(str(x+35),textboxValue1)
                        else:
                            update(str(x+1),textboxValue1)                       
                    else:
                        QMessageBox.question(self, 'Message ', "Nie poprawna wartość dla małżonki: " + textboxValue1, QMessageBox.Ok, QMessageBox.Ok)

            else:
                QMessageBox.question(self, 'Message ', "Nie poprawna wartość: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)

            self.on_click_next()

        self.textbox.setText("")
        self.textbox1.setText("")
        
    
    def on_click_DBUshow(self):
        self.w = WindowDBshow()
        self.w.show()
    
    def on_click_prev(self):
        x = prev(prev(current()))
        update('current',x)
        self.on_click_next()



