#self.importdossier.clicked.connect(self.Importedossier)


    def Importedossier(self):
        file= File()
        widget.addWidget(file)
        widget.setCurrentIndex(widget.currentIndex() + 1)

#class File(QDialog):
    #def __init__(self):
        #super(File, self).__init__()
        #("importfile.ui", self)
        #self.choosefile.clicked.connect(self.Choosefilef)
        #self.goback.clicked.connect(self.Goback)

    #def Choosefile:
    #def Goback(self):
        #main = Acceuil()
        ##widget.addWidget(main)
        #widget.setCurrentIndex(widget.currentIndex() + 1)


self.importdossier.clicked.connect(self.Importedossier)


    def Importedossier(self):
        file= File()
        widget.addWidget(file)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class File(QDialog):
    def __init__(self):
        super(File, self).__init__()
        ("importfile.ui", self)
        self.choosefile.clicked.connect(self.Choosefilef)
        self.goback.clicked.connect(self.Goback)

    def Choosefile(self):
        fname=QFileDialog.getOpenFileName(self, 'open file', "",)
        self.filename.setText(fname)