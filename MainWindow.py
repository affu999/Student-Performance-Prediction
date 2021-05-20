from PyQt5 import QtCore, QtGui, QtWidgets
from AdminLogin import WindowAdminLogin
from StudentLogin import WindowStudentLogin


class WindowMain(object):

    def funAdminLogin(self):
        self.winAdminLogin = QtWidgets.QMainWindow()
        self.uiAdminLogin = WindowAdminLogin()
        self.uiAdminLogin.setupUi(self.winAdminLogin)
        self.btnAdminLogin.setEnabled(False)
        self.winAdminLogin.show()


    def funStudentLogin(self):
        self.winStudentLogin = QtWidgets.QMainWindow()
        self.uiStudentLogin = WindowStudentLogin()
        self.uiStudentLogin.setupUi(self.winStudentLogin)
        self.btnStudentLogin.setEnabled(False)
        self.winStudentLogin.show()



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(339, 185)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnAdminLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdminLogin.setGeometry(QtCore.QRect(90, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAdminLogin.setFont(font)
        self.btnAdminLogin.setObjectName("btnAdminLogin")
        #------------------Adding Event to btnAdminLogin---------------------------
        self.btnAdminLogin.clicked.connect(self.funAdminLogin)
        #--------------------------------------------------------------------------
        self.btnStudentLogin = QtWidgets.QPushButton(self.centralwidget)
        self.btnStudentLogin.setGeometry(QtCore.QRect(90, 102, 141, 41))
        self.btnStudentLogin.setObjectName("btnStudentLogin")
        #------------------Adding Event to btnStudentLogin---------------------------
        self.btnStudentLogin.clicked.connect(self.funStudentLogin)
        #--------------------------------------------------------------------------
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Student Performance"))
        self.btnAdminLogin.setText(_translate("MainWindow", "Admin Login"))
        self.btnStudentLogin.setText(_translate("MainWindow", "Student Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WindowMain()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
