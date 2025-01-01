from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

def show_winner():
    number = randint(0, 99)
    winner.setText(str(number))
    text.setText('Победитель') #Winner

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Рандомайзер') #Randomizer
button = QPushButton('Сгенирировать') #Generate
winner = QLabel('Повторить:') #Repeat
text = QLabel('Нажми, чтобы узнать победителя') #Click to find out the winner
winner.setText('?')
line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)
main_win.move(900, 70)
main_win.resize(400, 200)
button.clicked.connect(show_winner)
main_win.show()
app.exec_()
