# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Scraping_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(944, 565)
        Dialog.setStyleSheet("background-color:rgb(200, 200, 200)")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(140, 450, 431, 16))
        self.progressBar.setStyleSheet("background-color: rgb(9, 200, 171);\n"
"border-top-color: rgb(85, 170, 255);\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.datatable = QtWidgets.QTableWidget(Dialog)
        self.datatable.setGeometry(QtCore.QRect(140, 150, 701, 281))
        self.datatable.setStyleSheet("background-color: rgba(200, 191, 58,0.5);")
        self.datatable.setLineWidth(1)
        self.datatable.setAutoScrollMargin(16)
        self.datatable.setShowGrid(True)
        self.datatable.setRowCount(0)
        self.datatable.setColumnCount(7)
        self.datatable.setObjectName("datatable")
        item = QtWidgets.QTableWidgetItem()
        self.datatable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.datatable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.datatable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.datatable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.datatable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.datatable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.datatable.setHorizontalHeaderItem(6, item)
        self.ascending = QtWidgets.QRadioButton(Dialog)
        self.ascending.setGeometry(QtCore.QRect(340, 40, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ascending.setFont(font)
        self.ascending.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"font: 75 12pt \"Cambria\";\n"
"")
        self.ascending.setObjectName("ascending")
        self.descending = QtWidgets.QRadioButton(Dialog)
        self.descending.setGeometry(QtCore.QRect(340, 70, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.descending.setFont(font)
        self.descending.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"font: 75 12pt \"Cambria\";")
        self.descending.setObjectName("descending")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(340, 10, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"font: 75 12pt \"Cambria\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, 230, 120, 141))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.stop = QtWidgets.QPushButton(self.frame)
        self.stop.setGeometry(QtCore.QRect(0, 80, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.stop.setFont(font)
        self.stop.setAutoFillBackground(False)
        self.stop.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"font: 75 12pt \"Cambria\";")
        self.stop.setObjectName("stop")
        self.pause = QtWidgets.QPushButton(self.frame)
        self.pause.setGeometry(QtCore.QRect(0, 50, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pause.setFont(font)
        self.pause.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"font: 75 12pt \"Cambria\";")
        self.pause.setObjectName("pause")
        self.start = QtWidgets.QPushButton(self.frame)
        self.start.setGeometry(QtCore.QRect(2, 20, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.start.setFont(font)
        self.start.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"font: 75 12pt \"Cambria\";")
        self.start.setObjectName("start")
        self.data_amount = QtWidgets.QLabel(Dialog)
        self.data_amount.setGeometry(QtCore.QRect(140, 480, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.data_amount.setFont(font)
        self.data_amount.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"background-color: rgb(200, 196, 95);\n"
"")
        self.data_amount.setObjectName("data_amount")
        self.data_time = QtWidgets.QLabel(Dialog)
        self.data_time.setGeometry(QtCore.QRect(500, 480, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.data_time.setFont(font)
        self.data_time.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"background-color: rgb(200, 196, 95);\n"
"\n"
"")
        self.data_time.setObjectName("data_time")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 951, 571))
        self.label_5.setStyleSheet("background-image: url(:/newPics/Downloads/pexels-rovenimagescom-949587.jpg);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/newPics/Downloads/pexels-rovenimagescom-949587.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"background-image: url(:/newPics/Pictures/new_background.jpeg);\n"
"font: 75 italic 20pt \"Times New Roman\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.select_algorithm = QtWidgets.QComboBox(Dialog)
        self.select_algorithm.setGeometry(QtCore.QRect(590, 50, 131, 31))
        self.select_algorithm.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"font: 75 12pt \"Cambria\";")
        self.select_algorithm.setObjectName("select_algorithm")
        self.select_algorithm.addItem("")
        self.select_algorithm.addItem("")
        self.select_algorithm.addItem("")
        self.select_algorithm.addItem("")
        self.select_algorithm.addItem("")
        self.select_algorithm.addItem("")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(590, 20, 131, 21))
        self.label_6.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"font: 75 12pt \"Cambria\";")
        self.label_6.setObjectName("label_6")
        self.save_order = QtWidgets.QPushButton(Dialog)
        self.save_order.setGeometry(QtCore.QRect(450, 70, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.save_order.setFont(font)
        self.save_order.setStyleSheet("background-color: rgb(200, 196, 95);\n"
"font: 75 12pt \"Cambria\";")
        self.save_order.setObjectName("save_order")
        self.Namewise = QtWidgets.QPushButton(Dialog)
        self.Namewise.setGeometry(QtCore.QRect(60, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Namewise.setFont(font)
        self.Namewise.setStyleSheet("font: 75 12pt \"Cambria\";\n"
"background-color: rgb(65, 126, 200);")
        self.Namewise.setObjectName("Namewise")
        self.Pricewise = QtWidgets.QPushButton(Dialog)
        self.Pricewise.setGeometry(QtCore.QRect(190, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Pricewise.setFont(font)
        self.Pricewise.setStyleSheet("background-color: rgb(65, 126, 200);\n"
"font: 75 12pt \"Cambria\";")
        self.Pricewise.setObjectName("Pricewise")
        self.Formulawise = QtWidgets.QPushButton(Dialog)
        self.Formulawise.setGeometry(QtCore.QRect(440, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Formulawise.setFont(font)
        self.Formulawise.setStyleSheet("background-color: rgb(65, 126, 200);\n"
"font: 75 12pt \"Cambria\";")
        self.Formulawise.setObjectName("Formulawise")
        self.Companywise = QtWidgets.QPushButton(Dialog)
        self.Companywise.setGeometry(QtCore.QRect(310, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Companywise.setFont(font)
        self.Companywise.setStyleSheet("background-color: rgb(65, 126, 200);\n"
"font: 75 12pt \"Cambria\";")
        self.Companywise.setObjectName("Companywise")
        self.Dosewise = QtWidgets.QPushButton(Dialog)
        self.Dosewise.setGeometry(QtCore.QRect(560, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Dosewise.setFont(font)
        self.Dosewise.setStyleSheet("background-color: rgb(65, 126, 200);\n"
"font: 75 12pt \"Cambria\";")
        self.Dosewise.setObjectName("Dosewise")
        self.Categorywise = QtWidgets.QPushButton(Dialog)
        self.Categorywise.setGeometry(QtCore.QRect(670, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Categorywise.setFont(font)
        self.Categorywise.setStyleSheet("background-color: rgb(65, 126, 200);\n"
"font: 75 12pt \"Cambria\";")
        self.Categorywise.setObjectName("Categorywise")
        self.Quantitywise = QtWidgets.QPushButton(Dialog)
        self.Quantitywise.setGeometry(QtCore.QRect(780, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Quantitywise.setFont(font)
        self.Quantitywise.setStyleSheet("background-color: rgb(65, 126, 200);\n"
"font: 75 12pt \"Cambria\";")
        self.Quantitywise.setObjectName("Quantitywise")
        self.label_5.raise_()
        self.progressBar.raise_()
        self.datatable.raise_()
        self.ascending.raise_()
        self.descending.raise_()
        self.label.raise_()
        self.frame.raise_()
        self.data_amount.raise_()
        self.data_time.raise_()
        self.label_4.raise_()
        self.select_algorithm.raise_()
        self.label_6.raise_()
        self.save_order.raise_()
        self.Namewise.raise_()
        self.Pricewise.raise_()
        self.Formulawise.raise_()
        self.Companywise.raise_()
        self.Dosewise.raise_()
        self.Categorywise.raise_()
        self.Quantitywise.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.datatable.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Name"))
        item = self.datatable.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Price"))
        item = self.datatable.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Company Name"))
        item = self.datatable.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Formula"))
        item = self.datatable.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Dose Size"))
        item = self.datatable.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "Category"))
        item = self.datatable.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "Quantity"))
        self.ascending.setText(_translate("Dialog", "Ascending"))
        self.descending.setText(_translate("Dialog", "Descending"))
        self.label.setText(_translate("Dialog", "  Arrange in :"))
        self.stop.setText(_translate("Dialog", "Stop"))
        self.pause.setText(_translate("Dialog", "Pause/Resume"))
        self.start.setText(_translate("Dialog", "Start"))
        self.data_amount.setText(_translate("Dialog", "12456 of 1053782"))
        self.data_time.setText(_translate("Dialog", "10m 25s"))
        self.label_4.setText(_translate("Dialog", " Pharmacy Data Scraper"))
        self.select_algorithm.setItemText(0, _translate("Dialog", "Insertion Sort"))
        self.select_algorithm.setItemText(1, _translate("Dialog", "Selection Sort"))
        self.select_algorithm.setItemText(2, _translate("Dialog", "Merge Sort"))
        self.select_algorithm.setItemText(3, _translate("Dialog", "Quick Sort"))
        self.select_algorithm.setItemText(4, _translate("Dialog", "Bubble Sort"))
        self.select_algorithm.setItemText(5, _translate("Dialog", "Counting Sort"))
        self.label_6.setText(_translate("Dialog", " Select Algorithm :"))
        self.save_order.setText(_translate("Dialog", "OK"))
        self.Namewise.setText(_translate("Dialog", "Name_wise"))
        self.Pricewise.setText(_translate("Dialog", "Price_wise"))
        self.Formulawise.setText(_translate("Dialog", "Formula_wise"))
        self.Companywise.setText(_translate("Dialog", "Company_wise"))
        self.Dosewise.setText(_translate("Dialog", "Dose_wise"))
        self.Categorywise.setText(_translate("Dialog", "Category_wise"))
        self.Quantitywise.setText(_translate("Dialog", "Quantity_wise"))
import pics_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
