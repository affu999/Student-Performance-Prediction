from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from StudentDashBoard import WindowStudentDashBoard
import sqlite3

class WindowStudentLogin(object):

    def login(self, MainWindow):
        try:
            con = sqlite3.connect("COLLEGE.db")
            cur = con.cursor()
            self.rollNo = self.txtRollNo.text()
            self.name = self.txtName.text()
            query = "SELECT * FROM STUDENT WHERE ROLLNO=? AND NAME=?"
            data = cur.execute(query, (self.rollNo, self.name)).fetchall()
            if len(data) > 0:
                self.winStudentDashBoard = QtWidgets.QMainWindow()
                self.uiStudentDashBoard = WindowStudentDashBoard()
                self.uiStudentDashBoard.setupUi(self.winStudentDashBoard, int(self.rollNo))
                MainWindow.setVisible(False)
                self.winStudentDashBoard.show()
            else:
                print("Student Does Not Exist!!!")
        except:
            pass
        finally:
            cur.close()
            con.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 190, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtRollNo = QtWidgets.QLineEdit(self.centralwidget)
        self.txtRollNo.setGeometry(QtCore.QRect(250, 120, 341, 31))
        self.txtRollNo.setObjectName("lineEdit")
        self.txtName = QtWidgets.QLineEdit(self.centralwidget)
        self.txtName.setGeometry(QtCore.QRect(250, 190, 341, 31))
        self.txtName.setObjectName("lineEdit_2")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Login"))
        self.label.setText(_translate("MainWindow", "Student Login"))
        self.label_2.setText(_translate("MainWindow", "Student RollNo"))
        self.label_3.setText(_translate("MainWindow", "Student Name"))
        self.pushButton.setText(_translate("MainWindow", "Login"))


##if __name__ == "__main__":
##    import sys
##    app = QtWidgets.QApplication(sys.argv)
##    MainWindow = QtWidgets.QMainWindow()
##    ui = WindowStudentLogin()
##    ui.setupUi(MainWindow)
##    MainWindow.show()
##    sys.exit(app.exec_())
