import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QMessageBox, \
    QGroupBox


class FlagApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Текстовый флаг')
        self.setFixedSize(400, 320)

        main_vbox = QVBoxLayout()
        colors = ['Красный', 'Зеленый', 'Белый', 'Синий', 'Желтый']
        self.all_radios = []

        for i in range(3):
            box = QGroupBox(f'Полоса {i + 1}')
            hbox = QHBoxLayout()
            rbs = []
            for c in colors:
                rb = QRadioButton(c)
                if c == colors[i]:
                    rb.setChecked(True)
                rbs.append(rb)
                hbox.addWidget(rb)
            box.setLayout(hbox)
            main_vbox.addWidget(box)
            self.all_radios.append(rbs)

        self.draw_btn = QPushButton('Нарисовать')
        self.draw_btn.clicked.connect(self.show_result)
        main_vbox.addWidget(self.draw_btn)

        self.setLayout(main_vbox)

    def show_result(self):
        res = []
        for rbs in self.all_radios:
            for rb in rbs:
                if rb.isChecked():
                    res.append(rb.text())
                    break
        QMessageBox.information(self, "Результат", f"Флаг: {', '.join(res)}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagApp()
    ex.show()
    sys.exit(app.exec())