import sys

import pyrebase
import firebase
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

firebaseConfig = {
    "apiKey": "AIzaSyBwdhi8tuPnCPqYJOXb39NVHzqaHgNP-h0",
    "authDomain": "easy-cloud-82e1a.firebaseapp.com",
    "databaseURL": "https://easy-cloud-82e1a-default-rtdb.firebaseio.com",
    "projectId": "easy-cloud-82e1a",
    "storageBucket": "easy-cloud-82e1a.appspot.com",
    "messagingSenderId": "418228642810",
    "appId": "1:418228642810:web:ea4a1948843f90636eba43",
    "measurementId": "G-N8NJ808W6G"}

base = firebase.FirebaseApplication(
    'https://console.firebase.google.com/project/easy-cloud-82e1a/database/easy-cloud-82e1a-default-rtdb/data/~2F',
    None)

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
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.invalid.setVisible(False)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            try:
                auth.create_user_with_email_and_password(email, password)
                main = Acceuil()
                widget.addWidget(main)
                widget.setCurrentIndex(widget.currentIndex() + 1)
                email = email

            except:
                self.invalid.setVisible(True)


class Acceuil(QDialog):
    def __init__(self):
        super(Acceuil, self).__init__()
        loadUi("main.ui", self)
        self.importecontact.clicked.connect(self.Importecontact)

    def Importecontact(self):
        crud = Crud()
        widget.addWidget(crud)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Crud(QDialog):
    def __init__(self):
        super(Crud, self).__init__()
        loadUi("crud.ui", self)
        self.enregistrer.clicked.connect(self.enregistrerfunction)
        self.voirlist.clicked.connect(self.Voirlist)

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
              "mail": email,
              "addresse": addresse
          }
         db.child("contact").push(data)

class Voirlist(QDialog):
    def __init__(self):
        super(Voirlist, self).__init__()
        loadUi("voirlist.ui", self)

    def table(self):
        result= base.get('/contact', None)
        print(result)





app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setWindowTitle("Easy cloud - Easy Fast and Simple")
widget.setFixedWidth(1130)
widget.setFixedHeight(584)
widget.show()
app.exec()
