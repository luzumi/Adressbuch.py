# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\VisualStudio-workspace\Adressbuch\AdressbuchPY_e\AdressbuchPY_e\AdressbuchUI\Kontaktliste\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lHeader = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.lHeader.setFont(font)
        self.lHeader.setAutoFillBackground(True)
        self.lHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.lHeader.setObjectName("lHeader")
        self.verticalLayout.addWidget(self.lHeader)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 90, 781, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelVN = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelVN.setObjectName("labelVN")
        self.horizontalLayout.addWidget(self.labelVN)
        self.lineEdit_Vorname = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_Vorname.setObjectName("lineEdit_Vorname")
        self.horizontalLayout.addWidget(self.lineEdit_Vorname)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.labelN = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelN.setObjectName("labelN")
        self.horizontalLayout.addWidget(self.labelN)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.horizontalLayout.addWidget(self.lineEdit_Name)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.labelTel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelTel.setObjectName("labelTel")
        self.horizontalLayout.addWidget(self.labelTel)
        self.lineEdit_Telefon = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_Telefon.setObjectName("lineEdit_Telefon")
        self.horizontalLayout.addWidget(self.lineEdit_Telefon)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 190, 781, 91))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_Hinzu = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_Hinzu.setObjectName("pushButton_Hinzu")
        self.horizontalLayout_2.addWidget(self.pushButton_Hinzu)
        self.pushButton_Hinzu.clicked.connect(self.addNummer)
        self.pushButton_Kontakt_anzeigen = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_Kontakt_anzeigen.setObjectName("pushButton_Kontakt_anzeigen")
        self.horizontalLayout_2.addWidget(self.pushButton_Kontakt_anzeigen)
        self.pushButton_Kontakt_anzeigen.clicked.connect(self.getNummer)
        self.pushButton_Kont_Del = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_Kont_Del.setObjectName("pushButton_Kont_Del")
        self.horizontalLayout_2.addWidget(self.pushButton_Kont_Del)
        self.pushButton_Kont_Del.clicked.connect(self.deleteNummer)
        self.pushButton_Show_all = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_Show_all.setObjectName("pushButton_Show_all")
        self.horizontalLayout_2.addWidget(self.pushButton_Show_all)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 290, 781, 151))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lHeader.setText(_translate("MainWindow", "Kontakliste Light"))
        self.labelVN.setText(_translate("MainWindow", "Vorname"))
        self.labelN.setText(_translate("MainWindow", "Nachname"))
        self.labelTel.setText(_translate("MainWindow", "Telefon"))
        self.pushButton_Hinzu.setText(_translate("MainWindow", "Kontakt hinzufügen"))
        self.pushButton_Kontakt_anzeigen.setText(_translate("MainWindow", "Kontakt anzeigen"))
        self.pushButton_Kont_Del.setText(_translate("MainWindow", "Kontakt löschen"))
        self.pushButton_Show_all.setText(_translate("MainWindow", "Show All"))



    """Constructor zur Vorbereitung des Datenzugriffs"""
    def __init__(self): #übernimmt keine Argumente, leerer Konstruktor, der intern alles bereitstellt
        self.conn = sqlite3.connect('contacts.db')    #handle zur Datenbank "contacts"
        self.c = self.conn.cursor()         #cursor c übergibt die anfrage an die db


    """Destructor zum schließen(freigeben) der Datenbankverbindung"""
    def __exit__(self, *args):
        print('__exit__')
        self.connection.close()


    """ Fuegt der DB einen neuen Eintrag hinzu. """
    def addNummer(self,vorname,name,nummer):
        #Vorbedingung_setzen
        self.conn = sqlite3.connect('contacts.db')    #handle zur Datenbank "contacts"
        self.c = self.conn.cursor()         #cursor c übergibt die anfrage an die db

        self.vorname =  super().setupUI.lineEdit_Vorname
        self.name  = super().setupUi.lineEdit_Name
        self.telefon = super().setupUi.lineEdit_Telefon
        assert(isinstance(nummer,str))      #prüft ob einträge vom typ string sind,
        assert(isinstance(vorname,str))     #wenn nicht bricht das programm ab um fehler zu vermeiden
        assert(isinstance(name,str))        #Python typisiert Datentypen schwach bis gar nicht
        params = (vorname, name, nummer)    #Tupel, einfacher zum einbinden in die SQL-Anfrage
        sql = "INSERT INTO contacts VALUES (NULL,?,?,?)" #erster Eintrag is die ID und wird von der DB erstellt
        self.c.execute(sql,params)          #cursor c wird Tupel params übergeben
        self.conn.commit()         #damit Aenderungen in der DB ausgeführt werden, wird der Handler genutzt(commit)
        self.connection.close()


    """Liefert Telefonnummen zu gegebenen Vorname und name"""
    def getNummer(self,vorname,name):   #gibt Liste der Telefonnummern aus
        self.conn = sqlite3.connect('contacts.db')    #handle zur Datenbank "contacts"
        self.c = self.conn.cursor()         #cursor c übergibt die anfrage an die db

        #Vorbedingung_setzen
        self.vorname = super().setupUi.lineEdit_Vorname
        self.name = super().setupUi.lineEdit_Name
        assert(isinstance(name,str))      #prüft ob einträge vom typ string sind
        assert(isinstance(vorname,str))
        liste = []                          #benötigt um Tupels in Liste von Strings umzuwandeln
        params = (vorname,name)
        sql = "SELECT telefon FROM contacts WHERE vorname = ? AND name = ?"
        self.c.execute(sql,params)
        for row in self.c.fetchall():       #der einzelne Datensatz von self.c (Liste von tTupel) wird in Liste geschrieben
            liste.append(str(row[0]))
            self.connection.close()


    """Löscht Datensatz zur angegebenen Telefonnummer"""
    def deleteNummer(self,nummer):
        self.conn = sqlite3.connect('contacts.db')    #handle zur Datenbank "contacts"
        self.c = self.conn.cursor()         #cursor c übergibt die anfrage an die db

        #Vorbedingung_setzen
        self.nummer = super().setupUi.lineEdit_Telefon
        assert(isinstance(nummer,str))
        params = (nummer,)                  #Tupel mit nur einem Eintrag muss mit komma geschrieben werden
        sql = "DELETE FROM contacts WHERE telefon = ?"
        self.c.execute(sql,params)
        self.conn.commit()          #wichtig damit die änderung in der DB datei geschrieben wird
        self.connection.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
