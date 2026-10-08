import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class Nim(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Псевдоним')
        self.resize(300, 200)

        lay = QVBoxLayout()

        self.lbl1 = QLabel('Сколько камней в куче (от 5):')
        lay.addWidget(self.lbl1)

        self.start_val = QLineEdit()
        lay.addWidget(self.start_val)

        self.start_btn = QPushButton('Начать')
        self.start_btn.clicked.connect(self.start)
        lay.addWidget(self.start_btn)

        self.info = QLabel('')
        lay.addWidget(self.info)

        self.turn_val = QLineEdit()
        lay.addWidget(self.turn_val)

        self.turn_btn = QPushButton('Ходить')
        self.turn_btn.clicked.connect(self.turn)
        self.turn_btn.setEnabled(False)
        lay.addWidget(self.turn_btn)

        self.setLayout(lay)
        self.count = 0

    def start(self):
        try:
            v = int(self.start_val.text())
            if v >= 5:
                self.count = v
                self.info.setText(f"Камней: {self.count}. Твой ход!")
                self.turn_btn.setEnabled(True)
                self.start_val.setEnabled(False)
                self.start_btn.setEnabled(False)
        except:
            pass

    def turn(self):
        try:
            t = int(self.turn_val.text())
            if 1 <= t <= 3 and t <= self.count:
                self.count -= t
                self.turn_val.clear()

                if self.count == 0:
                    QMessageBox.information(self, "Ура", "Победа!")
                    self.reset()
                    return

                c = (self.count - 1) % 4
                if c == 0:
                    c = 1
                elif c > 3:
                    c = 3

                self.count -= c
                if self.count <= 0:
                    self.info.setText("Камней: 0")
                    QMessageBox.information(self, "Увы", "Компьютер выиграл!")
                    self.reset()
                    return

                self.info.setText(f"Комп взял {c}. Осталось: {self.count}. Твой ход!")
        except:
            pass

    def reset(self):
        self.count = 0
        self.info.setText("")
        self.start_val.clear()
        self.start_val.setEnabled(True)
        self.start_btn.setEnabled(True)
        self.turn_btn.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Nim()
    ex.show()
    sys.exit(app.exec())