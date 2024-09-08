from PyQt5.QtWidgets import QApplication
from random import choice, shuffle

app = QApplication([])# створення додатку


from main_window import *
from menu_window import *

#main_window.show()


menu_window.show()


class Question: #створення класу для запитань
    def __init__(self,question, answer, wrong_ans1, wrong_ans2 , wrong_ans3):
        self.question = question
        self.answer = answer
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3


q1 = Question('Молоко', 'milk', 'miiillk', 'erhvhmngh', 'a0po')#питання
q2 = Question('Вентилятор', 'fan', 'fanукекер', 'erhvhmngh', 'ауіpo')#питання
q3 = Question('Банана', 'banana', 'ban', 'erdadahvhmngh', 'bауіpo')#питання
q4 = Question('Бібіка', 'car', 'xz', 'ercarrr', 'аcarrуіpo')#питання
q5 = Question('Школа', 'ad', 'school', 'erhvwsdfwhmngh', 's2wауіpo')#питання
q6 = Question('Плач', 'cry', 'mmmmmm', 'ercrhgh', 'carауіpo')#питання
questions = [q1, q2, q3, q4, q5, q6]#список з запитання
radio_btns = [r_btn1, r_btn2, r_btn3, r_btn4]#список з кнопками
#зміні для статистики
cout_right = 0
cout_wrong = 0
cout_all = 0


def new_question():#додаванння питання  в вікно з карткою
    global cur_quest
    cur_quest = choice(questions)#вибирає рандомне питання
    lbl_question.setText(cur_quest.question)#відображаємо питання
    lbl_right.setText(cur_quest.answer)# відображаємо правильну відповідь


    shuffle(radio_btns)# перелічую список з кнопками
    #додаємо варіанти відповідей кнопки
    radio_btns[0].setText(cur_quest.answer)
    radio_btns[1].setText(cur_quest.wrong_ans1)
    radio_btns[2].setText(cur_quest.wrong_ans2)
    radio_btns[3].setText(cur_quest.wrong_ans3)

new_question()

def check_ans():#первірка правильності 
    global cout_all,cout_right, cout_wrong
    radio_buttons_group.setExclusive(False)#дозволяємоо змінювати кнопки
    for btn in radio_btns:#знаходемо вибрану кнопку
        if btn.isChecked():
            if btn.text() == cur_quest.answer:
                answer_group_box.hide()
                cout_right += 1
                cout_all += 1
                lbl_correct.setText("Правильно")
                btn.setChecked(False)
                break#закінчення циклу
    else:
        lbl_correct.setText("Не правильно")
        btn.setChecked(False)
        cout_wrong += 1
        cout_all += 1
    radio_buttons_group.setExclusive(True)#блокуємо зміну кнопку


def next_question():
    if btn_answer.text()== "Відповісти":
        check_ans()
        answer_group_box.hide()
        result_group_box.show()
        btn_answer.setText("Наступне запитання")
    elif btn_answer.text() == "Наступне запитання":
        new_question()
        result_group_box.hide()
        answer_group_box.show()
        btn_answer.setText("Відповісти")

def clear():
    question_input.clear()
    right_ans_input.clear()
    wrong_1ans_input.clear()
    wrong_2ans_input.clear()
    wrong_3ans_input.clear()

def add_question():
    question = Question(
        question_input.text(),
        right_ans_input.text(),
        wrong_1ans_input.text(),
        wrong_2ans_input.text(),
        wrong_3ans_input.text())

    questions.append(question)
    clear()
    

def to_menu():
    main_window.hide()#ховає
    menu_window.show()#показує меню 

def to_main():
    menu_window.hide()
    main_window.show()


btn_menu.clicked.connect(to_menu)#показує меню
btn_back.clicked.connect(to_main)#показує друге вікно
btn_answer.clicked.connect(next_question)
btn_add.clicked.connect(add_question)
btn_clear.clicked.connect(clear)
app.exec_()