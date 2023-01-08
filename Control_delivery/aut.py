import psycopg2
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from mainWindow import Ui_MainWindow


#КЛАСС ОКНА АВТОРИЗАЦИИ
class Ui_AutorizationWindow(object):
    def setupUi(self, AutorizationWindow):
        # СОЗДАЕМ ПОЛЕ В КОТОРОЕ ПРИСВАИВАЕМ ОКНО АВТОРИЗАЦИИ(ЧТОБЫ ПОТОМ МОЖНО БЫЛО ЕГО ЗАКРЫТЬ ЧЕРЕЗ КОД)
        self.AutWin = AutorizationWindow

        # ЗАДАЕМ ПАРАМЕТРЫ ДЛЯ ОКНА АВТОРИЗАЦИИ
        AutorizationWindow.resize(450, 451)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AutorizationWindow.sizePolicy().hasHeightForWidth())
        AutorizationWindow.setFixedSize(QtCore.QSize(450, 451))
        AutorizationWindow.setStyleSheet("")

        # СОЗДАЕМ ЦЕНТРАЛЬНЫЙ ВИДЖЕТ НА КОТОРОМ БУДЕТ РАСПОЛАГАТЬСЯ ИНТЕРФЕЙС
        self.centralwidget = QtWidgets.QWidget(AutorizationWindow)

        # СОЗДАЕМ ФОН
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 450, 550))
        self.background.setStyleSheet("background-image: url(C:/Users/Vadim/Desktop/DataSet/fon.png);")
        self.background.setText("")

        # НАДПИСЬ АВТОРИЗАЦИИ
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 182, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(250, 250, 250);")
        self.label_2.setObjectName("label_2")

        # ПОЛЕ ДЛЯ ВВОДА ЛОГИНА
        self.login_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.login_lineEdit.setGeometry(QtCore.QRect(90, 120, 270, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.login_lineEdit.setFont(font)
        self.login_lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                          "border: none;\n"
                                          "border-bottom: 2px solid rgba(255, 255, 255, 150);\n"
                                          "color:  rgb(250, 250, 250);\n"
                                          "padding-bottom: 7px;")

        # ПОЛЕ ДЛЯ ВВОДА ПАРОЛЯ
        self.pass_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_lineEdit.setGeometry(QtCore.QRect(90, 200, 270, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pass_lineEdit.setFont(font)
        self.pass_lineEdit.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
                                         "border: none;\n"
                                         "border-bottom: 2px solid rgba(255, 255, 255, 150);\n"
                                         "color:  rgb(250, 250, 250);\n"
                                         "padding-bottom: 7px;")

        # КНОПКА ДЛЯ ВХОДА
        self.input_btn = QtWidgets.QPushButton(self.centralwidget)
        self.input_btn.setGeometry(QtCore.QRect(90, 320, 270, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.input_btn.setFont(font)
        self.input_btn.setStyleSheet("background-color:rgb(250, 250, 250);\n"
                                     "color: rgb(42, 103, 156);")
        self.input_btn.clicked.connect(self.openNewWindow)

        # УСТАНАВЛИВАЕМ ЦЕНТРАЛЬНЫЙ ВИДЖЕТ
        AutorizationWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(AutorizationWindow)
        QtCore.QMetaObject.connectSlotsByName(AutorizationWindow)

    # ФУНКИЯ ДЛЯ ПРИСВАИВАНИЯ ОБЪЕКТАМ ИМЕН
    def retranslateUi(self, AutorizationWindow):
        _translate = QtCore.QCoreApplication.translate
        AutorizationWindow.setWindowTitle(_translate("AutorizationWindow", "ControlDelivery"))
        self.label_2.setText(_translate("AutorizationWindow", "Авторизация"))
        self.login_lineEdit.setPlaceholderText(_translate("AutorizationWindow", "Login"))
        self.pass_lineEdit.setPlaceholderText(_translate("AutorizationWindow", "Password"))
        self.input_btn.setText(_translate("AutorizationWindow", "ВХОД"))

    # ФУНКЦИЯ ДЛЯ ОТКРЫТИЯ ОСНОВНОГО ОКНА
    def openNewWindow(self):
        login = self.login_lineEdit.text().strip()
        passw = self.pass_lineEdit.text().strip()
        if (login != '') and (passw != ''):
            try:
                if check(login) and check(passw):
                    conn = psycopg2.connect(user=login,
                                            password=passw,
                                            host="localhost",
                                            port="5432",
                                            database="delivery_sys")
                    conn.autocommit = True
                    self.window = QMainWindow()
                    self.ui = Ui_MainWindow()
                    self.ui.setupUi(self.window, login, conn)
                    self.window.show()
                    self.AutWin.close()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректно введены данные!!!')
                    msg.exec()
            except:
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText('Не удалось подключиться к базе данных')
                msg.exec()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Ошибка')
            msg.setText('Все поля должны быть заполнены!!!')
            msg.exec()


#ФУНКЦИЯ ДЛЯ ПРОВЕРКИ ПОЛЯ НА ИНЪЕКЦИЮ
def check(txt):
    listS = ["'", '-', '--', '/', '|', '*', '%', '#', '!', '?']
    return not any(symbol in txt for symbol in listS)