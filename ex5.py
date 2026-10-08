import sys
import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QDoubleSpinBox, \
    QPlainTextEdit, QPushButton, QLabel


class AntiPlag(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Антиплагиат')
        self.resize(600, 450)

        w = QWidget()
        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(QLabel('Порог (%):'))
        self.spin = QDoubleSpinBox()
        self.spin.setRange(0, 100)
        self.spin.setValue(50)
        hbox1.addWidget(self.spin)
        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()
        self.t1 = QPlainTextEdit()
        self.t2 = QPlainTextEdit()
        hbox2.addWidget(self.t1)
        hbox2.addWidget(self.t2)
        vbox.addLayout(hbox2)

        self.btn = QPushButton('Проверить')
        self.btn.clicked.connect(self.check)
        vbox.addWidget(self.btn)

        w.setLayout(vbox)
        self.setCentralWidget(w)

        self.statusBar().showMessage('Ожидание...')

    def check(self):
        text1_words = set(re.findall(r'\w+', self.t1.toPlainText().lower()))
        text2_words = set(re.findall(r'\w+', self.t2.toPlainText().lower()))

        if not text1_words or not text2_words:
            sim = 0
        else:
            inter = text1_words.intersection(text2_words)
            sim = (len(inter) / max(len(text1_words), len(text2_words))) * 100

        limit = self.spin.value()
        self.statusBar().showMessage(f"Схожесть: {sim:.2f}% (Порог: {limit}%)")

        if sim >= limit:
            self.statusBar().setStyleSheet("background-color: #ffcccc; color: red;")
        else:
            self.statusBar().setStyleSheet("background-color: #ccffcc; color: green;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlag()
    ex.show()
    sys.exit(app.exec())