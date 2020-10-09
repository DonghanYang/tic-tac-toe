from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QVBoxLayout


class GameUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300, 350)

        self._general_layout = QVBoxLayout()
        self._central_widget = QWidget(self)

        self._central_widget.setLayout(self._general_layout)
        self.setCentralWidget(self._central_widget)
        self._central_widget.layout().setContentsMargins(0, 0, 0, 0)
        self._central_widget.layout().setSpacing(0)

        self._display = None
        self._buttons = {}
        self._create_display()
        self._create_buttons()

    def _create_display(self):
        self._display = QLabel("X")
        self._display.setFont(QFont("Arial", 15))

        self._display.setFixedHeight(50)
        self._display.setAlignment(Qt.AlignCenter)

        self._general_layout.addWidget(self._display)

    def _create_buttons(self):
        buttons_layout = QGridLayout()
        buttons = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        for pos in buttons:
            self._buttons[pos] = QPushButton("")
            self._buttons[pos].setFont(QFont("Arial", 15))
            self._buttons[pos].setFixedSize(100, 100)
            buttons_layout.addWidget(self._buttons[pos], pos[0], pos[1])
        self._general_layout.addLayout(buttons_layout)

    @property
    def buttons(self):
        return self._buttons

    @property
    def display_text(self):
        return self._display.text()

    def set_display_text(self, text):
        self._display.setText(text)

    def clear_display(self):
        self.set_display_text("")

    def clear_button_text(self):
        for i in self._buttons:
            self._buttons[i].setText('')
