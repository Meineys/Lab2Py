import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget


class Contacts(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Записная книжка')
        self.resize(350, 400)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        self.fio = QLineEdit()
        self.num = QLineEdit()

        hbox.addWidget(self.fio)
        hbox.addWidget(self.num)
        vbox.addLayout(hbox)

        self.btn = QPushButton('Добавить контакт')
        self.btn.clicked.connect(self.add_item)
        vbox.addWidget(self.btn)

        self.lst = QListWidget()
        vbox.addWidget(self.lst)

        self.setLayout(vbox)

    def add_item(self):
        n = self.fio.text().strip()
        p = self.num.text().strip()
        if n and p:
            self.lst.addItem(f"{n}: {p}")
            self.fio.clear()
            self.num.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Contacts()
    ex.show()
    sys.exit(app.exec())