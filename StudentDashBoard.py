from PyQt5 import QtCore, QtGui, QtWidgets
##from UpdateSkills import FrameUpdateSkills
from studentUI.UpdateSkills import FrameUpdateSkills

class WindowStudentDashBoard(object):
    
    def funUpdateSkills(self):
        self.frmUpdateSkills = QtWidgets.QFrame(self.centralwidget)
        self.frmUpdateSkills.setGeometry(QtCore.QRect(120, 70, 491, 351))
        self.frmUpdateSkillsUi = FrameUpdateSkills()
        self.frmUpdateSkillsUi.setupUi(self.frmUpdateSkills, self.rollNo)
        self.frmUpdateSkills.setVisible(True)
        self.frame.setVisible(False)

    def setupUi(self, MainWindow, rollNo):
        self.rollNo = rollNo
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 102, 254))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.btnUpdateSkills = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnUpdateSkills.setMinimumSize(QtCore.QSize(80, 80))
        self.btnUpdateSkills.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.btnUpdateSkills)

        #=============================Adding Event to btnUpdateSkills========================

        self.btnUpdateSkills.clicked.connect(self.funUpdateSkills)

        #====================================================================================

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(120, 70, 491, 351))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(110, 110, 301, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(200, 50, 151, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Student DashBoard"))
        self.pushButton_5.setText(_translate("MainWindow", "Check\n"
        "Student\n"
        "Performance"))
        self.pushButton_3.setText(_translate("MainWindow", "Students\n"
        "Skill to\n"
        "Improve"))
        self.btnUpdateSkills.setText(_translate("MainWindow", "Update\n"
        "Skills"))
        self.label_2.setText(_translate("MainWindow", "Upcoming Result"))
        self.pushButton_2.setText(_translate("MainWindow", "View Performance"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = WindowStudentDashBoard()
    ui.setupUi(MainWindow, 3)
    MainWindow.show()
    sys.exit(app.exec_())
