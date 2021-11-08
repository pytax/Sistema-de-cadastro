# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(935, 497)
        MainWindow.setStyleSheet(u"background-color: rgb(9, 9, 9);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	\n"
"	border:none;\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu = QFrame(self.centralwidget)
        self.left_menu.setObjectName(u"left_menu")
        self.left_menu.setMaximumSize(QSize(9, 16777215))
        self.left_menu.setStyleSheet(u"")
        self.left_menu.setFrameShape(QFrame.StyledPanel)
        self.left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.frame_4 = QFrame(self.left_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Cooper Black"])
        font.setPointSize(12)
        self.label_3.setFont(font)

        self.verticalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.left_menu)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(65, 65, 65);\n"
"\n"
"}\n"
"\n"
"QToolBox{\n"
"\n"
"text-align: left;\n"
"	background-color: rgb(228, 254, 255);\n"
"\n"
"}\n"
"\n"
"\n"
"QToolBox::tab{\n"
"	border-radius: 5px;	\n"
"	\n"
"	background-color: rgb(194, 232, 255);\n"
"	text-align: left;\n"
"\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.toolBox = QToolBox(self.frame_5)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover{	\n"
"	background-color: rgb(65, 65, 65);\n"
"	 border-top-left-radius:15px\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 67, 343))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 9, 0, -1)
        self.btn_home = QPushButton(self.page)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_menu_cadastrar = QPushButton(self.page)
        self.btn_menu_cadastrar.setObjectName(u"btn_menu_cadastrar")
        self.btn_menu_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_menu_cadastrar.setFont(font1)
        self.btn_menu_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_menu_cadastrar)

        self.btn_menu_contatos = QPushButton(self.page)
        self.btn_menu_contatos.setObjectName(u"btn_menu_contatos")
        self.btn_menu_contatos.setMinimumSize(QSize(0, 30))
        self.btn_menu_contatos.setFont(font1)
        self.btn_menu_contatos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_menu_contatos)

        self.btn_menu_sobre = QPushButton(self.page)
        self.btn_menu_sobre.setObjectName(u"btn_menu_sobre")
        self.btn_menu_sobre.setMinimumSize(QSize(0, 30))
        self.btn_menu_sobre.setFont(font1)
        self.btn_menu_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.btn_menu_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Menu")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 84, 360))
        self.verticalLayout_15 = QVBoxLayout(self.page_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_15 = QLabel(self.page_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_15.setWordWrap(True)

        self.verticalLayout_15.addWidget(self.label_15)

        self.toolBox.addItem(self.page_2, u"Informa\u00e7\u00f5es")

        self.verticalLayout_5.addWidget(self.toolBox)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.left_menu)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/menu2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(30, 40))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(62, 62, 62);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.main_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_8 = QVBoxLayout(self.pg_home)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_4 = QLabel(self.pg_home)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_8.addWidget(self.label_4, 0, Qt.AlignVCenter)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_9 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tabWidget = QTabWidget(self.pg_cadastro)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_10 = QVBoxLayout(self.tab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_16 = QFrame(self.tab)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy1.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy1)
        self.frame_16.setStyleSheet(u"QLineEdit{\n"
"\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QFrame{\n"
"	\n"
"	\n"
"	background-color: rgb(231, 231, 231);\n"
"\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_16)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.txt_complemento = QLineEdit(self.frame_16)
        self.txt_complemento.setObjectName(u"txt_complemento")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_complemento.sizePolicy().hasHeightForWidth())
        self.txt_complemento.setSizePolicy(sizePolicy2)
        self.txt_complemento.setMinimumSize(QSize(0, 30))
        self.txt_complemento.setMaximumSize(QSize(16777215, 30))
        self.txt_complemento.setStyleSheet(u"")
        self.txt_complemento.setMaxLength(21)

        self.gridLayout_7.addWidget(self.txt_complemento, 3, 2, 1, 2)

        self.txt_tel_contr = QLineEdit(self.frame_16)
        self.txt_tel_contr.setObjectName(u"txt_tel_contr")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txt_tel_contr.sizePolicy().hasHeightForWidth())
        self.txt_tel_contr.setSizePolicy(sizePolicy3)
        self.txt_tel_contr.setMinimumSize(QSize(0, 30))
        self.txt_tel_contr.setMaximumSize(QSize(16777215, 30))
        self.txt_tel_contr.setStyleSheet(u"")
        self.txt_tel_contr.setMaxLength(13)
        self.txt_tel_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_tel_contr, 5, 0, 1, 3)

        self.txt_logradouro = QLineEdit(self.frame_16)
        self.txt_logradouro.setObjectName(u"txt_logradouro")
        sizePolicy2.setHeightForWidth(self.txt_logradouro.sizePolicy().hasHeightForWidth())
        self.txt_logradouro.setSizePolicy(sizePolicy2)
        self.txt_logradouro.setMinimumSize(QSize(0, 30))
        self.txt_logradouro.setMaximumSize(QSize(16777215, 30))
        self.txt_logradouro.setStyleSheet(u"")
        self.txt_logradouro.setMaxLength(40)

        self.gridLayout_7.addWidget(self.txt_logradouro, 2, 0, 1, 6)

        self.txt_cnpj_contr = QLineEdit(self.frame_16)
        self.txt_cnpj_contr.setObjectName(u"txt_cnpj_contr")
        sizePolicy2.setHeightForWidth(self.txt_cnpj_contr.sizePolicy().hasHeightForWidth())
        self.txt_cnpj_contr.setSizePolicy(sizePolicy2)
        self.txt_cnpj_contr.setMinimumSize(QSize(0, 30))
        self.txt_cnpj_contr.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.txt_cnpj_contr.setFont(font2)
        self.txt_cnpj_contr.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_cnpj_contr.setMaxLength(14)
        self.txt_cnpj_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_cnpj_contr, 1, 0, 1, 2)

        self.txt_nome_contr = QLineEdit(self.frame_16)
        self.txt_nome_contr.setObjectName(u"txt_nome_contr")
        sizePolicy2.setHeightForWidth(self.txt_nome_contr.sizePolicy().hasHeightForWidth())
        self.txt_nome_contr.setSizePolicy(sizePolicy2)
        self.txt_nome_contr.setMinimumSize(QSize(0, 30))
        self.txt_nome_contr.setMaximumSize(QSize(16777215, 30))
        self.txt_nome_contr.setStyleSheet(u"")
        self.txt_nome_contr.setMaxLength(115)
        self.txt_nome_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_nome_contr, 1, 2, 1, 4)

        self.txt_num = QLineEdit(self.frame_16)
        self.txt_num.setObjectName(u"txt_num")
        sizePolicy2.setHeightForWidth(self.txt_num.sizePolicy().hasHeightForWidth())
        self.txt_num.setSizePolicy(sizePolicy2)
        self.txt_num.setMinimumSize(QSize(0, 30))
        self.txt_num.setStyleSheet(u"")
        self.txt_num.setMaxLength(6)

        self.gridLayout_7.addWidget(self.txt_num, 3, 0, 1, 2)

        self.txt_uf = QLineEdit(self.frame_16)
        self.txt_uf.setObjectName(u"txt_uf")
        sizePolicy2.setHeightForWidth(self.txt_uf.sizePolicy().hasHeightForWidth())
        self.txt_uf.setSizePolicy(sizePolicy2)
        self.txt_uf.setMinimumSize(QSize(0, 0))
        self.txt_uf.setStyleSheet(u"")
        self.txt_uf.setMaxLength(2)
        self.txt_uf.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_uf, 4, 4, 1, 1)

        self.txt_email_contr = QLineEdit(self.frame_16)
        self.txt_email_contr.setObjectName(u"txt_email_contr")
        sizePolicy3.setHeightForWidth(self.txt_email_contr.sizePolicy().hasHeightForWidth())
        self.txt_email_contr.setSizePolicy(sizePolicy3)
        self.txt_email_contr.setMinimumSize(QSize(0, 30))
        self.txt_email_contr.setMaximumSize(QSize(16777215, 30))
        self.txt_email_contr.setStyleSheet(u"")
        self.txt_email_contr.setInputMethodHints(Qt.ImhEmailCharactersOnly)
        self.txt_email_contr.setMaxLength(40)
        self.txt_email_contr.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_email_contr, 5, 3, 1, 3)

        self.txt_cep = QLineEdit(self.frame_16)
        self.txt_cep.setObjectName(u"txt_cep")
        sizePolicy3.setHeightForWidth(self.txt_cep.sizePolicy().hasHeightForWidth())
        self.txt_cep.setSizePolicy(sizePolicy3)
        self.txt_cep.setMinimumSize(QSize(0, 30))
        self.txt_cep.setStyleSheet(u"")
        self.txt_cep.setMaxLength(8)
        self.txt_cep.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_cep, 4, 5, 1, 1)

        self.txt_mun = QLineEdit(self.frame_16)
        self.txt_mun.setObjectName(u"txt_mun")
        sizePolicy2.setHeightForWidth(self.txt_mun.sizePolicy().hasHeightForWidth())
        self.txt_mun.setSizePolicy(sizePolicy2)
        self.txt_mun.setMinimumSize(QSize(0, 30))
        self.txt_mun.setStyleSheet(u"")
        self.txt_mun.setMaxLength(50)
        self.txt_mun.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_mun, 4, 0, 1, 4)

        self.txt_bairro = QLineEdit(self.frame_16)
        self.txt_bairro.setObjectName(u"txt_bairro")
        sizePolicy2.setHeightForWidth(self.txt_bairro.sizePolicy().hasHeightForWidth())
        self.txt_bairro.setSizePolicy(sizePolicy2)
        self.txt_bairro.setMinimumSize(QSize(0, 0))
        self.txt_bairro.setStyleSheet(u"")
        self.txt_bairro.setMaxLength(20)
        self.txt_bairro.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.txt_bairro, 3, 4, 1, 2)

        self.label_18 = QLabel(self.frame_16)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(0, 99, 148);\n"
"background-color: rgb(249, 249, 249);\n"
"")

        self.gridLayout_7.addWidget(self.label_18, 0, 0, 1, 6)


        self.verticalLayout_10.addWidget(self.frame_16)

        self.btn_cadastrar = QPushButton(self.tab)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btn_cadastrar.sizePolicy().hasHeightForWidth())
        self.btn_cadastrar.setSizePolicy(sizePolicy4)
        self.btn_cadastrar.setMinimumSize(QSize(170, 30))
        self.btn_cadastrar.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setPointSize(11)
        self.btn_cadastrar.setFont(font3)
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(0, 170, 255); \n"
"	border-radius:15px;\n"
"	color:#fff\n"
"}\n"
"\n"
"QPushButton{\n"
"			border-radius:15px;\n"
"	background-color: rgb(243, 243, 243);\n"
"}")

        self.verticalLayout_10.addWidget(self.btn_cadastrar, 0, Qt.AlignHCenter)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_11 = QVBoxLayout(self.tab_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 70))
        font4 = QFont()
        font4.setFamilies([u"Eras Bold ITC"])
        font4.setPointSize(14)
        self.label_11.setFont(font4)
        self.label_11.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(9, 9, 9);")

        self.verticalLayout_11.addWidget(self.label_11)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tb_company = QTableWidget(self.tab_2)
        if (self.tb_company.columnCount() < 11):
            self.tb_company.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_company.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        if (self.tb_company.rowCount() < 20):
            self.tb_company.setRowCount(20)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tb_company.setItem(0, 0, __qtablewidgetitem11)
        self.tb_company.setObjectName(u"tb_company")
        self.tb_company.setStyleSheet(u"\n"
"QHeaderView::section {\n"
"background-color: rgb(148, 148, 148);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
" }\n"
"\n"
"QTableWidget{\n"
"	\n"
"	background-color: rgb(252, 252, 252);\n"
"\n"
"}")
        self.tb_company.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_company.setRowCount(20)
        self.tb_company.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_company.horizontalHeader().setDefaultSectionSize(170)
        self.tb_company.verticalHeader().setVisible(False)

        self.horizontalLayout_4.addWidget(self.tb_company)

        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"	border-radius:15px;\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	\n"
"	font: 11pt \"MS Shell Dlg 2\";\n"
"	\n"
"	color: rgb(0, 24, 74);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"\n"
"	background-color: rgb(230, 230, 230);\n"
"\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_gerar_excel = QPushButton(self.frame)
        self.btn_gerar_excel.setObjectName(u"btn_gerar_excel")
        sizePolicy4.setHeightForWidth(self.btn_gerar_excel.sizePolicy().hasHeightForWidth())
        self.btn_gerar_excel.setSizePolicy(sizePolicy4)
        self.btn_gerar_excel.setMinimumSize(QSize(120, 31))
        font5 = QFont()
        font5.setFamilies([u"MS Shell Dlg 2"])
        font5.setPointSize(11)
        font5.setBold(False)
        font5.setItalic(False)
        self.btn_gerar_excel.setFont(font5)
        self.btn_gerar_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gerar_excel.setStyleSheet(u"QPushButton:hover{\n"
"	 color: rgb(255,255,255);\n"
"	background-color: rgb(49, 147, 0)}\n"
"")

        self.verticalLayout_12.addWidget(self.btn_gerar_excel)

        self.btn_alterar = QPushButton(self.frame)
        self.btn_alterar.setObjectName(u"btn_alterar")
        sizePolicy4.setHeightForWidth(self.btn_alterar.sizePolicy().hasHeightForWidth())
        self.btn_alterar.setSizePolicy(sizePolicy4)
        self.btn_alterar.setMinimumSize(QSize(120, 31))
        self.btn_alterar.setFont(font5)
        self.btn_alterar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar.setStyleSheet(u"QPushButton:hover{\n"
"	background-color:rgb(255, 170, 0);\n"
" 	color: rgb(255,255,255)\n"
"}\n"
"")

        self.verticalLayout_12.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame)
        self.btn_excluir.setObjectName(u"btn_excluir")
        sizePolicy4.setHeightForWidth(self.btn_excluir.sizePolicy().hasHeightForWidth())
        self.btn_excluir.setSizePolicy(sizePolicy4)
        self.btn_excluir.setMinimumSize(QSize(120, 31))
        self.btn_excluir.setFont(font5)
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton:hover{background-color:rgb(199, 66, 0); color: rgb(255,255,255)}")

        self.verticalLayout_12.addWidget(self.btn_excluir)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)


        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_9.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_14 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_5 = QLabel(self.pg_contatos)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout_14.addWidget(self.label_5)

        self.frame_2 = QFrame(self.pg_contatos)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.label_8)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        sizePolicy1.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy1)

        self.verticalLayout_13.addWidget(self.label_12)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_13.addWidget(self.label_10)


        self.verticalLayout_14.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_contatos)
        self.pg_about = QWidget()
        self.pg_about.setObjectName(u"pg_about")
        self.verticalLayout_7 = QVBoxLayout(self.pg_about)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_16 = QLabel(self.pg_about)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setMaximumSize(QSize(16777215, 70))

        self.verticalLayout_7.addWidget(self.label_16)

        self.label_17 = QLabel(self.pg_about)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_17)

        self.Pages.addWidget(self.pg_about)

        self.verticalLayout_6.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"PyTax", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_menu_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.btn_menu_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.btn_menu_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Usu\u00e1rio:</span><span style=\" font-size:10pt;\"> PyTax</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Sistema: </span><span style=\" font-size:10pt;\">Cadastro</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Status:</span><span style=\" font-size:10pt;\"> Ativo</span></p><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Venc: </span><span style=\" font-size:10pt;\">12/12/2999</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Informa\u00e7\u00f5es", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"toggle", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Sistema de cadastro</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icons/icons/logo4.png\"/></p></body></html>", None))
        self.txt_complemento.setText("")
        self.txt_complemento.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.txt_tel_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Telefone", None))
        self.txt_logradouro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Logradouro", None))
        self.txt_cnpj_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CNPJ", None))
        self.txt_nome_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome Empresarial", None))
        self.txt_num.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero", None))
        self.txt_uf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.txt_email_contr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"email", None))
        self.txt_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.txt_mun.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Munic\u00edpio", None))
        self.txt_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Empresa</span></p></body></html>", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">EMPRESAS</p></body></html>", None))
        ___qtablewidgetitem = self.tb_company.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"CNPJ", None));
        ___qtablewidgetitem1 = self.tb_company.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tb_company.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"LOGRADOURO", None));
        ___qtablewidgetitem3 = self.tb_company.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"N\u00daMERO", None));
        ___qtablewidgetitem4 = self.tb_company.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"COMPLEMENTO", None));
        ___qtablewidgetitem5 = self.tb_company.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem6 = self.tb_company.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"MUN\u00cdCIPIO", None));
        ___qtablewidgetitem7 = self.tb_company.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"UF", None));
        ___qtablewidgetitem8 = self.tb_company.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem9 = self.tb_company.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem10 = self.tb_company.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));

        __sortingEnabled = self.tb_company.isSortingEnabled()
        self.tb_company.setSortingEnabled(False)
        self.tb_company.setSortingEnabled(__sortingEnabled)

        self.btn_gerar_excel.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Empresas", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">CONTATOS</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/whatsApp.png\"/><span style=\" font-size:18pt; vertical-align:super;\">(11)98013-0552</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/email.png\"/><span style=\" font-size:18pt; vertical-align:super;\">contato@pytax.net</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">pytaxsolutions</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/icons/icons/Youtube.png\"/><a href=\"https://www.youtube.com/channel/UCvo99mtwpnJtKJqeu0lQvLA\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ffffff; vertical-align:super;\">Pytax</span></a></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">SOBRE</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Este sistema faz consulta do CNPJ utilizando API da receita federal e faz o cadastro em um banco de dados SQLITE3. Objetivo desse sistema \u00e9 ensinar como utilizar Python e o QT para desenvolver aplica\u00e7\u00f5es modernas funcionais.</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Pytax 2021", None))
    # retranslateUi

