# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'control.ui'
#
# Created: Fri Sep 23 12:10:05 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(390, 420)
        Dialog.setMinimumSize(QtCore.QSize(382, 372))
        Dialog.setMaximumSize(QtCore.QSize(390, 420))
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Arx Control Center", None, QtGui.QApplication.UnicodeUTF8))
        Dialog.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 391, 421))
        self.tabWidget.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"background-color: rgb(62, 62, 62);\n"
"border-bottom-color: rgb(0, 0, 0);"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.frame_4 = QtGui.QFrame(self.tab_3)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 391, 401))
        self.frame_4.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(127, 0, 191, 255), stop:1 rgba(0, 0, 0, 255));"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.frame_5 = QtGui.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(90, 110, 211, 191))
        self.frame_5.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:reflect, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(78, 0, 118, 255), stop:1 rgba(0, 0, 0, 255));"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.label_3 = QtGui.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Moire"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);"))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pwBox = QtGui.QLineEdit(self.frame_5)
        self.pwBox.setGeometry(QtCore.QRect(20, 111, 171, 20))
        self.pwBox.setStyleSheet(_fromUtf8("background-color: rgb(247, 247, 247);"))
        self.pwBox.setObjectName(_fromUtf8("pwBox"))
        self.loginButton = QtGui.QPushButton(self.frame_5)
        self.loginButton.setGeometry(QtCore.QRect(60, 151, 91, 23))
        self.loginButton.setStyleSheet(_fromUtf8("background-color: rgb(93, 93, 93);"))
        self.loginButton.setText(QtGui.QApplication.translate("Dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.userBox = QtGui.QLineEdit(self.frame_5)
        self.userBox.setGeometry(QtCore.QRect(22, 41, 171, 20))
        self.userBox.setStyleSheet(_fromUtf8("background-color: rgb(247, 247, 247);"))
        self.userBox.setObjectName(_fromUtf8("userBox"))
        self.label_4 = QtGui.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(8, 80, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Moire"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);"))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 0, 391, 401))
        self.widget.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.166 rgba(70, 70, 70, 255), stop:0.333 rgba(0, 0, 0, 255), stop:0.488636 rgba(70, 70, 70, 255), stop:0.666 rgba(0, 0, 0, 255), stop:0.833 rgba(70, 70, 70, 255), stop:1 rgba(0, 0, 0, 255));"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.exitButton_2 = QtGui.QPushButton(self.widget)
        self.exitButton_2.setGeometry(QtCore.QRect(310, 340, 51, 23))
        self.exitButton_2.setStyleSheet(_fromUtf8("background-color: rgb(93, 93, 93);"))
        self.exitButton_2.setText(QtGui.QApplication.translate("Dialog", "Go", None, QtGui.QApplication.UnicodeUTF8))
        self.exitButton_2.setObjectName(_fromUtf8("exitButton_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 10, 311, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label.setMidLineWidth(-1)
        self.label.setText(QtGui.QApplication.translate("Dialog", "ArXBot Control Center", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(220, 340, 81, 22))
        self.comboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: a(0);"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "(Tasks)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Update List", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "DDOS", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Dialog", "SynFlood", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("Dialog", "SlowLoris", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("Dialog", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("Dialog", "Get", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(7, QtGui.QApplication.translate("Dialog", "Update Bot", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(8, QtGui.QApplication.translate("Dialog", "Run", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(9, QtGui.QApplication.translate("Dialog", "Vaccinate", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 351, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: rgb(70, 70, 70);"))
        self.lineEdit.setText(QtGui.QApplication.translate("Dialog", "                Bots                                      Task", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.line = QtGui.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(180, 80, 21, 221))
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"gridline-color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 0);\n"
"color: rgb(0, 255, 0);"))
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.output = QtGui.QLabel(self.widget)
        self.output.setGeometry(QtCore.QRect(20, 370, 341, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output.setFont(font)
        self.output.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.output.setText(QtGui.QApplication.translate("Dialog", " ", None, QtGui.QApplication.UnicodeUTF8))
        self.output.setObjectName(_fromUtf8("output"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 320, 71, 16))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Arguments:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.list = QtGui.QListWidget(self.widget)
        self.list.setGeometry(QtCore.QRect(20, 70, 351, 241))
        self.list.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(70, 70, 70, 255), stop:1 rgba(0, 0, 0, 255));\n"
"color: rgb(0, 255, 0);"))
        self.list.setObjectName(_fromUtf8("list"))
        self.argsBox = QtGui.QLineEdit(self.widget)
        self.argsBox.setGeometry(QtCore.QRect(20, 340, 191, 21))
        self.argsBox.setStyleSheet(_fromUtf8("background-color: rgb(222, 222, 222);"))
        self.argsBox.setText(_fromUtf8(""))
        self.argsBox.setObjectName(_fromUtf8("argsBox"))
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(180, 50, 20, 16))
        self.line_2.setAutoFillBackground(False)
        self.line_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"gridline-color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 255, 0);\n"
"color: rgb(0, 255, 0);"))
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.widget_2 = QtGui.QWidget(self.tab_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 391, 401))
        self.widget_2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.166 rgba(70, 70, 70, 255), stop:0.333 rgba(0, 0, 0, 255), stop:0.488636 rgba(70, 70, 70, 255), stop:0.666 rgba(0, 0, 0, 255), stop:0.833 rgba(70, 70, 70, 255), stop:1 rgba(0, 0, 0, 255));"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.detailsOutput = QtGui.QLabel(self.widget_2)
        self.detailsOutput.setGeometry(QtCore.QRect(30, 220, 341, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailsOutput.setFont(font)
        self.detailsOutput.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 255, 0);"))
        self.detailsOutput.setText(QtGui.QApplication.translate("Dialog", " ", None, QtGui.QApplication.UnicodeUTF8))
        self.detailsOutput.setObjectName(_fromUtf8("detailsOutput"))
        self.frame = QtGui.QFrame(self.widget_2)
        self.frame.setEnabled(False)
        self.frame.setGeometry(QtCore.QRect(20, 20, 171, 191))
        self.frame.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(70, 70, 70, 255), stop:1 rgba(0, 0, 0, 255));"))
        self.frame.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(70, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 255, 0);"))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "THIS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 120, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 255, 0);"))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "FEATURE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.frame_3 = QtGui.QFrame(self.widget_2)
        self.frame_3.setEnabled(False)
        self.frame_3.setGeometry(QtCore.QRect(20, 240, 341, 131))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(70, 70, 70, 255), stop:1 rgba(0, 0, 0, 255));"))
        self.frame_3.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.label_7 = QtGui.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(100, 50, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Century Gothic"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 255, 0);"))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "COMING SOON", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.frame_2 = QtGui.QFrame(self.widget_2)
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QtCore.QRect(200, 20, 161, 191))
        self.frame_2.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(70, 70, 70, 255), stop:1 rgba(0, 0, 0, 255));"))
        self.frame_2.setFrameShape(QtGui.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.output_5 = QtGui.QLabel(self.frame_2)
        self.output_5.setGeometry(QtCore.QRect(10, 50, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_5.setFont(font)
        self.output_5.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.output_5.setText(QtGui.QApplication.translate("Dialog", "OLD:", None, QtGui.QApplication.UnicodeUTF8))
        self.output_5.setObjectName(_fromUtf8("output_5"))
        self.oldPW = QtGui.QLineEdit(self.frame_2)
        self.oldPW.setGeometry(QtCore.QRect(50, 50, 101, 20))
        self.oldPW.setStyleSheet(_fromUtf8("background-color: rgb(221, 221, 221);"))
        self.oldPW.setObjectName(_fromUtf8("oldPW"))
        self.output_6 = QtGui.QLabel(self.frame_2)
        self.output_6.setGeometry(QtCore.QRect(10, 10, 141, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.output_6.setFont(font)
        self.output_6.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.output_6.setText(QtGui.QApplication.translate("Dialog", "PASSWORD CHANGER", None, QtGui.QApplication.UnicodeUTF8))
        self.output_6.setAlignment(QtCore.Qt.AlignCenter)
        self.output_6.setObjectName(_fromUtf8("output_6"))
        self.newPW = QtGui.QLineEdit(self.frame_2)
        self.newPW.setGeometry(QtCore.QRect(50, 80, 101, 20))
        self.newPW.setStyleSheet(_fromUtf8("background-color: rgb(221, 221, 221);"))
        self.newPW.setObjectName(_fromUtf8("newPW"))
        self.output_7 = QtGui.QLabel(self.frame_2)
        self.output_7.setGeometry(QtCore.QRect(10, 80, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_7.setFont(font)
        self.output_7.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.output_7.setText(QtGui.QApplication.translate("Dialog", "NEW:", None, QtGui.QApplication.UnicodeUTF8))
        self.output_7.setObjectName(_fromUtf8("output_7"))
        self.confirmNewPW = QtGui.QLineEdit(self.frame_2)
        self.confirmNewPW.setGeometry(QtCore.QRect(50, 110, 101, 20))
        self.confirmNewPW.setStyleSheet(_fromUtf8("background-color: rgb(221, 221, 221);"))
        self.confirmNewPW.setObjectName(_fromUtf8("confirmNewPW"))
        self.output_8 = QtGui.QLabel(self.frame_2)
        self.output_8.setGeometry(QtCore.QRect(10, 110, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_8.setFont(font)
        self.output_8.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.output_8.setText(QtGui.QApplication.translate("Dialog", "NEW:", None, QtGui.QApplication.UnicodeUTF8))
        self.output_8.setObjectName(_fromUtf8("output_8"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(40, 150, 75, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.pushButton.setText(QtGui.QApplication.translate("Dialog", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.widget_3 = QtGui.QWidget(self.tab_4)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 391, 401))
        self.widget_3.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.166 rgba(70, 70, 70, 255), stop:0.333 rgba(0, 0, 0, 255), stop:0.488636 rgba(70, 70, 70, 255), stop:0.666 rgba(0, 0, 0, 255), stop:0.833 rgba(70, 70, 70, 255), stop:1 rgba(0, 0, 0, 255));"))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.widget_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 371, 111))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 255, 0);"))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "URL Checker", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.output_4 = QtGui.QLabel(self.groupBox_2)
        self.output_4.setGeometry(QtCore.QRect(20, 20, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_4.setFont(font)
        self.output_4.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);"))
        self.output_4.setText(QtGui.QApplication.translate("Dialog", "URL:", None, QtGui.QApplication.UnicodeUTF8))
        self.output_4.setObjectName(_fromUtf8("output_4"))
        self.URLBox = QtGui.QLineEdit(self.groupBox_2)
        self.URLBox.setGeometry(QtCore.QRect(142, 20, 191, 20))
        self.URLBox.setStyleSheet(_fromUtf8("background-color: rgb(222, 222, 222);\n"
"color: rgb(0, 0, 0);"))
        self.URLBox.setObjectName(_fromUtf8("URLBox"))
        self.checkButton = QtGui.QPushButton(self.groupBox_2)
        self.checkButton.setGeometry(QtCore.QRect(250, 50, 81, 23))
        self.checkButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.checkButton.setText(QtGui.QApplication.translate("Dialog", "Check", None, QtGui.QApplication.UnicodeUTF8))
        self.checkButton.setObjectName(_fromUtf8("checkButton"))
        self.outputURLChecker = QtGui.QLabel(self.groupBox_2)
        self.outputURLChecker.setGeometry(QtCore.QRect(10, 80, 321, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(11)
        font.setItalic(True)
        self.outputURLChecker.setFont(font)
        self.outputURLChecker.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);"))
        self.outputURLChecker.setText(QtGui.QApplication.translate("Dialog", "Waiting for URL to check.", None, QtGui.QApplication.UnicodeUTF8))
        self.outputURLChecker.setAlignment(QtCore.Qt.AlignCenter)
        self.outputURLChecker.setObjectName(_fromUtf8("outputURLChecker"))
        self.groupBox = QtGui.QGroupBox(self.widget_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 371, 121))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(0, 255, 0);"))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Bot Builder", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.output_2 = QtGui.QLabel(self.groupBox)
        self.output_2.setGeometry(QtCore.QRect(20, 20, 41, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_2.setFont(font)
        self.output_2.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);"))
        self.output_2.setText(QtGui.QApplication.translate("Dialog", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.output_2.setObjectName(_fromUtf8("output_2"))
        self.output_3 = QtGui.QLabel(self.groupBox)
        self.output_3.setGeometry(QtCore.QRect(20, 50, 61, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.output_3.setFont(font)
        self.output_3.setStyleSheet(_fromUtf8("color: rgb(0, 255, 0);"))
        self.output_3.setText(QtGui.QApplication.translate("Dialog", "Mutex:", None, QtGui.QApplication.UnicodeUTF8))
        self.output_3.setObjectName(_fromUtf8("output_3"))
        self.ipBox = QtGui.QLineEdit(self.groupBox)
        self.ipBox.setGeometry(QtCore.QRect(140, 20, 191, 20))
        self.ipBox.setStyleSheet(_fromUtf8("background-color: rgb(222, 222, 222);\n"
"color: rgb(0, 0, 0);"))
        self.ipBox.setObjectName(_fromUtf8("ipBox"))
        self.mutexBox = QtGui.QLineEdit(self.groupBox)
        self.mutexBox.setGeometry(QtCore.QRect(140, 50, 191, 20))
        self.mutexBox.setStyleSheet(_fromUtf8("background-color: rgb(222, 222, 222);\n"
"color: rgb(0, 0, 0);"))
        self.mutexBox.setReadOnly(True)
        self.mutexBox.setObjectName(_fromUtf8("mutexBox"))
        self.ranMutexButton = QtGui.QPushButton(self.groupBox)
        self.ranMutexButton.setGeometry(QtCore.QRect(140, 80, 91, 23))
        self.ranMutexButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.ranMutexButton.setText(QtGui.QApplication.translate("Dialog", "Random Mutex", None, QtGui.QApplication.UnicodeUTF8))
        self.ranMutexButton.setObjectName(_fromUtf8("ranMutexButton"))
        self.buildButton = QtGui.QPushButton(self.groupBox)
        self.buildButton.setGeometry(QtCore.QRect(250, 80, 81, 23))
        self.buildButton.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);"))
        self.buildButton.setText(QtGui.QApplication.translate("Dialog", "Build", None, QtGui.QApplication.UnicodeUTF8))
        self.buildButton.setObjectName(_fromUtf8("buildButton"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.loginButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.sLogin)
        QtCore.QObject.connect(self.pwBox, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.loginButton.click)
        QtCore.QObject.connect(self.pwBox, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.loginButton.animateClick)
        QtCore.QObject.connect(self.exitButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.sGo)
        QtCore.QObject.connect(self.buildButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.sBuild)
        QtCore.QObject.connect(self.ranMutexButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.sRanMutex)
        QtCore.QObject.connect(self.checkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.sCheckURL)
        QtCore.QObject.connect(self.argsBox, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.exitButton_2.click)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.sNewPW)
        QtCore.QObject.connect(self.confirmNewPW, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.pushButton.click)
        QtCore.QObject.connect(self.pwBox, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), Dialog.sHidePW1)
        QtCore.QObject.connect(self.URLBox, QtCore.SIGNAL(_fromUtf8("returnPressed()")), self.checkButton.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.userBox, self.pwBox)
        Dialog.setTabOrder(self.pwBox, self.loginButton)
        Dialog.setTabOrder(self.loginButton, self.tabWidget)
        Dialog.setTabOrder(self.tabWidget, self.list)
        Dialog.setTabOrder(self.list, self.argsBox)

    def retranslateUi(self, Dialog):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Dialog", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Dialog", "Bot Control", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Dialog", "Account Details", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Dialog", "Tools", None, QtGui.QApplication.UnicodeUTF8))
