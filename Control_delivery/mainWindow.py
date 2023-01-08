from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


#КЛАСС ОСНОВНОГО ОКНА
class Ui_MainWindow(object):
    def setupUi(self, MainWindow, login, conn):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1198, 724)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setFixedSize(QtCore.QSize(1198, 724))

        self.conn = conn
        self.user_login = login
        self.user_pos = self.get_user_position()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1201, 711))
        self.label.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1201, 51))
        self.label_2.setStyleSheet("background-color: rgb(235, 235, 235);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(440, 0, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(39, 39, 39);")
        self.label_3.setObjectName("label_3")

        self.mainTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabWidget.setGeometry(QtCore.QRect(10, 60, 1191, 651))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.mainTabWidget.setFont(font)
        self.mainTabWidget.setAutoFillBackground(False)
        self.mainTabWidget.setStyleSheet("background: transparent;\n"
"font: 75 14pt \"Cambria\";\n"
"background-color: rgb(77, 77, 77);\n"
"border-color: rgb(77, 77, 77);")
        self.mainTabWidget.setObjectName("mainTabWidget")

        self.tables_tab = QtWidgets.QWidget()
        self.tables_tab.setObjectName("tables_tab")

        self.tableTabWidget = QtWidgets.QTabWidget(self.tables_tab)
        self.tableTabWidget.setGeometry(QtCore.QRect(0, 30, 861, 591))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tableTabWidget.setFont(font)
        self.tableTabWidget.setStyleSheet("font: 75 14pt \"Calibri\";\n"
"color: rgb(22, 22, 22);\n"
"")
        self.tableTabWidget.setObjectName("tableTabWidget")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.task_table = QtWidgets.QTableWidget(self.tab_3)
        self.task_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.task_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.task_table.setObjectName("task_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.task_table.setFont(font)
        self.task_table.setColumnCount(7)
        self.task_table.setHorizontalHeaderLabels(['ID', 'Condition', 'Metros', 'Start_date',
                                                    'Close_date', 'Execution_date', 'User_id'])
        self.task_table.verticalHeader().setVisible(False)
        self.task_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadTaskTable()

        self.tableTabWidget.addTab(self.tab_3, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.metro_table = QtWidgets.QTableWidget(self.tab_5)
        self.metro_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.metro_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.metro_table.setObjectName("metro_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.metro_table.setFont(font)
        self.metro_table.setColumnCount(4)
        self.metro_table.setHorizontalHeaderLabels(['ID', 'Name', 'BC_id', 'Condition'])
        self.metro_table.verticalHeader().setVisible(False)
        self.metro_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadMetroTable()

        self.tableTabWidget.addTab(self.tab_5, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.BC_table = QtWidgets.QTableWidget(self.tab_4)
        self.BC_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.BC_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.BC_table.setObjectName("BC_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BC_table.setFont(font)
        self.BC_table.setColumnCount(6)
        self.BC_table.setHorizontalHeaderLabels(['ID', 'Name', 'Address', 'Passes', 'Client_id', 'Metro_id'])
        self.BC_table.verticalHeader().setVisible(False)
        self.BC_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadBCTable()

        self.tableTabWidget.addTab(self.tab_4, "")

        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")

        self.client_table = QtWidgets.QTableWidget(self.tab_6)
        self.client_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.client_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.client_table.setObjectName("client_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.client_table.setFont(font)
        self.client_table.setColumnCount(4)
        self.client_table.setHorizontalHeaderLabels(['ID', 'Type', 'Name', 'BC_id'])
        self.client_table.verticalHeader().setVisible(False)
        self.client_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadClientTable()

        self.tableTabWidget.addTab(self.tab_6, "")

        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")

        self.company_table = QtWidgets.QTableWidget(self.tab_7)
        self.company_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.company_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.company_table.setObjectName("company_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.company_table.setFont(font)
        self.company_table.setColumnCount(9)
        self.company_table.setHorizontalHeaderLabels(['ID', 'Name', 'Office', 'Contacts_id', 'Call_ahead', 'Contract_id', 'Contract_received', 'Description', 'BC_id'])
        self.company_table.verticalHeader().setVisible(False)
        self.company_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadCompanyTable()

        self.tableTabWidget.addTab(self.tab_7, "")

        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")

        self.ie_table = QtWidgets.QTableWidget(self.tab_8)
        self.ie_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.ie_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ie_table.setObjectName("ie_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ie_table.setFont(font)
        self.ie_table.setColumnCount(10)
        self.ie_table.setHorizontalHeaderLabels(
                ['ID', 'fName', 'lName', 'Phone', 'Contract_id', 'Office', 'Call_ahead', 'Contract_received', 'Description',
                 'BC_id'])
        self.ie_table.verticalHeader().setVisible(False)
        self.ie_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadIETable()

        self.tableTabWidget.addTab(self.tab_8, "")

        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")

        self.dds_table = QtWidgets.QTableWidget(self.tab_9)
        self.dds_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.dds_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.dds_table.setObjectName("dds_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dds_table.setFont(font)
        self.dds_table.setColumnCount(3)
        self.dds_table.setHorizontalHeaderLabels(
                ['ID', 'Dates', 'Client_id'])
        self.dds_table.verticalHeader().setVisible(False)
        self.dds_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadDDSTable()

        self.tableTabWidget.addTab(self.tab_9, "")

        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")

        self.contact_table = QtWidgets.QTableWidget(self.tab_10)
        self.contact_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.contact_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contact_table.setObjectName("contact_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contact_table.setFont(font)
        self.contact_table.setColumnCount(5)
        self.contact_table.setHorizontalHeaderLabels(
                ['ID', 'fName', 'lName', 'Phone', 'Company_id'])
        self.contact_table.verticalHeader().setVisible(False)
        self.contact_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadContactTable()

        self.tableTabWidget.addTab(self.tab_10, "")

        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")

        self.contract_table = QtWidgets.QTableWidget(self.tab_11)
        self.contract_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.contract_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contract_table.setObjectName("contract_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contract_table.setFont(font)
        self.contract_table.setColumnCount(3)
        self.contract_table.setHorizontalHeaderLabels(
                ['ID', 'Num', 'Service_id'])
        self.contract_table.verticalHeader().setVisible(False)
        self.contract_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadContractTable()

        self.tableTabWidget.addTab(self.tab_11, "")

        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")

        self.service_table = QtWidgets.QTableWidget(self.tab_12)
        self.service_table.setGeometry(QtCore.QRect(0, 0, 856, 521))
        self.service_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.service_table.setObjectName("client_type_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.service_table.setFont(font)
        self.service_table.setColumnCount(2)
        self.service_table.setHorizontalHeaderLabels(
                ['ID', 'Name'])
        self.service_table.verticalHeader().setVisible(False)
        self.service_table.horizontalHeader().setSortIndicatorShown(True)
        self.loadServiceTable()

        self.tableTabWidget.addTab(self.tab_12, "")

        self.label_4 = QtWidgets.QLabel(self.tables_tab)
        self.label_4.setGeometry(QtCore.QRect(859, 60, 2, 561))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.widget_2 = QtWidgets.QWidget(self.tables_tab)
        self.widget_2.setGeometry(QtCore.QRect(870, 40, 311, 191))
        self.widget_2.setObjectName("widget_2")

        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(0, 30, 311, 151))
        self.label_6.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")

        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 13pt \"Impact\";")
        self.label_5.setObjectName("label_5")

        self.completed_task_Widget = QtWidgets.QWidget(self.widget_2)
        self.completed_task_Widget.setGeometry(QtCore.QRect(10, 100, 291, 71))
        self.completed_task_Widget.setStyleSheet("border-color: rgb(208, 208, 208);")
        self.completed_task_Widget.setObjectName("completed_task_Widget")
        self.completed_task_spinBox = QtWidgets.QSpinBox(self.completed_task_Widget)
        self.completed_task_spinBox.setGeometry(QtCore.QRect(20, 10, 101, 51))
        self.completed_task_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.completed_task_spinBox.setObjectName("completed_task_spinBox")

        self.completed_task_btn = QtWidgets.QPushButton(self.completed_task_Widget)
        self.completed_task_btn.setGeometry(QtCore.QRect(150, 10, 111, 51))
        self.completed_task_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.completed_task_btn.setObjectName("completed_task_btn")
        self.completed_task_btn.clicked.connect(self.completed_task)

        self.widget = QtWidgets.QWidget(self.tables_tab)
        self.widget.setGeometry(QtCore.QRect(870, 220, 311, 171))
        self.widget.setObjectName("widget")

        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(0, 20, 311, 151))
        self.label_7.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(47, 30, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 13pt \"Impact\";")
        self.label_8.setObjectName("label_8")

        self.ready_metro_Widget = QtWidgets.QWidget(self.widget)
        self.ready_metro_Widget.setGeometry(QtCore.QRect(20, 90, 261, 71))
        self.ready_metro_Widget.setStyleSheet("border-color: rgb(208, 208, 208);")
        self.ready_metro_Widget.setObjectName("ready_metro_Widget")

        self.ready_metro_spinBox = QtWidgets.QSpinBox(self.ready_metro_Widget)
        self.ready_metro_spinBox.setGeometry(QtCore.QRect(20, 10, 101, 51))
        self.ready_metro_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ready_metro_spinBox.setObjectName("ready_metro_spinBox")

        self.ready_metro_btn = QtWidgets.QPushButton(self.ready_metro_Widget)
        self.ready_metro_btn.setGeometry(QtCore.QRect(150, 10, 111, 51))
        self.ready_metro_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.ready_metro_btn.setObjectName("ready_metro_btn")
        self.ready_metro_btn.clicked.connect(self.ready_metro)

        self.label_9 = QtWidgets.QLabel(self.tables_tab)
        self.label_9.setGeometry(QtCore.QRect(1, 2, 1180, 21))
        self.label_9.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_9.setObjectName("label_9")

        self.widget_3 = QtWidgets.QWidget(self.tables_tab)
        self.widget_3.setGeometry(QtCore.QRect(860, 400, 321, 191))
        self.widget_3.setObjectName("widget_3")

        self.label_10 = QtWidgets.QLabel(self.widget_3)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 311, 161))
        self.label_10.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")

        self.clear_task_btn = QtWidgets.QPushButton(self.widget_3)
        self.clear_task_btn.setGeometry(QtCore.QRect(60, 100, 211, 51))
        self.clear_task_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.clear_task_btn.setObjectName("clear_task_btn")
        self.clear_task_btn.clicked.connect(self.clear_task)

        self.update_tables_btn = QtWidgets.QPushButton(self.widget_3)
        self.update_tables_btn.setGeometry(QtCore.QRect(60, 30, 211, 51))
        self.update_tables_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.update_tables_btn.setObjectName("update_tables_btn")
        self.update_tables_btn.clicked.connect(self.update_tables)

        self.mainTabWidget.addTab(self.tables_tab, "")

        self.create_update_tab = QtWidgets.QWidget()
        self.create_update_tab.setObjectName("create_update_tab")

        self.label_11 = QtWidgets.QLabel(self.create_update_tab)
        self.label_11.setGeometry(QtCore.QRect(1, 2, 1180, 21))
        self.label_11.setStyleSheet("color: rgb(240, 240, 240);")
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.create_update_tab)
        self.label_12.setGeometry(QtCore.QRect(0, 30, 1181, 577))
        self.label_12.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")

        self.create_update_tabWidget = QtWidgets.QTabWidget(self.create_update_tab)
        self.create_update_tabWidget.setGeometry(QtCore.QRect(215, 40, 751, 567))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.create_update_tabWidget.setFont(font)
        self.create_update_tabWidget.setStyleSheet("font: 75 20pt \"Cambria\";")
        self.create_update_tabWidget.setObjectName("create_update_tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(160, 120, 441, 321))
        self.label_13.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")

        self.name_metro_plainTextEdit = QtWidgets.QLineEdit(self.tab)
        self.name_metro_plainTextEdit.setGeometry(QtCore.QRect(240, 150, 291, 51))
        self.name_metro_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.name_metro_plainTextEdit.setObjectName("name_metro_plainTextEdit")

        self.create_metro_btn = QtWidgets.QPushButton(self.tab)
        self.create_metro_btn.setGeometry(QtCore.QRect(190, 330, 171, 61))
        self.create_metro_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.create_metro_btn.setObjectName("create_metro_btn")
        self.create_metro_btn.clicked.connect(self.create_metro)

        self.change_metro_btn = QtWidgets.QPushButton(self.tab)
        self.change_metro_btn.setGeometry(QtCore.QRect(400, 330, 171, 61))
        self.change_metro_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.change_metro_btn.setObjectName("change_metro_btn")
        self.change_metro_btn.clicked.connect(self.update_metro)

        self.id_metro_spinBox = QtWidgets.QSpinBox(self.tab)
        self.id_metro_spinBox.setGeometry(QtCore.QRect(340, 245, 101, 41))
        self.id_metro_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id_metro_spinBox.setObjectName("id_metro_spinBox")

        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(300, 240, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_15.setObjectName("label_15")

        self.label_30 = QtWidgets.QLabel(self.tab)
        self.label_30.setGeometry(QtCore.QRect(540, 140, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_30.setObjectName("label_30")

        self.create_update_tabWidget.addTab(self.tab, "")

        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")

        self.label_14 = QtWidgets.QLabel(self.tab_13)
        self.label_14.setGeometry(QtCore.QRect(130, 30, 501, 471))
        self.label_14.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")

        self.name_bc_plainTextEdit = QtWidgets.QLineEdit(self.tab_13)
        self.name_bc_plainTextEdit.setGeometry(QtCore.QRect(240, 60, 291, 51))
        self.name_bc_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.name_bc_plainTextEdit.setObjectName("name_bc_plainTextEdit")

        self.address_bc_plainTextEdit = QtWidgets.QLineEdit(self.tab_13)
        self.address_bc_plainTextEdit.setGeometry(QtCore.QRect(240, 130, 291, 51))
        self.address_bc_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.address_bc_plainTextEdit.setObjectName("address_bc_plainTextEdit")

        self.passes_bc_checkBox = QtWidgets.QCheckBox(self.tab_13)
        self.passes_bc_checkBox.setGeometry(QtCore.QRect(270, 200, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.passes_bc_checkBox.setFont(font)
        self.passes_bc_checkBox.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 14pt \"Courier\";\n"
"")
        self.passes_bc_checkBox.setObjectName("passes_bc_checkBox")

        self.create_bc_btn = QtWidgets.QPushButton(self.tab_13)
        self.create_bc_btn.setGeometry(QtCore.QRect(190, 410, 171, 61))
        self.create_bc_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.create_bc_btn.setObjectName("create_bc_btn")
        self.create_bc_btn.clicked.connect(self.create_BC)

        self.change_bc_btn = QtWidgets.QPushButton(self.tab_13)
        self.change_bc_btn.setGeometry(QtCore.QRect(400, 410, 171, 61))
        self.change_bc_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.change_bc_btn.setObjectName("change_bc_btn")
        self.change_bc_btn.clicked.connect(self.update_BC)

        self.label_16 = QtWidgets.QLabel(self.tab_13)
        self.label_16.setGeometry(QtCore.QRect(300, 330, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_16.setObjectName("label_16")

        self.id_bc_spinBox = QtWidgets.QSpinBox(self.tab_13)
        self.id_bc_spinBox.setGeometry(QtCore.QRect(350, 336, 101, 41))
        self.id_bc_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id_bc_spinBox.setObjectName("id_bc_spinBox")

        self.label_17 = QtWidgets.QLabel(self.tab_13)
        self.label_17.setGeometry(QtCore.QRect(234, 264, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_17.setObjectName("label_17")

        self.id_metro_bc_spinBox = QtWidgets.QSpinBox(self.tab_13)
        self.id_metro_bc_spinBox.setGeometry(QtCore.QRect(350, 270, 101, 41))
        self.id_metro_bc_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id_metro_bc_spinBox.setObjectName("id_metro_bc_spinBox")

        self.label_31 = QtWidgets.QLabel(self.tab_13)
        self.label_31.setGeometry(QtCore.QRect(540, 50, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_31.setObjectName("label_31")

        self.label_32 = QtWidgets.QLabel(self.tab_13)
        self.label_32.setGeometry(QtCore.QRect(540, 120, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_32.setObjectName("label_32")

        self.label_33 = QtWidgets.QLabel(self.tab_13)
        self.label_33.setGeometry(QtCore.QRect(520, 200, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_33.setObjectName("label_33")

        self.create_update_tabWidget.addTab(self.tab_13, "")

        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")

        self.label_18 = QtWidgets.QLabel(self.tab_15)
        self.label_18.setGeometry(QtCore.QRect(10, 20, 721, 471))
        self.label_18.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")

        self.ie_fname_plainTextEdit = QtWidgets.QLineEdit(self.tab_15)
        self.ie_fname_plainTextEdit.setGeometry(QtCore.QRect(80, 40, 271, 51))
        self.ie_fname_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.ie_fname_plainTextEdit.setObjectName("ie_fname_plainTextEdit")

        self.ie_lname_plainTextEdit = QtWidgets.QLineEdit(self.tab_15)
        self.ie_lname_plainTextEdit.setGeometry(QtCore.QRect(380, 40, 271, 51))
        self.ie_lname_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.ie_lname_plainTextEdit.setObjectName("ie_lname_plainTextEdit")

        self.ie_phone_plainTextEdit = QtWidgets.QLineEdit(self.tab_15)
        self.ie_phone_plainTextEdit.setGeometry(QtCore.QRect(80, 120, 271, 51))
        self.ie_phone_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.ie_phone_plainTextEdit.setObjectName("ie_phone_plainTextEdit")

        self.ie_office_plainTextEdit = QtWidgets.QLineEdit(self.tab_15)
        self.ie_office_plainTextEdit.setGeometry(QtCore.QRect(380, 120, 271, 51))
        self.ie_office_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.ie_office_plainTextEdit.setObjectName("ie_office_plainTextEdit")

        self.ie_contract_id_spinBox = QtWidgets.QSpinBox(self.tab_15)
        self.ie_contract_id_spinBox.setGeometry(QtCore.QRect(550, 210, 101, 31))
        self.ie_contract_id_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ie_contract_id_spinBox.setObjectName("ie_contract_id_spinBox")

        self.label_19 = QtWidgets.QLabel(self.tab_15)
        self.label_19.setGeometry(QtCore.QRect(380, 200, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_19.setObjectName("label_19")

        self.ie_id_spinBox = QtWidgets.QSpinBox(self.tab_15)
        self.ie_id_spinBox.setGeometry(QtCore.QRect(550, 310, 101, 31))
        self.ie_id_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ie_id_spinBox.setObjectName("ie_contract_id_spinBox")

        self.label_111 = QtWidgets.QLabel(self.tab_15)
        self.label_111.setGeometry(QtCore.QRect(460, 300, 60, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_111.setFont(font)
        self.label_111.setStyleSheet("color: rgb(236, 236, 236);\n"
                                    "font: 75 18pt \"Impact\";")
        self.label_111.setObjectName("label_19")
        self.label_111.setText('ID')

        self.ie_con_rec_checkBox = QtWidgets.QCheckBox(self.tab_15)
        self.ie_con_rec_checkBox.setGeometry(QtCore.QRect(80, 280, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ie_con_rec_checkBox.setFont(font)
        self.ie_con_rec_checkBox.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";\n"
"")
        self.ie_con_rec_checkBox.setObjectName("ie_con_rec_checkBox")

        self.ie_desc_plainTextEdit = QtWidgets.QLineEdit(self.tab_15)
        self.ie_desc_plainTextEdit.setGeometry(QtCore.QRect(80, 200, 271, 51))
        self.ie_desc_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.ie_desc_plainTextEdit.setObjectName("ie_desc_plainTextEdit")

        self.ie_bc_id_spinBox_3 = QtWidgets.QSpinBox(self.tab_15)
        self.ie_bc_id_spinBox_3.setGeometry(QtCore.QRect(550, 260, 101, 31))
        self.ie_bc_id_spinBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ie_bc_id_spinBox_3.setObjectName("ie_bc_id_spinBox_3")

        self.label_20 = QtWidgets.QLabel(self.tab_15)
        self.label_20.setGeometry(QtCore.QRect(460, 250, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_20.setObjectName("label_20")

        self.create_ie_btn = QtWidgets.QPushButton(self.tab_15)
        self.create_ie_btn.setGeometry(QtCore.QRect(160, 400, 171, 61))
        self.create_ie_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.create_ie_btn.setObjectName("create_ie_btn")
        self.create_ie_btn.clicked.connect(self.create_ie)

        self.change_ie_btn_3 = QtWidgets.QPushButton(self.tab_15)
        self.change_ie_btn_3.setGeometry(QtCore.QRect(390, 400, 171, 61))
        self.change_ie_btn_3.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.change_ie_btn_3.setObjectName("change_ie_btn_3")
        self.change_ie_btn_3.clicked.connect(self.update_ie)

        self.ie_call_a_checkBox = QtWidgets.QCheckBox(self.tab_15)
        self.ie_call_a_checkBox.setGeometry(QtCore.QRect(80, 330, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ie_call_a_checkBox.setFont(font)
        self.ie_call_a_checkBox.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";\n"
"")
        self.ie_call_a_checkBox.setObjectName("ie_call_a_checkBox")

        self.label_34 = QtWidgets.QLabel(self.tab_15)
        self.label_34.setGeometry(QtCore.QRect(660, 30, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_34.setObjectName("label_34")

        self.label_35 = QtWidgets.QLabel(self.tab_15)
        self.label_35.setGeometry(QtCore.QRect(60, 30, 16, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_35.setObjectName("label_35")

        self.label_36 = QtWidgets.QLabel(self.tab_15)
        self.label_36.setGeometry(QtCore.QRect(660, 110, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_36.setFont(font)
        self.label_36.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_36.setObjectName("label_36")

        self.label_37 = QtWidgets.QLabel(self.tab_15)
        self.label_37.setGeometry(QtCore.QRect(60, 110, 16, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_37.setObjectName("label_37")

        self.label_38 = QtWidgets.QLabel(self.tab_15)
        self.label_38.setGeometry(QtCore.QRect(60, 190, 16, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_38.setObjectName("label_38")

        self.label_39 = QtWidgets.QLabel(self.tab_15)
        self.label_39.setGeometry(QtCore.QRect(310, 270, 16, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_39.setObjectName("label_39")

        self.label_40 = QtWidgets.QLabel(self.tab_15)
        self.label_40.setGeometry(QtCore.QRect(380, 310, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_40.setObjectName("label_40")

        self.create_update_tabWidget.addTab(self.tab_15, "")

        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")

        self.label_21 = QtWidgets.QLabel(self.tab_16)
        self.label_21.setGeometry(QtCore.QRect(10, 20, 721, 471))
        self.label_21.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")

        self.company_name_plainTextEdit = QtWidgets.QLineEdit(self.tab_16)
        self.company_name_plainTextEdit.setGeometry(QtCore.QRect(60, 60, 271, 51))
        self.company_name_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.company_name_plainTextEdit.setObjectName("company_name_plainTextEdit")

        self.company_office_plainTextEdit = QtWidgets.QLineEdit(self.tab_16)
        self.company_office_plainTextEdit.setGeometry(QtCore.QRect(380, 60, 271, 51))
        self.company_office_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.company_office_plainTextEdit.setObjectName("company_office_plainTextEdit")

        self.company_call_a_checkBox = QtWidgets.QCheckBox(self.tab_16)
        self.company_call_a_checkBox.setGeometry(QtCore.QRect(250, 260, 301, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.company_call_a_checkBox.setFont(font)
        self.company_call_a_checkBox.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";\n"
"")
        self.company_call_a_checkBox.setObjectName("company_call_a_checkBox")

        self.company_contract_id_spinBox = QtWidgets.QSpinBox(self.tab_16)
        self.company_contract_id_spinBox.setGeometry(QtCore.QRect(190, 320, 101, 31))
        self.company_contract_id_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.company_contract_id_spinBox.setObjectName("company_contract_id_spinBox")

        self.label_22 = QtWidgets.QLabel(self.tab_16)
        self.label_22.setGeometry(QtCore.QRect(50, 310, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_22.setObjectName("label_22")

        self.company_id_spinBox = QtWidgets.QSpinBox(self.tab_16)
        self.company_id_spinBox.setGeometry(QtCore.QRect(370, 320, 101, 31))
        self.company_id_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.company_id_spinBox.setObjectName("company_contract_id_spinBox")

        self.label_q = QtWidgets.QLabel(self.tab_16)
        self.label_q.setGeometry(QtCore.QRect(330, 310, 40, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_q.setFont(font)
        self.label_q.setStyleSheet("color: rgb(236, 236, 236);\n"
                                    "font: 75 18pt \"Impact\";")
        self.label_q.setObjectName("label_22")
        self.label_q.setText('ID')

        self.company_con_rec_checkBox = QtWidgets.QCheckBox(self.tab_16)
        self.company_con_rec_checkBox.setGeometry(QtCore.QRect(250, 210, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.company_con_rec_checkBox.setFont(font)
        self.company_con_rec_checkBox.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";\n"
"")
        self.company_con_rec_checkBox.setObjectName("company_con_rec_checkBox")

        self.company_desc_plainTextEdit = QtWidgets.QLineEdit(self.tab_16)
        self.company_desc_plainTextEdit.setGeometry(QtCore.QRect(230, 140, 271, 51))
        self.company_desc_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.company_desc_plainTextEdit.setObjectName("company_desc_plainTextEdit")

        self.label_23 = QtWidgets.QLabel(self.tab_16)
        self.label_23.setGeometry(QtCore.QRect(540, 310, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_23.setObjectName("label_23")

        self.company_bc_id_spinBox = QtWidgets.QSpinBox(self.tab_16)
        self.company_bc_id_spinBox.setGeometry(QtCore.QRect(610, 320, 101, 31))
        self.company_bc_id_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.company_bc_id_spinBox.setObjectName("company_bc_id_spinBox")

        self.create_ie_btn_2 = QtWidgets.QPushButton(self.tab_16)
        self.create_ie_btn_2.setGeometry(QtCore.QRect(160, 400, 171, 61))
        self.create_ie_btn_2.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.create_ie_btn_2.setObjectName("create_ie_btn_2")
        self.create_ie_btn_2.clicked.connect(self.create_company)

        self.change_ie_btn_4 = QtWidgets.QPushButton(self.tab_16)
        self.change_ie_btn_4.setGeometry(QtCore.QRect(390, 400, 171, 61))
        self.change_ie_btn_4.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.change_ie_btn_4.setObjectName("change_ie_btn_4")
        self.change_ie_btn_4.clicked.connect(self.update_company)

        self.label_41 = QtWidgets.QLabel(self.tab_16)
        self.label_41.setGeometry(QtCore.QRect(660, 50, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_41.setObjectName("label_41")

        self.label_42 = QtWidgets.QLabel(self.tab_16)
        self.label_42.setGeometry(QtCore.QRect(40, 50, 16, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_42.setObjectName("label_42")

        self.label_43 = QtWidgets.QLabel(self.tab_16)
        self.label_43.setGeometry(QtCore.QRect(510, 130, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_43.setObjectName("label_43")

        self.label_44 = QtWidgets.QLabel(self.tab_16)
        self.label_44.setGeometry(QtCore.QRect(480, 200, 20, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_44.setObjectName("label_44")

        self.label_45 = QtWidgets.QLabel(self.tab_16)
        self.label_45.setGeometry(QtCore.QRect(550, 240, 16, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_45.setObjectName("label_45")

        self.create_update_tabWidget.addTab(self.tab_16, "")

        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")

        self.label_24 = QtWidgets.QLabel(self.tab_17)
        self.label_24.setGeometry(QtCore.QRect(130, 30, 501, 471))
        self.label_24.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")

        self.contact_fname_plainTextEdit = QtWidgets.QLineEdit(self.tab_17)
        self.contact_fname_plainTextEdit.setGeometry(QtCore.QRect(250, 60, 271, 51))
        self.contact_fname_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.contact_fname_plainTextEdit.setObjectName("contact_fname_plainTextEdit")

        self.contact_lname_plainTextEdit = QtWidgets.QLineEdit(self.tab_17)
        self.contact_lname_plainTextEdit.setGeometry(QtCore.QRect(250, 140, 271, 51))
        self.contact_lname_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.contact_lname_plainTextEdit.setObjectName("contact_lname_plainTextEdit")

        self.contact_phone_plainTextEdit = QtWidgets.QLineEdit(self.tab_17)
        self.contact_phone_plainTextEdit.setGeometry(QtCore.QRect(250, 230, 271, 51))
        self.contact_phone_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.contact_phone_plainTextEdit.setObjectName("contact_phone_plainTextEdit")

        self.label_25 = QtWidgets.QLabel(self.tab_17)
        self.label_25.setGeometry(QtCore.QRect(260, 315, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_25.setObjectName("label_25")

        self.contact_com_id_spinBox = QtWidgets.QSpinBox(self.tab_17)
        self.contact_com_id_spinBox.setGeometry(QtCore.QRect(420, 320, 101, 41))
        self.contact_com_id_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contact_com_id_spinBox.setObjectName("contact_com_id_spinBox")

        self.create_contact_btn = QtWidgets.QPushButton(self.tab_17)
        self.create_contact_btn.setGeometry(QtCore.QRect(210, 400, 171, 61))
        self.create_contact_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.create_contact_btn.setObjectName("create_contact_btn")
        self.create_contact_btn.clicked.connect(self.create_contact)

        self.change_contact_btn = QtWidgets.QPushButton(self.tab_17)
        self.change_contact_btn.setGeometry(QtCore.QRect(400, 400, 171, 61))
        self.change_contact_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.change_contact_btn.setObjectName("change_contact_btn")
        self.change_contact_btn.clicked.connect(self.update_contact)

        self.label_46 = QtWidgets.QLabel(self.tab_17)
        self.label_46.setGeometry(QtCore.QRect(530, 50, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_46.setObjectName("label_46")

        self.label_47 = QtWidgets.QLabel(self.tab_17)
        self.label_47.setGeometry(QtCore.QRect(530, 130, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.tab_17)
        self.label_48.setGeometry(QtCore.QRect(530, 220, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_48.setObjectName("label_48")
        self.create_update_tabWidget.addTab(self.tab_17, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")


        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(40, 40, 661, 281))
        self.label_26.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.service_name_plainTextEdit = QtWidgets.QLineEdit(self.tab_2)
        self.service_name_plainTextEdit.setGeometry(QtCore.QRect(80, 60, 581, 51))
        self.service_name_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.service_name_plainTextEdit.setObjectName("service_name_plainTextEdit")

        self.service_price_spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.service_price_spinBox.setGeometry(QtCore.QRect(175, 145, 101, 41))
        self.service_price_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.service_price_spinBox.setObjectName("service_price_spinBox")

        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(150, 140, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_27.setObjectName("label_27")

        self.service_id_spinBox = QtWidgets.QSpinBox(self.tab_2)
        self.service_id_spinBox.setGeometry(QtCore.QRect(475, 145, 101, 41))
        self.service_id_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.service_id_spinBox.setObjectName("service_price_spinBox")

        self.label_777 = QtWidgets.QLabel(self.tab_2)
        self.label_777.setGeometry(QtCore.QRect(450, 140, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_777.setFont(font)
        self.label_777.setStyleSheet("color: rgb(236, 236, 236);\n"
                                    "font: 75 18pt \"Impact\";")
        self.label_777.setObjectName("label_27")
        self.label_777.setText('ID')

        self.create_service_btn = QtWidgets.QPushButton(self.tab_2)
        self.create_service_btn.setGeometry(QtCore.QRect(160, 220, 171, 61))
        self.create_service_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.create_service_btn.setObjectName("create_service_btn")
        self.create_service_btn.clicked.connect(self.create_service)

        self.change_service_btn = QtWidgets.QPushButton(self.tab_2)
        self.change_service_btn.setGeometry(QtCore.QRect(430, 220, 171, 61))
        self.change_service_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.change_service_btn.setObjectName("change_service_btn")
        self.change_service_btn.clicked.connect(self.update_service)

        self.label_49 = QtWidgets.QLabel(self.tab_2)
        self.label_49.setGeometry(QtCore.QRect(670, 50, 16, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_49.setObjectName("label_49")

        self.label_50 = QtWidgets.QLabel(self.tab_2)
        self.label_50.setGeometry(QtCore.QRect(300, 130, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_50.setFont(font)
        self.label_50.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_50.setObjectName("label_50")
        self.create_update_tabWidget.addTab(self.tab_2, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.label_28 = QtWidgets.QLabel(self.tab_18)
        self.label_28.setGeometry(QtCore.QRect(40, 40, 661, 350))
        self.label_28.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")

        self.label_100 = QtWidgets.QLabel(self.tab_18)
        self.label_100.setGeometry(QtCore.QRect(150, 190, 230, 91))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_100.setFont(font)
        self.label_100.setStyleSheet("color: rgb(236, 236, 236);\n"
                                    "font: 75 18pt \"Impact\";")
        self.label_100.setText('user ID')


        self.task_user_id_spinBox = QtWidgets.QSpinBox(self.tab_18)
        self.task_user_id_spinBox.setGeometry(QtCore.QRect(240, 210, 130, 41))
        self.task_user_id_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.task_user_id_spinBox.setObjectName("service_price_spinBox")


        self.task_id_spinBox = QtWidgets.QSpinBox(self.tab_18)
        self.task_id_spinBox.setGeometry(QtCore.QRect(490, 210, 130, 41))
        self.task_id_spinBox.setStyleSheet("background-color: rgb(255, 255, 255);")

        self.label_555 = QtWidgets.QLabel(self.tab_18)
        self.label_555.setGeometry(QtCore.QRect(450, 190, 40, 91))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_555.setFont(font)
        self.label_555.setStyleSheet("color: rgb(236, 236, 236);\n"
                                     "font: 75 18pt \"Impact\";")
        self.label_555.setText('ID')


        self.task_metros_is_plainTextEdit = QtWidgets.QLineEdit(self.tab_18)
        self.task_metros_is_plainTextEdit.setGeometry(QtCore.QRect(80, 60, 581, 51))
        self.task_metros_is_plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.task_metros_is_plainTextEdit.setObjectName("task_metros_is_plainTextEdit")

        self.task_close_date_dateEdit = QtWidgets.QDateEdit(self.tab_18)
        self.task_close_date_dateEdit.setGeometry(QtCore.QRect(380, 150, 191, 41))
        self.task_close_date_dateEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.task_close_date_dateEdit.setObjectName("task_close_date_dateEdit")

        self.label_29 = QtWidgets.QLabel(self.tab_18)
        self.label_29.setGeometry(QtCore.QRect(180, 145, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_29.setObjectName("label_29")

        self.create_task_btn = QtWidgets.QPushButton(self.tab_18)
        self.create_task_btn.setGeometry(QtCore.QRect(160, 290, 171, 61))
        self.create_task_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.create_task_btn.setObjectName("create_task_btn")
        self.create_task_btn.clicked.connect(self.create_task)

        self.change_task_btn = QtWidgets.QPushButton(self.tab_18)
        self.change_task_btn.setGeometry(QtCore.QRect(430, 290, 171, 61))
        self.change_task_btn.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.change_task_btn.setObjectName("change_task_btn")
        self.change_task_btn.clicked.connect(self.update_task)

        self.label_51 = QtWidgets.QLabel(self.tab_18)
        self.label_51.setGeometry(QtCore.QRect(580, 140, 16, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_51.setObjectName("label_51")

        self.label_52 = QtWidgets.QLabel(self.tab_18)
        self.label_52.setGeometry(QtCore.QRect(670, 50, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 25pt \"Impact\";")
        self.label_52.setObjectName("label_52")

        self.create_update_tabWidget.addTab(self.tab_18, "")

        self.label_54 = QtWidgets.QLabel(self.create_update_tab)
        self.label_54.setGeometry(QtCore.QRect(960, 70, 6, 535))
        self.label_54.setText("")
        self.label_54.setObjectName("label_54")

        self.label_59 = QtWidgets.QLabel(self.create_update_tab)
        self.label_59.setGeometry(QtCore.QRect(10, 265, 191, 81))
        self.label_59.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_59.setText("")
        self.label_59.setObjectName("label_59")

        self.label_60 = QtWidgets.QLabel(self.create_update_tab)
        self.label_60.setGeometry(QtCore.QRect(20, 280, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_60.setFont(font)
        self.label_60.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 15pt \"Impact\";")
        self.label_60.setObjectName("label_60")

        self.label_61 = QtWidgets.QLabel(self.create_update_tab)
        self.label_61.setGeometry(QtCore.QRect(960, 210, 211, 141))
        self.label_61.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_61.setText("")
        self.label_61.setObjectName("label_61")

        self.label_62 = QtWidgets.QLabel(self.create_update_tab)
        self.label_62.setGeometry(QtCore.QRect(970, 250, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_62.setFont(font)
        self.label_62.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 15pt \"Impact\";")
        self.label_62.setObjectName("label_62")

        self.label_63 = QtWidgets.QLabel(self.create_update_tab)
        self.label_63.setGeometry(QtCore.QRect(970, 290, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_63.setFont(font)
        self.label_63.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 11pt \"Impact\";")
        self.label_63.setObjectName("label_63")

        self.label_64 = QtWidgets.QLabel(self.create_update_tab)
        self.label_64.setGeometry(QtCore.QRect(970, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_64.setFont(font)
        self.label_64.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 15pt \"Impact\";")
        self.label_64.setObjectName("label_64")

        self.label_65 = QtWidgets.QLabel(self.create_update_tab)
        self.label_65.setGeometry(QtCore.QRect(980, 220, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_65.setFont(font)
        self.label_65.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 16pt \"Impact\";")
        self.label_65.setObjectName("label_65")

        self.mainTabWidget.addTab(self.create_update_tab, "")

        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")

        self.label_53 = QtWidgets.QLabel(self.tab_14)
        self.label_53.setGeometry(QtCore.QRect(20, 30, 1141, 551))
        self.label_53.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_53.setText("")
        self.label_53.setObjectName("label_53")

        self.label_55 = QtWidgets.QLabel(self.tab_14)
        self.label_55.setGeometry(QtCore.QRect(80, 100, 531, 411))
        self.label_55.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_55.setText("")
        self.label_55.setObjectName("label_55")

        self.label_56 = QtWidgets.QLabel(self.tab_14)
        self.label_56.setGeometry(QtCore.QRect(740, 100, 351, 411))
        self.label_56.setStyleSheet("border: 2px solid #efefef;\n"
"border-radius: 10px;")
        self.label_56.setText("")
        self.label_56.setObjectName("label_56")

        self.user_data_table = QtWidgets.QTableWidget(self.tab_14)
        self.user_data_table.setGeometry(QtCore.QRect(90, 110, 511, 391))
        self.user_data_table.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.user_data_table.setObjectName("user_data_table")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user_data_table.setFont(font)
        self.user_data_table.setColumnCount(3)
        self.user_data_table.setHorizontalHeaderLabels(
                ['ID', 'Login', 'Role'])
        self.user_data_table.verticalHeader().setVisible(False)
        self.user_data_table.horizontalHeader().setSortIndicatorShown(True)

        self.label_66 = QtWidgets.QLabel(self.tab_14)
        self.label_66.setGeometry(QtCore.QRect(790, 40, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_66.setObjectName("label_66")

        self.company_name_plainTextEdit_2 = QtWidgets.QLineEdit(self.tab_14)
        self.company_name_plainTextEdit_2.setGeometry(QtCore.QRect(780, 140, 271, 51))
        self.company_name_plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 20pt \"Cambria\";\n"
"border-radius: 10px;")
        self.company_name_plainTextEdit_2.setObjectName("company_name_plainTextEdit_2")


        self.company_name_plainTextEdit_3 = QtWidgets.QLineEdit(self.tab_14)
        self.company_name_plainTextEdit_3.setGeometry(QtCore.QRect(780, 230, 271, 51))
        self.company_name_plainTextEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 20pt \"Cambria\";")
        self.company_name_plainTextEdit_3.setObjectName("company_name_plainTextEdit_3")

        self.company_name_plainTextEdit_4 = QtWidgets.QLineEdit(self.tab_14)
        self.company_name_plainTextEdit_4.setGeometry(QtCore.QRect(780, 320, 271, 51))
        self.company_name_plainTextEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"font: 20pt \"Cambria\";")
        self.company_name_plainTextEdit_4.setObjectName("company_name_plainTextEdit_4")

        self.create_ie_btn_3 = QtWidgets.QPushButton(self.tab_14)
        self.create_ie_btn_3.setGeometry(QtCore.QRect(770, 420, 141, 51))
        self.create_ie_btn_3.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.create_ie_btn_3.setObjectName("create_ie_btn_3")
        self.create_ie_btn_3.clicked.connect(self.create_user)

        self.create_ie_btn_4 = QtWidgets.QPushButton(self.tab_14)
        self.create_ie_btn_4.setGeometry(QtCore.QRect(920, 420, 141, 51))
        self.create_ie_btn_4.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);\n"
"border-radius: 5px;")
        self.create_ie_btn_4.setObjectName("create_ie_btn_4")
        self.create_ie_btn_4.clicked.connect(self.delete_user)

        self.label_67 = QtWidgets.QLabel(self.tab_14)
        self.label_67.setGeometry(QtCore.QRect(220, 40, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_67.setFont(font)
        self.label_67.setStyleSheet("color: rgb(236, 236, 236);\n"
"font: 75 18pt \"Impact\";")
        self.label_67.setObjectName("label_67")

        self.mainTabWidget.addTab(self.tab_14, "")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.mainTabWidget.setCurrentIndex(0)
        self.tableTabWidget.setCurrentIndex(0)
        self.create_update_tabWidget.setCurrentIndex(0)

        self.getPriv()
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ControlDelivery"))
        self.label_3.setText(_translate("MainWindow", "Система управления БД"))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_3), _translate("MainWindow", " Задания "))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_5), _translate("MainWindow", " Метро "))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_4), _translate("MainWindow", " БЦ "))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_6), _translate("MainWindow", " Клиенты "))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_7), _translate("MainWindow", " Компании "))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_8), _translate("MainWindow", " ИП-и"))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_9), _translate("MainWindow", "ЛДД"))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_10), _translate("MainWindow", "Контакты"))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_11), _translate("MainWindow", "Контракты"))
        self.tableTabWidget.setTabText(self.tableTabWidget.indexOf(self.tab_12), _translate("MainWindow", "Услуги"))
        self.label_5.setText(_translate("MainWindow", "Пометить задание как выполненное"))
        self.completed_task_btn.setText(_translate("MainWindow", "Завершить"))
        self.label_8.setText(_translate("MainWindow", "Готовность док-ов на метро"))
        self.ready_metro_btn.setText(_translate("MainWindow", "Готовность"))
        self.label_9.setText(_translate("MainWindow", "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"))
        self.clear_task_btn.setText(_translate("MainWindow", "Очистить задания"))
        self.update_tables_btn.setText(_translate("MainWindow", "Обновить таблицы"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tables_tab), _translate("MainWindow", "Таблицы"))
        self.label_11.setText(_translate("MainWindow", "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"))
        self.name_metro_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Название"))
        self.create_metro_btn.setText(_translate("MainWindow", "Создать"))
        self.change_metro_btn.setText(_translate("MainWindow", "Изменить"))
        self.label_15.setText(_translate("MainWindow", "ID"))
        self.label_30.setText(_translate("MainWindow", "*"))
        self.create_update_tabWidget.setTabText(self.create_update_tabWidget.indexOf(self.tab), _translate("MainWindow", "Метро"))
        self.name_bc_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Название"))
        self.address_bc_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Адрес"))
        self.passes_bc_checkBox.setText(_translate("MainWindow", "Пропускная система"))
        self.create_bc_btn.setText(_translate("MainWindow", "Создать"))
        self.change_bc_btn.setText(_translate("MainWindow", "Изменить"))
        self.label_16.setText(_translate("MainWindow", "ID"))
        self.label_17.setText(_translate("MainWindow", "Метро ID"))
        self.label_31.setText(_translate("MainWindow", "*"))
        self.label_32.setText(_translate("MainWindow", "*"))
        self.label_33.setText(_translate("MainWindow", "*"))
        self.create_update_tabWidget.setTabText(self.create_update_tabWidget.indexOf(self.tab_13), _translate("MainWindow", "БЦ"))
        self.ie_fname_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.ie_lname_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Фамилия"))
        self.ie_phone_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Телефон"))
        self.ie_office_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Офис"))
        self.label_19.setText(_translate("MainWindow", "ID Контракта"))
        self.ie_con_rec_checkBox.setText(_translate("MainWindow", "Договор доставлен"))
        self.ie_desc_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Доп. информация"))
        self.label_20.setText(_translate("MainWindow", "ID БЦ"))
        self.create_ie_btn.setText(_translate("MainWindow", "Создать"))
        self.change_ie_btn_3.setText(_translate("MainWindow", "Изменить"))
        self.ie_call_a_checkBox.setText(_translate("MainWindow", "Предварительный звонок"))
        self.label_34.setText(_translate("MainWindow", "*"))
        self.label_35.setText(_translate("MainWindow", "*"))
        self.label_36.setText(_translate("MainWindow", "*"))
        self.label_37.setText(_translate("MainWindow", "*"))
        self.label_38.setText(_translate("MainWindow", "*"))
        self.label_39.setText(_translate("MainWindow", "*"))
        self.label_40.setText(_translate("MainWindow", "*"))
        self.create_update_tabWidget.setTabText(self.create_update_tabWidget.indexOf(self.tab_15), _translate("MainWindow", "ИП"))
        self.company_name_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.company_office_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Офис"))
        self.company_call_a_checkBox.setText(_translate("MainWindow", "Предварительный звонок"))
        self.label_22.setText(_translate("MainWindow", "ID Контракта"))
        self.company_con_rec_checkBox.setText(_translate("MainWindow", "Договор доставлен"))
        self.company_desc_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Доп. информация"))
        self.label_23.setText(_translate("MainWindow", "ID БЦ"))
        self.create_ie_btn_2.setText(_translate("MainWindow", "Создать"))
        self.change_ie_btn_4.setText(_translate("MainWindow", "Изменить"))
        self.label_41.setText(_translate("MainWindow", "*"))
        self.label_42.setText(_translate("MainWindow", "*"))
        self.label_43.setText(_translate("MainWindow", "*"))
        self.label_44.setText(_translate("MainWindow", "*"))
        self.label_45.setText(_translate("MainWindow", "*"))
        self.create_update_tabWidget.setTabText(self.create_update_tabWidget.indexOf(self.tab_16), _translate("MainWindow", "Компания"))
        self.contact_fname_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Имя"))
        self.contact_lname_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Фамилия"))
        self.contact_phone_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Телефон"))
        self.label_25.setText(_translate("MainWindow", "ID Компании"))
        self.create_contact_btn.setText(_translate("MainWindow", "Создать"))
        self.change_contact_btn.setText(_translate("MainWindow", "Изменить"))
        self.label_46.setText(_translate("MainWindow", "*"))
        self.label_47.setText(_translate("MainWindow", "*"))
        self.label_48.setText(_translate("MainWindow", "*"))
        self.create_update_tabWidget.setTabText(self.create_update_tabWidget.indexOf(self.tab_17), _translate("MainWindow", "Контакты"))
        self.service_name_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Название"))
        self.label_27.setText(_translate("MainWindow", "$"))
        self.create_service_btn.setText(_translate("MainWindow", "Создать"))
        self.change_service_btn.setText(_translate("MainWindow", "Изменить"))
        self.label_49.setText(_translate("MainWindow", "*"))
        self.label_50.setText(_translate("MainWindow", "*"))
        self.create_update_tabWidget.setTabText(self.create_update_tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Услуга"))
        self.task_metros_is_plainTextEdit.setPlaceholderText(_translate("MainWindow", "Номер метро (1, 2, 3)"))
        self.label_29.setText(_translate("MainWindow", "Дата завершения"))
        self.create_task_btn.setText(_translate("MainWindow", "Создать"))
        self.change_task_btn.setText(_translate("MainWindow", "Изменить"))
        self.label_51.setText(_translate("MainWindow", "*"))
        self.label_52.setText(_translate("MainWindow", "*"))
        self.create_update_tabWidget.setTabText(self.create_update_tabWidget.indexOf(self.tab_18), _translate("MainWindow", "Задание"))
        self.label_60.setText(_translate("MainWindow", "* - можно изменить"))
        self.label_62.setText(_translate("MainWindow", "1. (Метро, БЦ) / Услуга"))
        self.label_63.setText(_translate("MainWindow", "2. ИП / (Компания, Контакты)"))
        self.label_64.setText(_translate("MainWindow", "3. Задание"))
        self.label_65.setText(_translate("MainWindow", "Алгоритм создания"))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.create_update_tab), _translate("MainWindow", "Создать / Изменить"))
        self.label_66.setText(_translate("MainWindow", "Пользователь системы"))
        self.company_name_plainTextEdit_2.setPlaceholderText(_translate("MainWindow", "login"))
        self.company_name_plainTextEdit_3.setPlaceholderText(_translate("MainWindow", "role"))
        self.company_name_plainTextEdit_4.setPlaceholderText(_translate("MainWindow", "password"))
        self.create_ie_btn_3.setText(_translate("MainWindow", "Создать"))
        self.create_ie_btn_4.setText(_translate("MainWindow", "Удалить"))
        self.label_67.setText(_translate("MainWindow", "Таблица пользователей"))
        self.service_price_spinBox.setMaximum(100000)
        self.id_bc_spinBox.setMaximum(100000)
        self.id_metro_spinBox.setMaximum(100000)
        self.id_metro_bc_spinBox.setMaximum(100000)
        self.ie_bc_id_spinBox_3.setMaximum(100000)
        self.ie_contract_id_spinBox.setMaximum(100000)
        self.task_user_id_spinBox.setMaximum(100000)
        self.company_bc_id_spinBox.setMaximum(100000)
        self.company_contract_id_spinBox.setMaximum(100000)
        self.ready_metro_spinBox.setMaximum(100000)
        self.contact_com_id_spinBox.setMaximum(100000)
        self.completed_task_spinBox.setMaximum(100000)
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_14), _translate("MainWindow", "Система"))

    #ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ РОЛИ ПОЛЬЗОВАТЕЛЯ
    def getPriv(self):
        if self.user_pos == 'courier':
                    self.create_update_tab.setEnabled(False)
                    self.tab_14.setEnabled(False)
                    self.ready_metro_Widget.setEnabled(False)
                    self.clear_task_btn.setEnabled(False)
        elif self.user_pos == 'manager':
                    self.tab_14.setEnabled(False)
                    self.completed_task_Widget.setEnabled(False)
        elif self.user_pos == 'admin' or self.user_pos == 'postgres':
                    self.loadUserTable()

    def loadTaskTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM task;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.task_table.setRowCount(len(list))
                    for row in list:
                            self.task_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.task_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.task_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            self.task_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                            self.task_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                            self.task_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                            self.task_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу заданий!!!')
                    msg.exec()
    def loadMetroTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM metro_station;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.metro_table.setRowCount(len(list))
                    for row in list:
                            self.metro_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.metro_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.metro_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            self.metro_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу метро!!!')
                    msg.exec()

    def loadBCTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM business_center;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.BC_table.setRowCount(len(list))
                    for row in list:
                            self.BC_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.BC_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.BC_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            self.BC_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                            self.BC_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                            self.BC_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу БЦ!!!')
                    msg.exec()

    def loadClientTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM client;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.client_table.setRowCount(len(list))
                    for row in list:
                            self.client_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.client_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.client_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            self.client_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу Клиентов!!!')
                    msg.exec()

    def loadCompanyTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM company;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.company_table.setRowCount(len(list))
                    for row in list:
                            self.company_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.company_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.company_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            self.company_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                            self.company_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                            self.company_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                            self.company_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                            self.company_table.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                            self.company_table.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу Компаний!!!')
                    msg.exec()

    def loadIETable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM Individual_entrepreneur;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.ie_table.setRowCount(len(list))
                    for row in list:
                            self.ie_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.ie_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.ie_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            self.ie_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                            self.ie_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                            self.ie_table.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[5])))
                            self.ie_table.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(row[6])))
                            self.ie_table.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(str(row[7])))
                            self.ie_table.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(str(row[8])))
                            self.ie_table.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(str(row[9])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу ИП!!!')
                    msg.exec()

    def loadDDSTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM document_delivery_sheet;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.dds_table.setRowCount(len(list))
                    for row in list:
                            self.dds_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.dds_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.dds_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу ЛДД!!!')
                    msg.exec()

    def loadContactTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM contact_person;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.contact_table.setRowCount(len(list))
                    for row in list:
                            self.contact_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.contact_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.contact_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            self.contact_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
                            self.contact_table.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу Контактов!!!')
                    msg.exec()

    def loadContractTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM contract;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.contract_table.setRowCount(len(list))
                    for row in list:
                            self.contract_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.contract_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.contract_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу Контрактов!!!')
                    msg.exec()

    def loadServiceTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM service;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.service_table.setRowCount(len(list))
                    for row in list:
                            self.service_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.service_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.service_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу Услуг!!!')
                    msg.exec()

    def loadUserTable(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT * FROM user_data;""")
                    tablerow = 0
                    list = cur.fetchall()
                    self.user_data_table.setRowCount(len(list))
                    for row in list:
                            self.user_data_table.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
                            self.user_data_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                            self.user_data_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                            tablerow += 1
                    cur.close()
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось заполнить таблицу Пользователей!!!')
                    msg.exec()


    #ФУНКЦИЯ ДЛЯ ОБНОВЛЕНИЯ ТАБЛИЦ
    def update_tables(self):
            if self.user_pos == 'manager' or self.user_pos == 'courier':
                    self.loadIETable()
                    self.loadBCTable()
                    self.loadServiceTable()
                    self.loadContractTable()
                    self.loadContactTable()
                    self.loadDDSTable()
                    self.loadClientTable()
                    self.loadMetroTable()
                    self.loadTaskTable()
                    self.loadCompanyTable()
            else:
                    self.loadIETable()
                    self.loadBCTable()
                    self.loadServiceTable()
                    self.loadContractTable()
                    self.loadContactTable()
                    self.loadDDSTable()
                    self.loadClientTable()
                    self.loadMetroTable()
                    self.loadTaskTable()
                    self.loadCompanyTable()
                    self.loadUserTable()

    #ФУНКЦИЯ ДЛЯ ПОМЕТКИ ЗАДАНИЯ, КАК ВЫПОЛНЕННОЕ
    def completed_task(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    value = self.completed_task_spinBox.text()
                    if check(value):
                           cur.execute(f"""CALL completed_task({value});""")
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось пометить задание!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ ПОМЕТКИ МЕТРО, КАК ГОТОВОГО К РАЗДАЧЕ
    def ready_metro(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    value = self.ready_metro_spinBox.text()
                    if check(value):
                           cur.execute(f"""CALL ready_metro({value});""")
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось изменить состояние метро!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ УДАЛЕНИЯ ПРОСРОЧЕННЫХ ЗАДАНИЙ
    def clear_task(self):
            try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute(f"""CALL clear_tasks();""")
            except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось изменить состояние метро!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ СОЗДАНИЯ ПОЛЬЗОВАТЕЛЯ
    def create_user(self):
            login = self.company_name_plainTextEdit_2.text().strip()
            passwd = self.company_name_plainTextEdit_4.text().strip()
            role = self.company_name_plainTextEdit_3.text().strip()
            if check(login) and check(passwd) and check(role):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""CALL create_user('{login}', {role}, '{passwd}');""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось создать пользователя!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ УДАЛЕНИЯ ПОЛЬЗОВАТЕЛЯ
    def delete_user(self):
            login = self.company_name_plainTextEdit_2.text().strip()
            if check(login):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""CALL delete_user('{login}');""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось удалить пользователя!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ СОЗДАНИЯ МЕТРО
    def create_metro(self):
            name = self.name_metro_plainTextEdit.text().strip()
            if check(name):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""CALL create_metro('{name}');""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось создать метро!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ ИЗМЕНЕНИЯ МЕТРО
    def update_metro(self):
            name = self.name_metro_plainTextEdit.text().strip()
            num = self.id_metro_spinBox.value()
            if check(name):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""UPDATE public.metro_station SET metro_station_name = '{name}' WHERE metro_station_id = {num};""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось изменить метро!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ СОЗДАНИЯ БЦ
    def create_BC(self):
            name = self.name_bc_plainTextEdit.text().strip()
            addr = self.address_bc_plainTextEdit.text().strip()
            passes = '+' if self.passes_bc_checkBox.isChecked() else '-'
            metro_id = self.id_metro_bc_spinBox.value()
            if check(name):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""CALL create_BC('{name}', '{addr}', '{passes}', {metro_id});""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось создать БЦ!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ ИЗМЕНЕНИЯ БЦ
    def update_BC(self):
            name = self.name_bc_plainTextEdit.text().strip()
            addr = self.address_bc_plainTextEdit.text().strip()
            passes = '+' if self.passes_bc_checkBox.isChecked() else '-'
            num = self.id_metro_bc_spinBox.value()
            if check(name):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""UPDATE public.Business_center SET BC_name = '{name}', BC_address = '{addr}',BC_passes = '{passes}' WHERE bc_id = {num};""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось изменить БЦ метро!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ СОЗДАНИЯ ИП
    def create_ie(self):
            fname = self.ie_fname_plainTextEdit.text().strip()
            lname = self.ie_lname_plainTextEdit.text().strip()
            phone = self.ie_phone_plainTextEdit.text().strip()
            contr = self.ie_contract_id_spinBox.value()
            office = self.ie_office_plainTextEdit.text().strip()
            call_a = '+' if self.ie_call_a_checkBox.isChecked() else '-'
            con_rec = '+' if self.ie_con_rec_checkBox.isChecked() else '-'
            desc = self.ie_desc_plainTextEdit.text().strip()
            if desc == '':
                    desc = None
            bc_id = self.ie_bc_id_spinBox_3.value()
            if check(fname) and check(lname) and check(phone) and check(office) and check(desc):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""CALL create_ie('{fname}', '{lname}', {phone}, {contr}, '{office}','{call_a}','{con_rec}','{desc}', {bc_id});""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось создать ИП!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ ИЗМЕНЕНИЯ ИП
    def update_ie(self):
            fname = self.ie_fname_plainTextEdit.text().strip()
            lname = self.ie_lname_plainTextEdit.text().strip()
            phone = self.ie_phone_plainTextEdit.text().strip()
            office = self.ie_office_plainTextEdit.text().strip()
            call_a = '+' if self.ie_call_a_checkBox.isChecked() else '-'
            con_rec = '+' if self.ie_con_rec_checkBox.isChecked() else '-'
            desc = self.ie_desc_plainTextEdit.text().strip()
            ie_id = self.ie_id_spinBox.value()
            if desc == '':
                    desc = None
            if check(fname) and check(lname) and check(phone) and check(office) and check(desc):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""UPDATE public.individual_entrepreneur 
                            SET ie_firstname = '{fname}',
                            ie_lastname = '{lname}',
                            ie_phone = '{phone}',
                            ie_office_num =  '{office}',
                            ie_call_ahead = '{call_a}',
                            ie_contract_received = '{con_rec}',
                            ie_description = '{desc}'
                            WHERE ie_id = {ie_id};""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось изменить ИП!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ СОЗДАНИЯ КОМПАНИИ
    def create_company(self):
            name = self.company_name_plainTextEdit.text().strip()
            contr = self.company_contract_id_spinBox.value()
            office = self.company_office_plainTextEdit.text().strip()
            call_a = '+' if self.company_call_a_checkBox.isChecked() else '-'
            con_rec = '+' if self.company_con_rec_checkBox.isChecked() else '-'
            desc = self.company_desc_plainTextEdit.text().strip()
            if desc == '':
                    desc = None
            bc_id = self.company_bc_id_spinBox.value()

            if check(name) and check(office) and check(desc):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""CALL create_company('{name}', '{office}', '{call_a}', {contr}, '{con_rec}', '{desc}', {bc_id});""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось создать компанию!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ ИЗМЕНЕНИЯ КОМПАНИИ
    def update_company(self):
            name = self.company_name_plainTextEdit.text().strip()
            office = self.company_office_plainTextEdit.text().strip()
            desc = self.company_desc_plainTextEdit.text().strip()
            call_a = '+' if self.company_call_a_checkBox.isChecked() else '-'
            con_rec = '+' if self.company_con_rec_checkBox.isChecked() else '-'
            id_company = self.company_id_spinBox.value()
            if desc == '':
                    desc = None

            if check(name) and check(office) and check(desc):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""UPDATE public.company 
                                                        SET company_name = '{name}',
                                                        company_office_num =  '{office}',
                                                        company_call_ahead = '{call_a}',
                                                        company_contract_received = '{con_rec}',
                                                        company_description = '{desc}'
                                                        WHERE company_id = {id_company};""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось изменить компанию!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ СОЗДАНИЯ КОНТАКТНОГО ЛИЦА
    def create_contact(self):
            fname = self.contact_fname_plainTextEdit.text().strip()
            lname = self.contact_lname_plainTextEdit.text().strip()
            phone = self.contact_phone_plainTextEdit.text().strip()
            company_id = self.contact_com_id_spinBox.value()

            if check(fname) and check(lname) and check(phone):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""CALL create_contact_person('{fname}', '{lname}',  {phone}, {company_id});""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось создать контактное лицо!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ ИЗМЕНЕНИЯ КОНТАКТНОГО ЛИЦА
    def update_contact(self):
            fname = self.contact_fname_plainTextEdit.text().strip()
            lname = self.contact_lname_plainTextEdit.text().strip()
            phone = self.contact_phone_plainTextEdit.text().strip()
            company_id = self.contact_com_id_spinBox.value()

            if check(fname) and check(lname) and check(phone):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""UPDATE public.contact_person
                                        SET contact_person_firstname = '{fname}',
                                        contact_person_lastname =  '{lname}',
                                        contact_person_phonenum = {phone}
                                        WHERE contact_person_id = {company_id};""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось изменить контактное лицо!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ СОЗДАНИЯ УСЛУГИ
    def create_service(self):
            name = self.service_name_plainTextEdit.text().strip()
            price = self.service_price_spinBox.value()

            if check(name):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""CALL create_service('{name}', {price});""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось создать услугу!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()

    #ФУНКЦИЯ ДЛЯ ИЗМЕНЕНИЯ УСЛУГИ
    def update_service(self):
            name = self.service_name_plainTextEdit.text().strip()
            price = self.service_price_spinBox.value()
            num = self.service_id_spinBox.value()

            if check(name):
                    try:
                            conn = self.conn
                            cur = conn.cursor()
                            cur.execute(f"""UPDATE public.service
                                                                    SET service_name = '{name}',
                                                                    service_price =  {price}
                                                                    WHERE service_id = {num};""")
                    except:
                            msg = QMessageBox()
                            msg.setWindowTitle('Ошибка')
                            msg.setText('Не удалось создать услугу!!!')
                            msg.exec()
            else:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Некорректные данные!!!')
                    msg.exec()


    #ФУНКЦИЯ СОЗДАНИЯ ЗАДАНИЯ
    def create_task(self):
            user_id = self.task_user_id_spinBox.value()
            metro_id = self.task_metros_is_plainTextEdit.text().strip().split(', ')
            date = self.task_close_date_dateEdit.date().toPyDate()
            st = '{'
            try:
                metro_id2 = [int(item) for item in metro_id]
                st = '{'
                x = len(metro_id2)
                for i in range(x):
                        if i == x - 1:
                                st += str(metro_id2[i])
                        else:
                                st += str(metro_id2[i]) + ', '
                st += '}'
            except:
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText('Некорректные данные!!!')
                msg.exec()
                exit()
            try:
                conn = self.conn
                cur = conn.cursor()
                cur.execute(f"""CALL create_task('{st}', '{date}', {user_id});""")
            except:
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText('Не удалось создать задание!!!')
                msg.exec()

    #ФУНКЦИЯ ИЗМЕНЕНИЯ ЗАДАНИЯ
    def update_task(self):
            task_id = self.task_id_spinBox.value()
            metro_id = self.task_metros_is_plainTextEdit.text().strip().split(', ')
            date = self.task_close_date_dateEdit.date().toPyDate()
            st = '{'
            try:
                metro_id2 = [int(item) for item in metro_id]
                st = '{'
                x = len(metro_id2)
                for i in range(x):
                        if i == x - 1:
                                st += str(metro_id2[i])
                        else:
                                st += str(metro_id2[i]) + ', '
                st += '}'
            except:
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText('Некорректные данные!!!')
                msg.exec()
                exit()
            try:
                conn = self.conn
                cur = conn.cursor()
                cur.execute(f"""UPDATE public.task
                                        SET task_metro_id = '{st}',
                                        task_close_date =  '{date}'
                                        WHERE task_id = {task_id};""")
            except:
                msg = QMessageBox()
                msg.setWindowTitle('Ошибка')
                msg.setText('Не удалось изменить задание!!!')
                msg.exec()


    #ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ РОЛИ ПОЛЬЗОВАТЕЛЯ
    def get_user_position(self):
        if self.user_login == 'postgres':
            position = 'admin'
            return position
        else:
                try:
                    conn = self.conn
                    cur = conn.cursor()
                    cur.execute("""SELECT user_role FROM user_data WHERE (user_login = current_user);""")
                    ind = int(cur.fetchone()[0])
                    if ind == 1:
                        position = 'courier'
                    elif ind == 2:
                        position = 'manager'
                    else:
                        position = 'admin'
                    cur.close()
                    return position
                except:
                    msg = QMessageBox()
                    msg.setWindowTitle('Ошибка')
                    msg.setText('Не удалось получить роль пользователя!!!')
                    msg.exec()


#ФУНКЦИЯ ДЛЯ ПРОВЕРКИ ПОЛЯ НА ИНЪЕКЦИЮ
def check(txt):
    listS = ["'", '-', '--', '/', '|', '*', '%', '#', '!', '?']
    return not any(symbol in txt for symbol in listS)


