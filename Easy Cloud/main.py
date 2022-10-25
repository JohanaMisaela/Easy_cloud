import sys
from pyrebase import *

import os
from firebase import firebase
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QPushButton, QLabel
from PyQt5.uic import loadUi
from PIL import Image


firebaseConfig = {
    "apiKey": "AIzaSyBwdhi8tuPnCPqYJOXb39NVHzqaHgNP-h0",
    "authDomain": "easy-cloud-82e1a.firebaseapp.com",
    "databaseURL": "https://easy-cloud-82e1a-default-rtdb.firebaseio.com",
    "projectId": "easy-cloud-82e1a",
    "storageBucket": "easy-cloud-82e1a.appspot.com",
    "messagingSenderId": "418228642810",
    "appId": "1:418228642810:web:ea4a1948843f90636eba43",
    "measurementId": "G-N8NJ808W6G"}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        self.invalid.setVisible(False)

    def loginfunction(self):
        email = self.email.text()
        password = self.password.text()
        try:
            auth.sign_in_with_email_and_password(email, password)
            main = Acceuil()
            widget.addWidget(main)
            widget.setCurrentIndex(widget.currentIndex() + 1)

        except:
            self.invalid.setVisible(True)

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("signin.ui", self)
        self.signinbutton.clicked.connect(self.createaccfunction)
        self.backbutton.clicked.connect(self.backfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.invalid.setVisible(False)

    def backfunction(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            try:
                auth.create_user_with_email_and_password(email, password)
                main = Acceuil()
                widget.addWidget(main)
                widget.setCurrentIndex(widget.currentIndex() + 1)

            except:
                self.invalid.setVisible(True)


class Acceuil(QDialog):
    def __init__(self):
        super(Acceuil, self).__init__()
        loadUi("main.ui", self)
        self.importecontact.clicked.connect(self.Importecontact)
        self.decbutton.clicked.connect(self.deconnecter)
        self.importeimage.clicked.connect(self.Chooseimage)

    def deconnecter(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Chooseimage(self):
        image = Image()
        widget.addWidget(image)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Importecontact(self):
        crud = Crud()
        widget.addWidget(crud)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Image(QDialog):
    def __init__(self):
        super(Image, self).__init__()
        loadUi("importimag.ui", self)
        self.choose = self.findChild(QPushButton, "choose")
        self.labelpath = self.findChild(QLabel, "labelpath")
        self.choose.clicked.connect(self.Chooseimage)
        self.goback.clicked.connect(self.Goback)
        self.inimage.clicked.connect(self.image)

    def image(self):
        affich = affichimage()
        widget.addWidget(affich)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Goback(self):
        main = Acceuil()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Chooseimage(self):
        fname = QFileDialog.getOpenFileName(self, 'open file')
        if fname:
            image = (os.path.basename(str(fname[0])))
            storage.child(image).put(fname[0])


class affichimage(QDialog):
    def __init__(self):
        super(affichimage, self).__init__()
        loadUi("afficheimg.ui", self)

    def load(self):
        from firebase import firebase
        firebase = firebase.FirebaseApplication('gs://easy-cloud-82e1a.appspot.com', None)
        image = firebase.get()
        type(image)

    def Goback(self):
        main = Acceuil()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Chooseimage(self):
        fname = QFileDialog.getOpenFileName(self, 'open file')
        if fname:
            image = (os.path.basename(str(fname[0])))
            storage.child(image).put(fname[0])


class Crud(QDialog):
    def __init__(self):
        super(Crud, self).__init__()
        loadUi("crud.ui", self)
        self.enregistrer.clicked.connect(self.enregistrerfunction)
        self.goback.clicked.connect(self.Goback)

    def Goback(self):
        main = Acceuil()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def enregistrerfunction(self):
        email = self.mail.toPlainText()
        nom = self.nom.toPlainText()
        prenom = self.prenom.toPlainText()
        numero = self.numero.toPlainText()
        addresse = self.addresse.toPlainText()

        data = {
            'nom': nom,
            'prenom': prenom,
            'numero': numero,
            'mail': email,
            'addresse': addresse
        }
        db.child("contact").push(data)
        voirlist = Voirlist()
        widget.addWidget(voirlist)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Voirlist(QDialog):
    def __init__(self):
        super(Voirlist, self).__init__()
        loadUi("voirlist.ui", self)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 200)
        self.tableWidget.setColumnWidth(4, 200)
        self.loaddata()

    def loaddata(self):
        from firebase import firebase
        firebase = firebase.FirebaseApplication('https://easy-cloud-82e1a-default-rtdb.firebaseio.com/', None)
        contacts = firebase.get('/contact/', '')
        values = []
        dico = list()
        for key, value in contacts.items():
            values.append(value)
        for i in values:
            dico.append(i)

        row = 0
        self.tableWidget.setRowCount(0)
        for key in dico:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(key["nom"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("prenom"))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem("numero"))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("mail"))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem("utfgjvbm"))
        row = row + 1


app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("Easy cloud - Easy Fast and Simple")
widget.setFixedWidth(1130)
widget.setFixedHeight(584)
widget.show()
app.exec()
