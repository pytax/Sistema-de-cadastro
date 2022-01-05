from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem)
from ui_main import Ui_MainWindow
import sys
from ui_funtions import *
from database import Data_base
import pandas as pd
import sqlite3


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyTax - Sistema de cadastro de empresas")
        appIcon = QIcon(u"icons/logo4.png")
        self.setWindowIcon(appIcon)

        ################################################
        #TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.leftMenu)
        ################################################

        ##############################################################################################
        #Páginas do Sistema
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_menu_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_menu_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_about))
        self.btn_menu_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))
        ###############################################################################################

        ###############################################################################################
        # PREENCHER AUTOMATICAMENTE OS DADOS DO CNPJ
        self.txt_cnpj_contr.editingFinished.connect(self.consult_api)
        ###############################################################################################

        self.btn_cadastrar.clicked.connect(self.cadastrar_empresas)
        self.btn_alterar.clicked.connect(self.updata_company)
        self.btn_excluir.clicked.connect(self.deletar_empresa)
        self.btn_gerar_excel.clicked.connect(self.gerar_excel_2)

        self.buscar_empresas()

    def leftMenu(self):

        width = self.left_menu.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.left_menu, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def consult_api(self):
        campos = consulta_cnpj(self.txt_cnpj_contr.text())

        self.txt_nome_contr.setText(campos[0])
        self.txt_logradouro.setText(campos[1])
        self.txt_num.setText(campos[2])
        self.txt_complemento.setText(campos[3])
        self.txt_bairro.setText(campos[4])
        self.txt_mun.setText(campos[5])
        self.txt_uf.setText(campos[6])
        self.txt_cep.setText(campos[7].replace('.', '').replace('-',''))
        self.txt_tel_contr.setText(campos[8].replace('(','').replace('-','').replace(')',''))
        self.txt_email_contr.setText(campos[9])

    def cadastrar_empresas(self):
        db = Data_base()
        db.connect()

        fullDataSet = (

            self.txt_cnpj_contr.text(), self.txt_nome_contr.text(), self.txt_logradouro.text(), self.txt_num.text(),
            self.txt_complemento.text(), self.txt_bairro.text(), self.txt_mun.text(), self.txt_uf.text(),
            self.txt_cep.text(), self.txt_tel_contr.text().strip(), self.txt_email_contr.text()
        )

        #CADASTRAR NO BANCO DE DADOS
        resp = db.register_company(fullDataSet)

        if resp == "OK":
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Casdastro Realizado")
            msg.setText("Cadastro Realizado com sucesso")
            msg.exec()
            db.close_connection()
            return
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Erro")
            msg.setText("Erro ao cadastrar, verifique se as informações foram preenchidadas corretamente!")
            msg.exec()
            db.close_connection()
            return

    def buscar_empresas(self):

        db = Data_base()
        db.connect()
        result = db.select_all_companies()

        self.tb_company.clearContents()
        self.tb_company.setRowCount(len(result))

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                self.tb_company.setItem(row, column, QTableWidgetItem(str(data)))

        db.close_connection()

    def updata_company(self):

        dados = []
        update_dados = []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
            update_dados.append(dados)
            dados = []

        #ATUALIZAR DADOS NO BANCO
        db = Data_base()
        db.connect() 

        for emp in update_dados:
            db.update_company(tuple(emp))

        db.close_connection()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Atualização de Dados")
        msg.setText("Dados atualizados com sucesso!")
        msg.exec()

        self.tb_company.reset()
        self.buscar_empresas()

    def deletar_empresa(self):

        db = Data_base()
        db.connect()

        msg = QMessageBox()
        msg.setWindowTitle("Excluir")
        msg.setText("Este registor será excluído.")
        msg.setInformativeText("Você tem certeza que deseja excluir?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resp = msg.exec()

        if resp == QMessageBox.Yes:
            cnpj = self.tb_company.selectionModel().currentIndex().siblingAtColumn(0).data()
            result = db.delete_companies(cnpj)
            self.buscar_empresas()

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("EMPRESAS")
            msg.setText(result)
            msg.exec()

        db.close_connection()

    def gerar_excel(self):

        dados = []
        all_dados =  []

        for row in range(self.tb_company.rowCount()):
            for column in range(self.tb_company.columnCount()):
                dados.append(self.tb_company.item(row, column).text())
        
            all_dados.append(dados)
            dados = []

        columns = ['CNPJ', 'NOME', 'LOGRADOURO', 'NUMERO', 'COMPLEMENTO',
            'BAIRRO', 'MUNICÍPIO', 'UF', 'CEP','TELEFONE','EMAIL']
        
        empresas = pd.DataFrame(all_dados, columns= columns)
        empresas.to_excel("Empresas.xlsx", sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()

    def gerar_excel_2(self):

        cnx = sqlite3.connect("system.db")

        empresas = pd.read_sql_query("""SELECT * FROM Empresas""", cnx)

        empresas.to_excel("Empresas.xlsx", sheet_name='empresas', index=False)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Excel")
        msg.setText("Relatório Excel gerado com sucesso!")
        msg.exec()



        



if __name__ == "__main__":

    db = Data_base()
    db.connect()
    db.create_table_company()
    db.close_connection()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    app.exec()