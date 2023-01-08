import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from aut import Ui_AutorizationWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui_autorization = Ui_AutorizationWindow()
    ui_autorization.setupUi(window)
    window.show()
    sys.exit(app.exec())

