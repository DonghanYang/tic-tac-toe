import sys
from PyQt5.QtWidgets import QApplication

from controller import GameController
from view import GameUI


def main():
    app = QApplication(sys.argv)

    view = GameUI()
    view.show()

    GameController(view=view)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
