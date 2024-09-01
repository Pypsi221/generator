from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])# створення додатку


from main_window import *
from menu_window import *

#main_window.show()


menu_window.show()


class Question:
    def __init__(self,question, answer, wrong_ans1, wrong_ans2 , wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3


q1 = Question('Молоко', 'milk', 'miiillk', 'erhvhmngh', 'a0po')
q2 = Question('Вентилятор', 'fan', 'fanукекер', 'erhvhmngh', 'ауіpo')
q3 = Question('Банана', 'banana', 'ban', 'erdadahvhmngh', 'bауіpo')
q4 = Question('Бібіка', 'car', 'xz', 'ercarrr', 'аcarrуіpo')
q5 = Question('Школа', 'ad', 'school', 'erhvwsdfwhmngh', 's2wауіpo')
q6 = Question('Плач', 'cry', 'mmmmmm', 'ercrhgh', 'carауіpo')
question = [q1, q2, q3, q4, q5, q6]
radio_btns = [r_btn1, r_btn2, r_btn3, r_btn4]

cout_right = 0
cout_wrong = 0
cout_all = 0


def new_question():
    global cur_quest
    cur_quest = choice(question)
    lbl_question.setText(cur_quest.question)
    lbl_right.setText(cur_quest.answer)


    shuffle(radio_btns)
    radio_btns[0].setText(cur_quest.answer)
    radio_btns[1].setText(cur_quest.wrong_ans1)
    radio_btns[2].setText(cur_quest.wrong_ans2)
    radio_btns[3].setText(cur_quest.wrong_ans3)

new_question()

def check_ans():
    global cout_all,cout_right
    radio_buttons_group.setExclusive(False)
    for btn in radio_btns:
        if btn.isChecked():
            if btn.text() == cur_quest.answer:
                answer_group_box_group_box.hide
                cout_right += 1
                cout_all += 1
                lbl_correct.setText("Правильно")
                btn.setChecked(False)
                break
    else:
        lbl_correct.setText("Не правильно")
        btn.setChecked(False)
        cout_wrong += 1
        cout_all += 1
    radio_buttons_group.setExclusive(True)





















def to_menu():
    main_window.hide()#ховає
    menu_window.show()#показує меню 

def to_main():
    menu_window.hide()
    main_window.show()


btn_menu.clicked.connect(to_menu)#показує меню
btn_back.clicked.connect(to_main)#показує друге вікно








app.exec_()