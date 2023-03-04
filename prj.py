import sys

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QPushButton, QLabel, QLineEdit


class Calc(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.v_box = QVBoxLayout()
        self.h_row = QHBoxLayout()
        self.setWindowTitle('Super Calculator')

        self.eval_edit = QLineEdit('0')
        self.v_box.addWidget(self.eval_edit)
        
        self.result_label = QLabel()
        self.v_box.addWidget(self.result_label)

        self.btn=[
            ['C','(',')','/'],
            ['7','8','9','*'],
            ['4','5','6','-'],
            ['1','2','3','+'],
            ['←','0','.','=']
        ]

        for i in range(len(self.btn)):
            h_box = QHBoxLayout()
            for j in range(len(self.btn[i])):
                self.btn[i][j] = QPushButton(self.btn[i][j])
                h_box.addWidget(self.btn[i][j])
            self.v_box.addLayout(h_box)

        self.setLayout(self.v_box)
        self.show()

app = QApplication(sys.argv)
win = Calc()
sys.exit(app.exec())

#just interest