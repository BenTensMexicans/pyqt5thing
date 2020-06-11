from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QPushButton, QMessageBox
import sys
import socket
import threading
import time
codes = {"msg":"222", "challenge":"798", "error":"545", "throw":"877", "connectr":"133", "done": "099","aord":"344"}

class Ui_NameChoose(object):
    def setupUi(self, NameChoose):
        NameChoose.setObjectName("NameChoose")
        NameChoose.resize(153, 77)
        NameChoose.setFixedSize(153,77)
        self.entername = QtWidgets.QLineEdit(NameChoose)
        self.entername.setGeometry(QtCore.QRect(20, 40, 113, 20))
        self.entername.setObjectName("entername")
        self.label = QtWidgets.QLabel(NameChoose)
        self.label.setGeometry(QtCore.QRect(40, 10, 71, 16))
        self.label.setObjectName("label")

        self.retranslateUi(NameChoose)
        QtCore.QMetaObject.connectSlotsByName(NameChoose)

        self.c = socket.socket()
        self.c.connect(("107.202.105.8", 8888))
        self.c.send(bytes("197884", "utf-8"))
        print(self.c)
        self.entername.returnPressed.connect(self.openwin)



    def retranslateUi(self, NameChoose):
        _translate = QtCore.QCoreApplication.translate
        NameChoose.setWindowTitle(_translate("NameChoose", "RPS"))
        self.entername.setPlaceholderText(_translate("NameChoose", "Ex: John"))
        self.label.setText(_translate("NameChoose", " Choose name"))


    def openwin(self):
        name = str(self.entername.text())
        self.c.send(bytes(str(name),"utf-8"))
        if self.c.recv(2048).decode() == "!GOOD":
            global window
            global ui
            window = QtWidgets.QMainWindow()
            ui = Ui_MainWindow()
            ui.setupUi(window, self.c)
            NameChoose.hide()
            window.show()
        else:
            msg = QMessageBox()
            print(type(msg))
            msg.setWindowTitle("Error")
            msg.setText("The name \"{}\" is already taken!".format(name))
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, c):
        self.c = c
        print (c)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 592)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setFixedSize(800,592)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/Untitled-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 291, 551))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 549))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.conlist = QtWidgets.QListView(self.scrollAreaWidgetContents)
        self.conlist.setGeometry(QtCore.QRect(-1, -1, 291, 551))
        self.conlist.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.conlist.setObjectName("conlist")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.send = QtWidgets.QLineEdit(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(310, 530, 481, 20))
        self.send.setObjectName("send")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(310, 0, 481, 521))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 479, 519))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.chat = QtWidgets.QTextEdit(self.scrollAreaWidgetContents_2)
        self.chat.setGeometry(QtCore.QRect(0, 0, 481, 521))
        self.chat.setReadOnly(True)
        self.chat.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.chat.setObjectName("chat")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuInfo = QtWidgets.QMenu(self.menubar)
        self.menuInfo.setObjectName("menuInfo")
        self.menuMade_by = QtWidgets.QMenu(self.menuInfo)
        self.menuMade_by.setObjectName("menuMade_by")
        self.menuHelp = QtWidgets.QMenu(self.menuInfo)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionBen_W = QtWidgets.QAction(MainWindow)
        self.actionBen_W.setObjectName("actionBen_W")
        self.actionNo_help_for_now = QtWidgets.QAction(MainWindow)
        self.actionNo_help_for_now.setObjectName("actionNo_help_for_now")
        self.menuMade_by.addAction(self.actionBen_W)
        self.menuHelp.addAction(self.actionNo_help_for_now)
        self.menuInfo.addAction(self.menuMade_by.menuAction())
        self.menuInfo.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.thread = QtCore.QThreadPool()
        self.thread.start(self.reciever())


        self.send.returnPressed.connect(self.sendmsg)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RPS"))
        self.send.setPlaceholderText(_translate("MainWindow", "Send message...."))
        self.chat.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuInfo.setTitle(_translate("MainWindow", "Info"))
        self.menuMade_by.setTitle(_translate("MainWindow", "Made by"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionBen_W.setText(_translate("MainWindow", "Ben W"))
        self.actionNo_help_for_now.setText(_translate("MainWindow", "No help for now :("))

    def sendmsg(self):
        print("asd")
        if self.send.text() is not "" and self.send.text():
            self.c.send(bytes(codes["msg"]+self.send.text(), "utf-8"))
            self.send.clear()


    def reciever(self):
        while True:
            msg = self.c.recv(2048).decode("utf-8")
            if msg:
                if msg[:3] == codes["msg"]:
                    print (msg)
                    self.chat.setPlainText(self.chat.toPlainText() + "{}".format(msg[3:]))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    NameChoose = QtWidgets.QMainWindow()
    ui = Ui_NameChoose()
    ui.setupUi(NameChoose)
    NameChoose.show()
    sys.exit(app.exec_())
