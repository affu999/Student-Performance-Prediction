from PyQt5 import QtCore, QtGui, QtWidgets
from AdminDashBoard import WindowAdminDashBoard
from functools import partial
import sqlite3
from PyQt5.QtWidgets import QMessageBox


class WindowAdminLogin(object):

    def login(self, MainWindow):
        try:
            con = sqlite3.connect("COLLEGE.db")
            cur = con.cursor()
            self.userName = self.txtUserName.text()
            self.password = self.txtPassword.text()
            query = "SELECT * FROM ADMIN WHERE NAME=? AND PASSWORD=?"
            data = cur.execute(query, (self.userName, self.password)).fetchall()
            if len(data) > 0:
                self.winAdminDashBoard = QtWidgets.QMainWindow()
                self.uiAdminDashBoard = WindowAdminDashBoard()
                self.uiAdminDashBoard.setupUi(self.winAdminDashBoard)
                MainWindow.setVisible(False)
                self.winAdminDashBoard.show()
            else:
                QMessageBox.warning(self.centralwidget, "Warning", "Invalid User!!!")
                # print("Invalid User!!!")
            cur.close()
            con.close()
        except:
            QMessageBox.warning(self.centralwidget, "Warning", "Could not Connect!!!")
            

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtUserName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtUserName.setGeometry(QtCore.QRect(250, 120, 341, 31))
        self.txtUserName.setObjectName("lineEdit")
        self.txtPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.txtPassword.setGeometry(QtCore.QRect(250, 190, 341, 31))
        self.txtPassword.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 260, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        #================Adding Event to Login button=======================

        self.pushButton.clicked.connect(partial(self.login, MainWindow))

        #===================================================================
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin Login"))
        self.label.setText(_translate("MainWindow", "Admin Login"))
        self.label_2.setText(_translate("MainWindow", "UserName"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.pushButton.setText(_translate("MainWindow", "Login"))


##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    MainWindow = QtWidgets.QMainWindow()
##    ui = WindowAdminLogin()
##    ui.setupUi(MainWindow)
##    MainWindow.show()
##    sys.exit(app.exec_())
