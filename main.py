import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_dialog_window import LoginDialogWindow
from home_widget import HomeWidgetWindow
from db_connection import MySQLConnection

def main():
    #mysql_connection = MySQLConnection()
    app = QtGui.QApplication(sys.argv)
    window = LoginDialogWindow()
    window.show()

    home_window = HomeWidgetWindow()
    home_window.hide()

    sys.exit(app.exec_())
    #mysql_connection.cnx.close()

if __name__ == "__main__":
    main()
