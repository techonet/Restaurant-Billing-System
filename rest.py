# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restaurant.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 761, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/restaurant.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 281, 51))
        font = QtGui.QFont()
        font.setFamily("eufm10")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 70, 301, 191))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.C1 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C1.setFont(font)
        self.C1.setStyleSheet("color: rgb(6, 73, 29);")
        self.C1.setObjectName("C1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.C1)
        self.C2 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C2.setFont(font)
        self.C2.setStyleSheet("color: rgb(6, 73, 29);")
        self.C2.setObjectName("C2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.C2)
        self.C3 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C3.setFont(font)
        self.C3.setStyleSheet("color: rgb(6, 73, 29);")
        self.C3.setObjectName("C3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.C3)
        self.C4 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C4.setFont(font)
        self.C4.setStyleSheet("color: rgb(6, 73, 29);")
        self.C4.setObjectName("C4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.C4)
        self.C5 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C5.setFont(font)
        self.C5.setStyleSheet("color: rgb(6, 73, 29);")
        self.C5.setObjectName("C5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.C5)
        self.C6 = QtWidgets.QCheckBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C6.setFont(font)
        self.C6.setStyleSheet("color: rgb(6, 73, 29);")
        self.C6.setObjectName("C6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.C6)
        self.S1 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.S1.setObjectName("S1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.S1)
        self.S2 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.S2.setObjectName("S2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.S2)
        self.S3 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.S3.setObjectName("S3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.S3)
        self.S4 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.S4.setObjectName("S4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.S4)
        self.S5 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.S5.setObjectName("S5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.S5)
        self.S6 = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.S6.setObjectName("S6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.S6)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(30, 260, 301, 61))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.B2 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.B2.setObjectName("B2")
        self.B2.clicked.connect(self.order)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.B2)
        self.B1 = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.B1.setObjectName("B1")
        self.B1.clicked.connect(self.clean)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.B1)
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(520, 170, 231, 83))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(239, 41, 41);")
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(246, 130, 130);")
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(164, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.T1 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.T1.setObjectName("T1")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.T1)
        self.CM1 = QtWidgets.QComboBox(self.formLayoutWidget_3)
        self.CM1.setObjectName("CM1")
        self.CM1.addItem("5")
        self.CM1.addItem("12")
        self.CM1.addItem("15")
        self.CM1.addItem("18")
        self.CM1.addItem("25")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CM1)
        self.T2 = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.T2.setObjectName("T2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.T2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Restaurant Billing"))
        self.label_2.setText(_translate("MainWindow", "Restaurant"))
        self.C1.setText(_translate("MainWindow", "Pizza :: 500 Rs."))
        self.C2.setText(_translate("MainWindow", "Burger :: 400 Rs."))
        self.C3.setText(_translate("MainWindow", "Pasta :: 300 Rs."))
        self.C4.setText(_translate("MainWindow", "Ice Cream :: 200 Rs."))
        self.C5.setText(_translate("MainWindow", "Coffee :: 100 Rs."))
        self.C6.setText(_translate("MainWindow", "Cold Drink :: 50 Rs."))
        self.B2.setText(_translate("MainWindow", "Order"))
        self.B1.setText(_translate("MainWindow", "Reset"))
        self.label_3.setText(_translate("MainWindow", "Bill :"))
        self.label_4.setText(_translate("MainWindow", "GST :"))
        self.label_5.setText(_translate("MainWindow", "Total Bill : "))

    def order(self):
        total = 0
        I1 = 0
        I2 = int(self.CM1.currentText())
        if(self.C1.isChecked() == True):
            I1 = int(self.S1.text())
            total = total + (I1 * 500)
        if(self.C2.isChecked() == True):
            I1 = int(self.S2.text())
            total = total + (I1 * 400)
        if(self.C3.isChecked() == True):
            I1 = int(self.S3.text())
            total = total + (I1 * 300)
        if(self.C4.isChecked() == True):
            I1 = int(self.S4.text())
            total = total + (I1 * 200)
        if(self.C5.isChecked() == True):
            I1 = int(self.S5.text())
            total = total + (I1 * 100)
        if(self.C6.isChecked() == True):
            I1 = int(self.S6.text())
            total = total + (I1 * 50)
        I3 = total + ((total*I2)/100)
        self.T1.setText(str(total))
        self.T2.setText(str(I3))
    def clean(self):
        self.C1.setChecked(False)
        self.C2.setChecked(False)
        self.C3.setChecked(False)
        self.C4.setChecked(False)
        self.C5.setChecked(False)
        self.C6.setChecked(False) 
        self.S1.setValue(0)
        self.S2.setValue(0)
        self.S3.setValue(0)
        self.S4.setValue(0)
        self.S5.setValue(0)
        self.S6.setValue(0)
        self.T1.setText("0")
        self.T2.setText("0")
    
import first_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
