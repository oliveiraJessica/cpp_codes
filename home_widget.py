import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

qtCreatorFile = "home_widget.ui"

Ui_Dialog, QtBaseClass = uic.loadUiType(qtCreatorFile)

class HomeWidgetWindow(QtGui.QDialog, Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        Ui_Dialog.__init__(self)
        self.setupUi(self)
        self.register_push_button.clicked.connect(self.register_patient)
        self.search_push_button.clicked.connect(self.search_patient)
        self.initiate_consultation_push_button.clicked.connect(self.initiate_consultation)
        self.exit_push_button.clicked.connect(self.exit)

    def register_patient(self):
        print("Abrir janela de registro")

    def search_patient(self):
        print("Abrir janela de busca de pacientes")

    def initiate_consultation(self):
        print("Abrir janela de início de consulta")

    def exit(self):
        print("Fechar janela")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = HomeWidgetWindow()
    window.show()
    sys.exit(app.exec_())
