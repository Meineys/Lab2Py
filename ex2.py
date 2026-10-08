import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QCalendarWidget, QTimeEdit, \
    QPushButton, QListWidget
from PyQt6.QtCore import QDateTime


class Diary(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ежедневник')
        self.resize(600, 400)

        main_lay = QHBoxLayout()
        left_lay = QVBoxLayout()

        self.title_input = QLineEdit()
        left_lay.addWidget(self.title_input)

        self.cal = QCalendarWidget()
        left_lay.addWidget(self.cal)

        self.time_picker = QTimeEdit()
        left_lay.addWidget(self.time_picker)

        self.add_btn = QPushButton('Добавить')
        self.add_btn.clicked.connect(self.save_event)
        left_lay.addWidget(self.add_btn)

        main_lay.addLayout(left_lay)

        self.list_w = QListWidget()
        main_lay.addWidget(self.list_w)

        self.setLayout(main_lay)
        self.data = []

    def save_event(self):
        txt = self.title_input.text().strip()
        if not txt:
            return

        dt = QDateTime(self.cal.selectedDate(), self.time_picker.time())
        self.data.append((dt, txt))
        self.data.sort(key=lambda x: x[0])

        self.list_w.clear()
        for d, t in self.data:
            self.list_w.addItem(f"{d.toString('yyyy-MM-dd HH:mm')} — {t}")

        self.title_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Diary()
    ex.show()
    sys.exit(app.exec())