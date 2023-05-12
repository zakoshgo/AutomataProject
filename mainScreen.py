# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import CFG_to_PDA
import NFA_and_ENFA_to_DFA

import graphviz

Epsilon_NFA_flag = 0


class Ui_FirstWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 346)
        MainWindow.setToolTipDuration(0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)  # directed graph push button
        self.pushButton.clicked.connect(self.directedButtonClick)
        self.pushButton.setGeometry(QtCore.QRect(110, 180, 141, 81))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)  # undirected graph push button
        self.pushButton_2.clicked.connect(self.undirectedButtonClick)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 180, 141, 81))

        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 601, 61))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automata Project"))
        self.pushButton.setText(_translate("MainWindow", "Convert NFA To DFA"))
        self.pushButton_2.setText(_translate("MainWindow", "Convert Context \nFree Grammar To PDA"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Choose the problem type you want to solve</span></p></body></html>"))

    # the function that opens the graph window when any of the choices is clicked
    def directedButtonClick(self):
        self.w = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.w)
        self.w.show()
        MainWindow.close()

    def undirectedButtonClick(self):
        self.w = QtWidgets.QMainWindow()
        self.ui = Ui_PDAscreen()
        self.ui.setupUi(self.w)
        self.w.show()
        MainWindow.close()


class Ui_PDAscreen(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 857)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 461, 801))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(140, 110, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.addRule(self.lineEdit.text()))

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 180, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 180, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.add_nonterm_userdef(self.lineEdit_2.text()))

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 230, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(230, 230, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 230, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.add_term_userdef(self.lineEdit_3.text()))

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(230, 280, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(lambda: self.set_start_symbol(self.lineEdit_4.text()))

        self.convertbtn = QtWidgets.QPushButton(self.frame)
        self.convertbtn.setGeometry(QtCore.QRect(350, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.convertbtn.setFont(font)
        self.convertbtn.setText("Convert")
        self.convertbtn.setObjectName("pushButton_4")
        self.convertbtn.clicked.connect(lambda: self.convert_to_PDA())

        self.rulesLabel = QtWidgets.QLabel(self.frame)
        self.rulesLabel.setGeometry(QtCore.QRect(20, 400, 421, 200))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.rulesLabel.setFont(font)
        self.rulesLabel.setStyleSheet("border: 2px solid lightgrey;")
        self.rulesLabel.setText("Rules:\n")
        self.rulesLabel.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.rulesLabel.setObjectName("label_8")

        self.nonTermDeflbl = QtWidgets.QLabel(self.frame)
        self.nonTermDeflbl.setGeometry(QtCore.QRect(20, 600, 421, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.nonTermDeflbl.setFont(font)
        self.nonTermDeflbl.setStyleSheet("border: 2px solid lightgrey;")
        self.nonTermDeflbl.setText("Non Terminal Definitions:\n")
        self.nonTermDeflbl.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.nonTermDeflbl.setObjectName("label_8")

        self.TermDeflbl = QtWidgets.QLabel(self.frame)
        self.TermDeflbl.setGeometry(QtCore.QRect(20, 670, 421, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.TermDeflbl.setFont(font)
        self.TermDeflbl.setStyleSheet("border: 2px solid lightgrey;")
        self.TermDeflbl.setText("Terminal Definitions:\n")
        self.TermDeflbl.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.TermDeflbl.setObjectName("label_8")

        self.TermDeflbl = QtWidgets.QLabel(self.frame)
        self.TermDeflbl.setGeometry(QtCore.QRect(20, 670, 421, 70))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.TermDeflbl.setFont(font)
        self.TermDeflbl.setStyleSheet("border: 2px solid lightgrey;")
        self.TermDeflbl.setText("Terminal Definitions:\n")
        self.TermDeflbl.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.TermDeflbl.setObjectName("label_8")

        self.startlbl = QtWidgets.QLabel(self.frame)
        self.startlbl.setGeometry(QtCore.QRect(20, 740, 421, 50))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.startlbl.setFont(font)
        self.startlbl.setStyleSheet("border: 2px solid lightgrey;")
        self.startlbl.setText("Start Symbol:\n")
        self.startlbl.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.startlbl.setObjectName("label_8")

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(460, 0, 661, 801))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(220, 20, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.showWarning()

    rules = []
    nonterm_userdef = []
    term_userdef = []
    start_symbol = ''
    symbol_set_flag = 0

    def showWarning(self, extra=""):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Very Important")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setInformativeText("!! # symbolizes the epsilon!!")
        msg.setDetailedText(extra)
        x = msg.exec_()

    def showError(self, err_msg, extra=""):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid Operation")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setInformativeText(err_msg)
        msg.setDetailedText(extra)
        x = msg.exec_()

    def addRule(self, rule):
        self.rules.append(rule)
        self.rulesLabel.setText(self.rulesLabel.text() + rule + "\n")
        self.rulesLabel.update()
        print(self.rules)

    def add_nonterm_userdef(self, definition):
        self.nonterm_userdef.append(definition)
        self.nonTermDeflbl.setText(self.nonTermDeflbl.text() + definition + " ")
        self.nonTermDeflbl.update()
        print(self.nonterm_userdef)

    def add_term_userdef(self, definition):
        self.term_userdef.append(definition)
        self.TermDeflbl.setText(self.TermDeflbl.text() + definition + " ")
        self.TermDeflbl.update()
        print(self.term_userdef)

    def set_start_symbol(self, symbol):
        if self.symbol_set_flag == 0:
            self.start_symbol = symbol
            self.symbol_set_flag = 1
            self.startlbl.setText(self.startlbl.text() + symbol)
            print(self.start_symbol)
        else:
            self.showError("start symbol already set")

    def convert_to_PDA(self):
        try:
            CFG_to_PDA.Push_down(self.rules, self.nonterm_userdef, self.start_symbol, self.term_userdef)
            PDA_graph = graphviz.Digraph(comment='pda', format='png')
            print("loop Incoming")
            for tran in CFG_to_PDA.transitions:
                print("loop entered")
                for n in CFG_to_PDA.transitions[tran]:
                    PDA_graph.edge('' + tran[0], '' + n[2], label='' + tran[1] + ',' + n[0] + '->' + n[1])
                    print(PDA_graph)

            PDA_graph.render(directory='PDA', view=True).replace('\\', '/')
        except Exception as err:
            print(str(err))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Add a rule:"))
        self.label_2.setText(_translate("MainWindow", "Context Free Grammer"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Set Non Terminal Definition:"))
        self.pushButton_2.setText(_translate("MainWindow", "Set"))
        self.label_4.setText(_translate("MainWindow", "Set Terminal Definition:"))
        self.pushButton_3.setText(_translate("MainWindow", "Set"))
        self.label_5.setText(_translate("MainWindow", "Set Start Symbol:"))
        self.pushButton_4.setText(_translate("MainWindow", "Add"))
        self.label_7.setText(_translate("MainWindow", "PushDown Automata"))


class Ui_SecondWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(622, 346)
        MainWindow.setToolTipDuration(0)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)  # directed graph push button
        self.pushButton.clicked.connect(self.directedButtonClick)
        self.pushButton.setGeometry(QtCore.QRect(110, 180, 141, 81))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)  # undirected graph push button
        self.pushButton_2.clicked.connect(self.undirectedButtonClick)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 180, 141, 81))

        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 601, 61))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Automata Project"))
        self.pushButton.setText(_translate("MainWindow", "Regular NFA"))
        self.pushButton_2.setText(_translate("MainWindow", "Epsilon NFA"))
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">What type of NFA will you use?</span></p></body></html>"))

    # the function that opens the graph window when any of the choices is clicked
    def directedButtonClick(self):
        global Epsilon_NFA_flag
        Epsilon_NFA_flag = 0
        MainWindow.close()
        self.w = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.w)
        self.w.show()

    def undirectedButtonClick(self):
        global Epsilon_NFA_flag
        Epsilon_NFA_flag = 1
        MainWindow.close()
        self.w = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.w)
        self.w.show()


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 853)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 791))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 40, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(50, 90, 211, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.addState(self.lineEdit.text()))

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 140, 321, 16))
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 200, 121, 31))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 240, 121, 31))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(10, 240, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 280, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 280, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 330, 211, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(
            lambda: self.addTransition(self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text()))

        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setGeometry(QtCore.QRect(0, 380, 321, 16))
        self.line_5.setLineWidth(2)
        self.line_5.setMidLineWidth(0)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(10, 400, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.startStateIN = QtWidgets.QLineEdit(self.frame)
        self.startStateIN.setGeometry(QtCore.QRect(100, 400, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startStateIN.setFont(font)
        self.startStateIN.setText("")
        self.startStateIN.setObjectName("startStateIN")

        self.StartStateButton = QtWidgets.QPushButton(self.frame)
        self.StartStateButton.setGeometry(QtCore.QRect(230, 400, 70, 31))
        self.StartStateButton.setObjectName("StartStateButton")
        self.StartStateButton.clicked.connect(lambda: self.set_start_state(self.startStateIN.text()))

        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 440, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.FinalStateIN = QtWidgets.QLineEdit(self.frame)
        self.FinalStateIN.setGeometry(QtCore.QRect(100, 440, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.FinalStateIN.setFont(font)
        self.FinalStateIN.setText("")
        self.FinalStateIN.setObjectName("FinalStateIN")

        self.FinalStateButton = QtWidgets.QPushButton(self.frame)
        self.FinalStateButton.setGeometry(QtCore.QRect(230, 440, 70, 31))
        self.FinalStateButton.setObjectName("FinalStateButton")
        self.FinalStateButton.clicked.connect(lambda: self.set_final_state(self.FinalStateIN.text()))

        self.alphalbl = QtWidgets.QLabel(self.frame)
        self.alphalbl.setGeometry(QtCore.QRect(10, 480, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.alphalbl.setFont(font)
        self.alphalbl.setText("Set Alpha:")
        self.alphalbl.setObjectName("label_8")

        self.alphaIN = QtWidgets.QLineEdit(self.frame)
        self.alphaIN.setGeometry(QtCore.QRect(100, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.alphaIN.setFont(font)
        self.alphaIN.setText("")
        self.alphaIN.setObjectName("alphaIN")

        self.setAlphaButton = QtWidgets.QPushButton(self.frame)
        self.setAlphaButton.setGeometry(QtCore.QRect(230, 480, 70, 31))
        self.setAlphaButton.setObjectName("setAlphaButton")
        self.setAlphaButton.setText("set")
        self.setAlphaButton.clicked.connect(lambda: self.set_alpha(self.alphaIN.text()))

        self.NFAstartlbl = QtWidgets.QLabel(self.frame)
        self.NFAstartlbl.setGeometry(QtCore.QRect(10, 520, 300, 31))
        self.NFAstartlbl.setText("NFA start state: ")

        self.NFAfinallbl = QtWidgets.QLabel(self.frame)
        self.NFAfinallbl.setGeometry(QtCore.QRect(10, 540, 300, 31))
        self.NFAfinallbl.setText("NFA final states: ")

        self.graphAlphalbl = QtWidgets.QLabel(self.frame)
        self.graphAlphalbl.setGeometry(QtCore.QRect(10, 560, 300, 31))
        self.graphAlphalbl.setText("alpha: ")

        self.DFAstartlbl = QtWidgets.QLabel(self.frame)
        self.DFAstartlbl.setGeometry(QtCore.QRect(10, 580, 300, 31))
        self.DFAstartlbl.setText("DFA start state: ")

        self.DFAfinallbl = QtWidgets.QLabel(self.frame)
        self.DFAfinallbl.setGeometry(QtCore.QRect(10, 600, 300, 31))
        self.DFAfinallbl.setText("DFA final states: ")

        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setGeometry(QtCore.QRect(0, 680, 321, 16))
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(0)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 700, 211, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda: self.convert())

        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setGeometry(QtCore.QRect(0, 750, 321, 16))
        self.line_3.setLineWidth(2)
        self.line_3.setMidLineWidth(0)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setGeometry(QtCore.QRect(310, 0, 20, 791))
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout.addWidget(self.frame)

        self.NFAframe = QtWidgets.QFrame(self.centralwidget)
        self.NFAframe.setGeometry(QtCore.QRect(320, 0, 801, 391))
        self.NFAframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NFAframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NFAframe.setObjectName("NFAframe")

        self.pixmap = QPixmap()
        self.imgLabel = QtWidgets.QLabel(self.NFAframe)
        self.imgLabel.setPixmap(self.pixmap)
        self.imgLabel.setFixedSize(800, 390)

        self.DFAframe = QtWidgets.QFrame(self.centralwidget)
        self.DFAframe.setGeometry(QtCore.QRect(320, 390, 801, 401))
        self.DFAframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DFAframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DFAframe.setObjectName("DFAframe")

        self.dfa_pixmap = QPixmap()
        self.dfa_img_label = QtWidgets.QLabel(self.DFAframe)
        self.dfa_img_label.setPixmap(self.dfa_pixmap)
        self.dfa_img_label.setFixedSize(800, 390)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.showWarning()

    def showWarning(self, extra=""):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Very Important")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setInformativeText("ADD ALL STATES BEFORE ADDING TRANSITIONS\n ALL STATE NAMES MUST HAVE CONSISTANT SIZE\n!! ^ symbolizes the epsilon!!")
        msg.setDetailedText(extra)
        x = msg.exec_()

    def showError(self, err_msg, extra=""):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Invalid Operation")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setInformativeText(err_msg)
        msg.setDetailedText(extra)
        x = msg.exec_()

    NFAgraph = graphviz.Digraph(comment='NFAgraph', format='png')

    def addState(self, stateName):
        for state in NFA_and_ENFA_to_DFA.states:
            if state == stateName:
                self.showError("state already added")
                return

        NFA_and_ENFA_to_DFA.states.add(stateName)
        self.NFAgraph.node(stateName)
        self.NFAgraph.render(directory='doctest-output').replace('\\', '/')
        self.imgLabel.destroy()
        self.NFAframe.close()

        def ontimeout():
            self.pixmap = QPixmap("doctest-output/Digraph.gv.png")
            self.imgLabel.setPixmap(self.pixmap)
            self.imgLabel.show()
            self.NFAframe.show()
            MainWindow.update()

        self.__timer = QTimer()
        self.__timer.timeout.connect(ontimeout)
        self.__timer.start(2000)

        print(self.NFAgraph)

    def addTransition(self, state1, state2, transition):
        try:
            new_key = (state1, transition)
            value = {state2}
            for key in NFA_and_ENFA_to_DFA.transition.keys():
                if key == new_key:
                    value.update(NFA_and_ENFA_to_DFA.transition[key])

            NFA_and_ENFA_to_DFA.transition[new_key] = value
            print(NFA_and_ENFA_to_DFA.transition)
            self.NFAgraph.edge(state1, state2, label=transition)
            self.NFAgraph.render(directory='doctest-output').replace('\\', '/')
            self.imgLabel.destroy()
            self.NFAframe.close()

            def ontimeout():
                self.pixmap = QPixmap("doctest-output/Digraph.gv.png")
                self.imgLabel.setPixmap(self.pixmap)
                self.imgLabel.show()
                self.NFAframe.show()
                MainWindow.update()

            self.__timer = QTimer()
            self.__timer.timeout.connect(ontimeout)
            self.__timer.start(2000)

            print(self.NFAgraph)
        except Exception as err:
            print(str(err))

    def set_start_state(self, start_state):
        for state in NFA_and_ENFA_to_DFA.states:
            if state == start_state:
                NFA_and_ENFA_to_DFA.initialState = start_state
                self.DFAstartlbl.setText(self.DFAstartlbl.text()+start_state)
                self.NFAstartlbl.setText(self.NFAstartlbl.text()+start_state)
                print(NFA_and_ENFA_to_DFA.initialState)
                return

        self.showError("state not found")

    def set_final_state(self, final_state):
        for state in NFA_and_ENFA_to_DFA.finalState:
            if state == final_state:
                self.showError("this final state is already set")
                return
        for state in NFA_and_ENFA_to_DFA.states:
            if state == final_state:
                NFA_and_ENFA_to_DFA.finalState.add(final_state)
                self.DFAfinallbl.setText(self.DFAfinallbl.text()+final_state+" ")
                print(NFA_and_ENFA_to_DFA.finalState)
                return

        self.showError("state not found")

    def set_alpha(self, alpha_input):

        for alpha in NFA_and_ENFA_to_DFA.alpha:
            if alpha == alpha_input:
                self.showError("this alpha is already set")
                return

        if len(NFA_and_ENFA_to_DFA.alpha) == 2:
            self.showError("no more can be added")
            return
        self.graphAlphalbl.setText(self.graphAlphalbl.text()+alpha_input+" ")
        NFA_and_ENFA_to_DFA.alpha.add(alpha_input)
        print(NFA_and_ENFA_to_DFA.alpha)

    def convert(self):
        if Epsilon_NFA_flag == 1:
            output, dfa_final_states = NFA_and_ENFA_to_DFA.ENFA_DFA(NFA_and_ENFA_to_DFA.transition,
                                                                    NFA_and_ENFA_to_DFA.states,
                                                                    NFA_and_ENFA_to_DFA.initialState,
                                                                    NFA_and_ENFA_to_DFA.finalState)
        else:
            output, dfa_final_states = NFA_and_ENFA_to_DFA.NFA_to_DFA(NFA_and_ENFA_to_DFA.states,
                                                                      NFA_and_ENFA_to_DFA.alpha,
                                                                      NFA_and_ENFA_to_DFA.transition,
                                                                      NFA_and_ENFA_to_DFA.finalState,
                                                                      NFA_and_ENFA_to_DFA.initialState)
        for state in dfa_final_states:
            self.DFAfinallbl.setText(self.DFAfinallbl.text() + state + " ")

        print(dfa_final_states)
        print(output)
        DFAgraph = graphviz.Digraph(comment="DFAgraph", format="png")
        for key in output:
            for nextState in output[key]:
                DFAgraph.edge(key[0],nextState, label=key[1])

        print(DFAgraph)
        DFAgraph.render(directory="DFA", view=True).replace('\\', '/')
        self.dfa_img_label.destroy()
        self.DFAframe.close()

        def ontimeout():
            self.dfa_pixmap = QPixmap("DFA/Digraph.gv.png")
            self.dfa_img_label.setPixmap(self.dfa_pixmap)
            self.dfa_img_label.show()
            self.DFAframe.show()
            MainWindow.update()

        self.__timer = QTimer()
        self.__timer.timeout.connect(ontimeout)
        self.__timer.start(2000)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "State Name:"))
        self.label_2.setText(_translate("MainWindow", "Add a State"))
        self.pushButton.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Add a State Transition"))
        self.label_4.setText(_translate("MainWindow", "From State:"))
        self.label_5.setText(_translate("MainWindow", "To State:"))
        self.label_6.setText(_translate("MainWindow", "Condition:"))
        self.label_7.setText(_translate("MainWindow", "Start State:"))
        self.label_8.setText(_translate("MainWindow", "Final State:"))
        self.pushButton_2.setText(_translate("MainWindow", "Add"))
        self.pushButton_3.setText(_translate("MainWindow", "Convert to DFA"))
        self.StartStateButton.setText(_translate("MainWindow", "Set"))
        self.FinalStateButton.setText(_translate("MainWindow", "Set"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FirstWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
