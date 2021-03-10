"""

GUI Calculator PyQt5

Copyright © 2021 xphreak5

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, 
distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

from PyQt5 import QtCore, QtGui, QtWidgets

# Main window
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(314, 392)
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Montserrat SemiBold")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button7.setGeometry(QtCore.QRect(30, 240, 31, 31))
        self.Button7.setObjectName("Button7")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(30, 190, 31, 31))
        self.Button4.setObjectName("Button4")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(30, 140, 31, 31))
        self.Button1.setObjectName("Button1")
        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button6.setGeometry(QtCore.QRect(150, 190, 31, 31))
        self.Button6.setObjectName("Button6")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(90, 140, 31, 31))
        self.Button2.setObjectName("Button2")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(150, 140, 31, 31))
        self.Button3.setObjectName("Button3")
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(90, 190, 31, 31))
        self.Button5.setObjectName("Button5")
        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button8.setGeometry(QtCore.QRect(90, 240, 31, 31))
        self.Button8.setObjectName("Button8")
        self.Button9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button9.setGeometry(QtCore.QRect(150, 240, 31, 31))
        self.Button9.setObjectName("Button9")
        self.ResultBar = QtWidgets.QLineEdit(self.centralwidget)
        self.ResultBar.setGeometry(QtCore.QRect(20, 50, 211, 51))
        self.ResultBar.setReadOnly(True)
        self.ResultBar.setObjectName("ResultBar")
        self.Button0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button0.setGeometry(QtCore.QRect(90, 290, 31, 31))
        self.Button0.setObjectName("Button0")
        self.ButtonPlus = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonPlus.setGeometry(QtCore.QRect(230, 140, 71, 31))
        self.ButtonPlus.setObjectName("ButtonPlus")
        self.ButtonMinus = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonMinus.setGeometry(QtCore.QRect(230, 180, 71, 31))
        self.ButtonMinus.setObjectName("ButtonMinus")
        self.ButtonMultiply = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonMultiply.setGeometry(QtCore.QRect(230, 220, 71, 31))
        self.ButtonMultiply.setObjectName("ButtonMultiply")
        self.ButtonDivide = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDivide.setGeometry(QtCore.QRect(230, 260, 71, 31))
        self.ButtonDivide.setObjectName("ButtonDivide")
        self.ButtonEquals = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonEquals.setGeometry(QtCore.QRect(120, 330, 181, 31))
        self.ButtonEquals.setObjectName("ButtonEquals")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 60, 71, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.operatorList = [" + ", " - ", " / ", " * "]
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainn()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button7.setText(_translate("MainWindow", "7"))
        self.Button4.setText(_translate("MainWindow", "4"))
        self.Button1.setText(_translate("MainWindow", "1"))
        self.Button6.setText(_translate("MainWindow", "6"))
        self.Button2.setText(_translate("MainWindow", "2"))
        self.Button3.setText(_translate("MainWindow", "3"))
        self.Button5.setText(_translate("MainWindow", "5"))
        self.Button8.setText(_translate("MainWindow", "8"))
        self.Button9.setText(_translate("MainWindow", "9"))
        self.Button0.setText(_translate("MainWindow", "0"))
        self.ButtonPlus.setText(_translate("MainWindow", "+"))
        self.ButtonMinus.setText(_translate("MainWindow", "-"))
        self.ButtonMultiply.setText(_translate("MainWindow", "*"))
        self.ButtonDivide.setText(_translate("MainWindow", "/"))
        self.ButtonEquals.setText(_translate("MainWindow", "="))
        self.pushButton.setText(_translate("MainWindow", "Clear"))


    # Text changer on resultbar
    def mixCocktailtext(self, content):
        global normaltext, text
        text = self.ResultBar.text()
        normaltext = text + content
        self.ResultBar.setText(normaltext)



    #Button click funcs
    def button1clicked(self):
        self.Button1.clicked.connect(lambda: self.mixCocktailtext("1"))
        
    def button2clicked(self):
        self.Button2.clicked.connect(lambda: self.mixCocktailtext("2"))

    def button3clicked(self):
        self.Button3.clicked.connect(lambda: self.mixCocktailtext("3"))
    
    def button4clicked(self):
        self.Button4.clicked.connect(lambda: self.mixCocktailtext("4"))

    def button5clicked(self):
        self.Button5.clicked.connect(lambda: self.mixCocktailtext("5"))

    def button6clicked(self):
        self.Button6.clicked.connect(lambda: self.mixCocktailtext("6"))

    def button7clicked(self):
        self.Button7.clicked.connect(lambda: self.mixCocktailtext("7"))

    def button8clicked(self):
        self.Button8.clicked.connect(lambda: self.mixCocktailtext("8"))

    def button9clicked(self):
        self.Button9.clicked.connect(lambda: self.mixCocktailtext("9"))

    def button0clicked(self):
        self.Button0.clicked.connect(lambda: self.mixCocktailtext("0"))

    def buttonplusclicked(self):
        self.ButtonPlus.clicked.connect(lambda: self.mixCocktailtext(" + "))

    def buttonminusclicked(self):
        self.ButtonMinus.clicked.connect(lambda: self.mixCocktailtext(" - "))
        
    def buttondivideclicked(self):
        self.ButtonDivide.clicked.connect(lambda: self.mixCocktailtext(" / "))

    def buttonmultiplyclicked(self):
        self.ButtonMultiply.clicked.connect(lambda: self.mixCocktailtext(" * "))

    def buttonclearclicked(self):
        self.pushButton.clicked.connect(lambda: self.ResultBar.setText(""))

        
    def mixCocktailtextt(self):
        global normaltext
        normaltext = self.ResultBar.text()
    

    def buttonequalsclicked(self):
        self.mixCocktailtextt()
        self.ButtonEquals.clicked.connect(lambda: self.stringSplitter())


    #Processes
    def stringSplitter(self):
        for i in self.operatorList:
            if i in normaltext and i == " + ":
                a = normaltext.split(i)
                b = int(a[0]) + int((a[1]))
                self.ResultBar.setText(str(b))
        
        for i in self.operatorList:
            if i in normaltext and i == " - ":
                a = normaltext.split(i)
                b = int(a[0]) - int((a[1]))
                self.ResultBar.setText(str(b))

        for i in self.operatorList:
            if i in normaltext and i == " * ":
                a = normaltext.split(i)
                b = int(a[0]) * int((a[1]))
                self.ResultBar.setText(str(b))

        for i in self.operatorList:
            if i in normaltext and i == " / ":
                a = normaltext.split(i)
                b = int(a[0]) / int((a[1]))
                self.ResultBar.setText(str(b))

    # Call funcs
    def mainn(self):
        self.buttonequalsclicked()
        self.button1clicked()
        self.button2clicked()
        self.button3clicked()
        self.button4clicked()
        self.button5clicked()
        self.button6clicked()
        self.button7clicked()
        self.button8clicked()
        self.button9clicked()
        self.button0clicked()
        self.buttonplusclicked()
        self.buttonminusclicked()
        self.buttondivideclicked()
        self.buttonmultiplyclicked()
        self.buttonclearclicked()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
