import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from db_connection import MySQLConnection

qtCreatorFile = "login_dialog_window.ui"

Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)

class LoginDialogWindow(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.acess_push_button.clicked.connect(self.login_user)

    def check_acess_button(self):
        user_text = self.user_line_edit.text()
        password_text = self.password_line_edit.text()
        print('Button Pressed')
        print('User: %s' % user_text)
        print('Password: %s' % password_text)

    def login_user(self):
        user_text = self.user_line_edit.text()
        password_text = self.password_line_edit.text()
        query = "select id from users where login = '" + user_text + "' and password = '" + password_text + "';"
        print(query)
        user_id = mysql_connection.execute_query(query)
        print(user_id)
        if user_id != None:
            print(user_id, ' connected')
            self.summom_welcome_window()
        else:
            self.summom_warning_window()
            print('Senha ou usuário incorreto')

    def summom_warning_window(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Senha ou usuário incorreto")
        msg.setWindowTitle("Login falhou")
        msg.exec_()

    def summom_welcome_window(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Bem vindo!")
        msg.setWindowTitle("Login efetuado")
        msg.exec_()

if __name__ == "__main__":
    mysql_connection = MySQLConnection()
    app = QtGui.QApplication(sys.argv)
    window = LoginDialogWindow()
    window.show()
    sys.exit(app.exec_())
    #mysql_connection.cnx.close()
