from PyQt5.QtWidgets import QApplication , QWidget , QLabel , QPushButton , QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication([])

window = QWidget()
window.resize(500,300)
window.setWindowTitle("Генератор")

winner_lbl = QLabel("Натисни щоб дізнатися переможця")
num_lbl = QLabel ('?')
btn_ok = QPushButton ("Згенерувати")
vl = QVBoxLayout()
vl.addWidget(winner_lbl, alignment = Qt.AlignCenter)
vl.addWidget(num_lbl, alignment = Qt.AlignCenter)
vl.addWidget(btn_ok, alignment = Qt.AlignCenter)

window.setLayout(vl)


















window.show()
app.exec_()