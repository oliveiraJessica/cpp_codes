import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

qtCreatorFile = "ui/home_widget.ui"

Ui_Widget, QtBaseClass = uic.loadUiType(qtCreatorFile)

class HomeWidgetWindow(QtGui.QWidget, Ui_Widget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        Ui_Widget.__init__(self)
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
