### БПМ-22-1
### Лысенко Максим
### Козин Вячеслав
### Заруба Александр

import sys
from typing import List
from functools import reduce
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QComboBox, QLabel, QStackedLayout


def factorial(number):
    if number == 0:
        return 1
    elif number == 1:
        return number
    else:
        return number * factorial(number - 1)
    
def summa(list: List[int]):
    return str(sum(list))

def multiplication(list: List[int]):
    return str(reduce(lambda x, y: x * y, list))

def rearrangement_with(n, m):
    if int(n) >= 0 and int (m) >= 0:
        return str(int(int(n) ** int(m)))
    else:
        return "При вводе данных вы допустили ошибку"

def rearrangement_without(n, m):
    if int(m) <= int(n) and int(n) >= 0 and int (m) >= 0:
        return str(int(factorial(int(n))/factorial(int(n-m))))
    else:
        return "При вводе данных вы допустили ошибку"

def comb_with(n, m):
    if int(n) >= 0 and int (m) >= 0:
        return str(int(factorial(int(n) + int(m) - 1)/(factorial(int(m)) * factorial(int(n-1)))))
    else:
        return "При вводе данных вы допустили ошибку"

def comb_without(n, m):
    if int(m) <= int(n) and int(n) >= 0 and int (m) >= 0:
        return str(int(factorial(int(n))/(factorial(int(m)) * factorial(int(n-m)))))
    else:
        return "При вводе данных вы допустили ошибку"

def permutations_with(list: List[int]):
    chis = sum(list)
    list_fac_values = [factorial(num) for num in list]
    znam = 1
    for value in list_fac_values:
        znam *= value 
    return str(int(factorial(int(chis))/int(znam)))

def permmutations_without(n):
    if int(n) >= 0:
        return str(int(factorial(int(n))))
    else:
        return "При вводе данных вы допустили ошибку"




class Combinatorika(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Комбинаторные схемы')
        self.setGeometry(600, 200, 400, 500)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        

        # Сделали макет с переключением
        self.stacked_layout = QStackedLayout()
        
        # Добавление виджета для Начальной страницы
        self.stacked_layout.addWidget(QLabel("Здравствуйте! Я калькулятор комбинаторных схем!"))

        # Виджет под правило суммы
        self.widget1 = QWidget()
        self.layout_1 = QVBoxLayout()
        
        self.layout_1.addWidget(QLabel("Введите количество объектов каждого типа через запятую"))

        self.layout_1_2 = QHBoxLayout()
        self.layout_1_2.addWidget(QLabel("(n1, n2, ..., nk): "))
        self.input_line_n_1 = QLineEdit()
        self.layout_1_2.addWidget(self.input_line_n_1)
        self.layout_1.addLayout(self.layout_1_2)

        self.layout_1_3 = QHBoxLayout()
        self.layout_1_3.addWidget(QLabel("Решение: "))
        self.output_line_1 = QLineEdit()
        self.layout_1_3.addWidget(self.output_line_1)
        self.layout_1.addLayout(self.layout_1_3)

        self.widget1.setLayout(self.layout_1)
        self.stacked_layout.addWidget(self.widget1)

        # Виджет под правило умножения
        self.widget2 = QWidget()
        self.layout_2 = QVBoxLayout()
        
        self.layout_2.addWidget(QLabel("Введите количество объектов каждого типа через запятую"))

        self.layout_2_2 = QHBoxLayout()
        self.layout_2_2.addWidget(QLabel("(n1, n2, ..., nk): "))
        self.input_line_n_2 = QLineEdit()
        self.layout_2_2.addWidget(self.input_line_n_2)
        self.layout_2.addLayout(self.layout_2_2)

        self.layout_2_3 = QHBoxLayout()
        self.layout_2_3.addWidget(QLabel("Решение: "))
        self.output_line_2 = QLineEdit()
        self.layout_2_3.addWidget(self.output_line_2)
        self.layout_2.addLayout(self.layout_2_3)

        self.widget2.setLayout(self.layout_2)
        self.stacked_layout.addWidget(self.widget2)
        
        # Виджет под размещение с повторениями
        self.widget3 = QWidget()
        self.layout_3 = QVBoxLayout()
        self.layout_3_1 = QHBoxLayout()
        
        self.layout_3.addWidget(QLabel("Из n объектов выбираем m объектов и переставляем всеми способами"))

        self.layout_3_1.addWidget(QLabel("n="))
        self.input_line_n_3 = QLineEdit()
        self.layout_3_1.addWidget(self.input_line_n_3)
        self.layout_3_1.addWidget(QLabel("m="))
        self.input_line_m_3 = QLineEdit()
        self.layout_3_1.addWidget(self.input_line_m_3)
        self.layout_3.addLayout(self.layout_3_1)

        self.layout_3_2 = QHBoxLayout()
        self.layout_3_2.addWidget(QLabel("Решение: "))
        self.output_line_3 = QLineEdit()
        self.layout_3_2.addWidget(self.output_line_3)
        self.layout_3.addLayout(self.layout_3_2)

        self.widget3.setLayout(self.layout_3)
        self.stacked_layout.addWidget(self.widget3)
        
        # Виджет под размещения без повторений
        self.widget4 = QWidget()
        self.layout_4 = QVBoxLayout()
        self.layout_4_1 = QHBoxLayout()
        
        self.layout_4.addWidget(QLabel("Из n объектов выбираем m объектов и переставляем всеми способами"))

        self.layout_4_1.addWidget(QLabel("n="))
        self.input_line_n_4 = QLineEdit()
        self.layout_4_1.addWidget(self.input_line_n_4)
        self.layout_4_1.addWidget(QLabel("m="))
        self.input_line_m_4 = QLineEdit()
        self.layout_4_1.addWidget(self.input_line_m_4)
        self.layout_4.addLayout(self.layout_4_1)

        self.layout_4_2 = QHBoxLayout()
        self.layout_4_2.addWidget(QLabel("Решение: "))
        self.output_line_4 = QLineEdit()
        self.layout_4_2.addWidget(self.output_line_4)
        self.layout_4.addLayout(self.layout_4_2)

        self.widget4.setLayout(self.layout_4)
        self.stacked_layout.addWidget(self.widget4)
        
        # Виджет под сочетания с повторениями
        self.widget5 = QWidget()
        self.layout_5 = QVBoxLayout()
        self.layout_5_1 = QHBoxLayout()
        
        self.layout_5.addWidget(QLabel("Из n объектов будем выбирать m объектов всеми возможными способами"))

        self.layout_5_1.addWidget(QLabel("n="))
        self.input_line_n_5 = QLineEdit()
        self.layout_5_1.addWidget(self.input_line_n_5)
        self.layout_5_1.addWidget(QLabel("m="))
        self.input_line_m_5 = QLineEdit()
        self.layout_5_1.addWidget(self.input_line_m_5)
        self.layout_5.addLayout(self.layout_5_1)

        self.layout_5_2 = QHBoxLayout()
        self.layout_5_2.addWidget(QLabel("Решение: "))
        self.output_line_5 = QLineEdit()
        self.layout_5_2.addWidget(self.output_line_5)
        self.layout_5.addLayout(self.layout_5_2)

        self.widget5.setLayout(self.layout_5)
        self.stacked_layout.addWidget(self.widget5)
        
        # Виджет под сочетания без повторений
        self.widget6 = QWidget()
        self.layout_6 = QVBoxLayout()
        self.layout_6_1 = QHBoxLayout()
        
        self.layout_6.addWidget(QLabel("Из n объектов будем выбирать m объектов всеми возможными способами"))

        self.layout_6_1.addWidget(QLabel("n="))
        self.input_line_n_6 = QLineEdit()
        self.layout_6_1.addWidget(self.input_line_n_6)
        self.layout_6_1.addWidget(QLabel("m="))
        self.input_line_m_6 = QLineEdit()
        self.layout_6_1.addWidget(self.input_line_m_6)
        self.layout_6.addLayout(self.layout_6_1)

        self.layout_6_2 = QHBoxLayout()
        self.layout_6_2.addWidget(QLabel("Решение: "))
        self.output_line_6 = QLineEdit()
        self.layout_6_2.addWidget(self.output_line_6)
        self.layout_6.addLayout(self.layout_6_2)

        self.widget6.setLayout(self.layout_6)
        self.stacked_layout.addWidget(self.widget6)

        # Виджет под перестановку с повторениями
        self.widget7 = QWidget()
        self.layout_7 = QVBoxLayout()
        
        self.layout_7.addWidget(QLabel("Введите количество объектов каждого типа через запятую"))

        self.layout_7_2 = QHBoxLayout()
        self.layout_7_2.addWidget(QLabel("(n1, n2, ..., nk): "))
        self.input_line_n_7 = QLineEdit()
        self.layout_7_2.addWidget(self.input_line_n_7)
        self.layout_7.addLayout(self.layout_7_2)

        self.layout_7_3 = QHBoxLayout()
        self.layout_7_3.addWidget(QLabel("Решение: "))
        self.output_line_7 = QLineEdit()
        self.layout_7_3.addWidget(self.output_line_7)
        self.layout_7.addLayout(self.layout_7_3)

        self.widget7.setLayout(self.layout_7)
        self.stacked_layout.addWidget(self.widget7)
        
        # Виджет под перестановку без повторений
        self.widget8 = QWidget()
        self.layout_8 = QVBoxLayout()
        self.layout_8_1 = QHBoxLayout()
        
        self.layout_8.addWidget(QLabel("Введите количество n различных объектов"))

        self.layout_8_1.addWidget(QLabel("n="))
        self.input_line_n_8 = QLineEdit()
        self.layout_8_1.addWidget(self.input_line_n_8)
        self.layout_8.addLayout(self.layout_8_1)

        self.layout_8_2 = QHBoxLayout()
        self.layout_8_2.addWidget(QLabel("Решение: "))
        self.output_line_8 = QLineEdit()
        self.layout_8_2.addWidget(self.output_line_8)
        self.layout_8.addLayout(self.layout_8_2)

        self.widget8.setLayout(self.layout_8)
        self.stacked_layout.addWidget(self.widget8)

        
        self.system_combo_box = QComboBox()
        self.system_combo_box.addItems([
            "-",
            "Правило суммы",
            "Правило умножения",
            "Размещение с повторениями",
            "Размещение без повторений",
            "Сочетание с повторениями",
            "Сочетание без повторений",
            "Перестановка с повторениями",
            "Перестановки без повторений"
        ])
        self.system_combo_box.activated.connect(self.stacked_layout.setCurrentIndex)
        self.layout.addWidget(self.system_combo_box)
        self.layout.addLayout(self.stacked_layout)

        self.buttons_layout = QVBoxLayout()
        self.layout.addLayout(self.buttons_layout)
        self.create_numbers()
        

    def create_numbers(self):
        buttons = [
            ('='),
            ('7', '8', '9'),
            ('4', '5', '6'),
            ('1', '2', '3'),
            ('0', ',')
        ]

        for row in buttons:
            h_layout = QHBoxLayout()
            for label in row:
                button = QPushButton(label)
                button.clicked.connect(self.button_clicked)
                h_layout.addWidget(button)
            self.buttons_layout.addLayout(h_layout)
    

    def button_clicked(self):
        button = self.sender()
        label = button.text()
        if self.system_combo_box.currentIndex() == 1: # Правило суммы
            current_text_1 = self.input_line_n_1.text()
            if label == '=' and self.input_line_n_1.text() != '':
                text = str(self.input_line_n_1.text())
                cleaned_text = ''.join(text.split()).strip(',')
                num_of_obj = [int(x) for x in cleaned_text.split(',') if x]
                if (len(num_of_obj) - 1) == text.count(','):
                    self.output_line_1.setText(summa(num_of_obj))
                else:
                    self.output_line_1.setText("Неверное количество объектов!")
            else:
                self.input_line_n_1.setText(current_text_1 + label)
        elif self.system_combo_box.currentIndex() == 2: # Правило умножения
            current_text_2 = self.input_line_n_2.text()
            if label == '=' and self.input_line_n_2.text() != '':
                text = str(self.input_line_n_2.text())
                cleaned_text = ''.join(text.split()).strip(',')
                num_of_obj = [int(x) for x in cleaned_text.split(',') if x]
                if (len(num_of_obj) - 1) == text.count(','):
                    self.output_line_2.setText(multiplication(num_of_obj))
                else:
                    self.output_line_2.setText("Неверное количество объектов!")
            else:
                self.input_line_n_2.setText(current_text_2 + label)
        elif self.system_combo_box.currentIndex() == 3: # Размещение с повторениями
            if label == '=' and self.input_line_n_3.text() != '' and self.input_line_m_3.text() != '':
                self.output_line_3.setText(rearrangement_with(int(self.input_line_n_3.text()), int(self.input_line_m_3.text())))
            else:
                pass
        elif self.system_combo_box.currentIndex() == 4: # Размещение без повторений
            if label == '=' and self.input_line_n_4.text() != '' and self.input_line_m_4.text() != '':
                self.output_line_4.setText(rearrangement_without(int(self.input_line_n_4.text()), int(self.input_line_m_4.text())))
            else:
                pass
        elif self.system_combo_box.currentIndex() == 5: # Сочетания с повторениями
            if label == '=' and self.input_line_n_5.text() != '' and self.input_line_m_5.text() != '':
                self.output_line_5.setText(comb_with(int(self.input_line_n_5.text()), int(self.input_line_m_5.text())))
            else:
                pass
        elif self.system_combo_box.currentIndex() == 6: # Сочетания без повторений
            if label == '=' and self.input_line_n_6.text() != '' and self.input_line_m_6.text() != '':
                self.output_line_6.setText(comb_without(int(self.input_line_n_6.text()), int(self.input_line_m_6.text())))
            else:
                pass
        elif self.system_combo_box.currentIndex() == 7: # Перестановка с повторениями
            current_text_7 = self.input_line_n_7.text()
            if label == '=' and self.input_line_n_7.text() != '':
                text = str(self.input_line_n_7.text())
                cleaned_text = ''.join(text.split()).strip(',')
                num_of_obj = [int(x) for x in cleaned_text.split(',') if x]
                if (len(num_of_obj) - 1) == text.count(','):
                    self.output_line_7.setText(permutations_with(num_of_obj))
                else:
                    self.output_line_7.setText("Неверное количество объектов!")
            else:
                self.input_line_n_7.setText(current_text_7 + label)
        elif self.system_combo_box.currentIndex() == 8: # Перестановка без повторений
            current_text_8 = self.input_line_n_8.text()
            if label == '=' and self.input_line_n_8.text() != '':
                self.output_line_8.setText(permmutations_without(int(self.input_line_n_8.text())))
            else:
                self.input_line_n_8.setText(current_text_8 + label)
        else:
            pass
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Combinatorika()
    calculator.show()
    sys.exit(app.exec_())