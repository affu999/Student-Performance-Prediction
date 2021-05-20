from PyQt5 import QtCore, QtGui, QtWidgets
from UpdateViewStudentData import FrameUpdateViewStudentData
from CheckStudentPerformance import FrameCheckStudentPerformance
from CollegeAcademicStatus import FrameCollegeAcademicStatus
from StudentsSkillToImprove import FrameStudentsSkillToImprove
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class WindowAdminDashBoard(object):

    def funEnterStudentDetails(self):
        self.rollNo = str(self.txtRollNo.text())
        self.name = str(self.txtName.text())
        self.gender = str(self.cmbBoxGender.currentText())
        self.age = str(self.cmbBoxAge.currentText())
        if self.rollNo != "" and self.name != "":
            try:
                con = sqlite3.connect("COLLEGE.db")
                cur = con.cursor()
                query = "INSERT INTO STUDENT('ROLLNO', 'NAME', 'sex', 'age') VALUES(?, ?, ?, ?)"
                cur.execute(query, (self.rollNo, self.name, self.gender, self.age))
                con.commit()
                # print("Insert Success!!!")
                cur.close()
                con.close()
            except:
                QMessageBox.information(self.centralwidget, "Info", "Student Already Exist!!!")
                # print("Student already Exist!!!")
                
        else:
            QMessageBox.warning(self.centralwidget, "Warning", "Name/RollNo field is empty!!!")
            # print("Could not Insert!!!")
            

    def createFrames(self):
        self.frmUpdateViewStudentData = QtWidgets.QFrame(self.centralwidget)
        self.frmCheckStudentPerformance = QtWidgets.QFrame(self.centralwidget)
        self.frmCollegeAcademicStatus = QtWidgets.QFrame(self.centralwidget)
        self.frmStudentsSkillToImprove = QtWidgets.QFrame(self.centralwidget)


    def funUpdateViewStudentData(self):
        self.btnUpdateViewStudentData.setEnabled(False)
        self.frmUpdateViewStudentData = QtWidgets.QFrame(self.centralwidget)
        # self.frmCheckStudentPerformance = QtWidgets.QFrame(self.centralwidget)
        self.frmUpdateViewStudentData.setGeometry(QtCore.QRect(110, 70, 511, 421))
        self.frmUpdateViewStudentDataUi = FrameUpdateViewStudentData()
        self.frmUpdateViewStudentDataUi.setupUi(self.frmUpdateViewStudentData)
        self.frmUpdateViewStudentData.setVisible(True)
        self.frmStudentsSkillToImprove.setVisible(False)
        self.frmCollegeAcademicStatus.setVisible(False)
        self.frmCheckStudentPerformance.setVisible(False)
        self.frameStudentRegistration.setVisible(False)
        self.btnStudentRegistration.setEnabled(True)
        self.btnCheckStudentPerformance.setEnabled(True)
        self.btnCollegeAcademicStatus.setEnabled(True)
        self.btnStudentsSkillToImprove.setEnabled(True)


    def funStudentRegistration(self):
        self.btnStudentRegistration.setEnabled(False)
        # self.frmUpdateViewStudentData = QtWidgets.QFrame(self.centralwidget)
        # self.frmCheckStudentPerformance = QtWidgets.QFrame(self.centralwidget)
        self.frmCheckStudentPerformance.setVisible(False)
        self.frmStudentsSkillToImprove.setVisible(False)
        self.frmUpdateViewStudentData.setVisible(False)
        self.frmCollegeAcademicStatus.setVisible(False)
        self.frameStudentRegistration.setVisible(True)
        self.btnUpdateViewStudentData.setEnabled(True)
        self.btnCheckStudentPerformance.setEnabled(True)
        self.btnCollegeAcademicStatus.setEnabled(True)
        self.btnStudentsSkillToImprove.setEnabled(True)


    def funCheckStudentPerformance(self):
        self.btnCheckStudentPerformance.setEnabled(False)
        self.frmCheckStudentPerformance = QtWidgets.QFrame(self.centralwidget)
        # self.frmUpdateViewStudentData = QtWidgets.QFrame(self.centralwidget)
        self.frmCheckStudentPerformance.setGeometry(QtCore.QRect(110, 70, 511, 421))
        self.frmCheckStudentPerformanceUi = FrameCheckStudentPerformance()
        self.frmCheckStudentPerformanceUi.setupUi(self.frmCheckStudentPerformance)
        self.frmCheckStudentPerformance.setVisible(True)
        self.frmStudentsSkillToImprove.setVisible(False)
        self.frmCollegeAcademicStatus.setVisible(False)
        self.frameStudentRegistration.setVisible(False)
        self.frmUpdateViewStudentData.setVisible(False)
        self.btnUpdateViewStudentData.setEnabled(True)
        self.btnStudentRegistration.setEnabled(True)
        self.btnCollegeAcademicStatus.setEnabled(True)
        self.btnStudentsSkillToImprove.setEnabled(True)


    def funCollegeAcademicStatus(self):
        self.btnCollegeAcademicStatus.setEnabled(False)
        self.frmCollegeAcademicStatus = QtWidgets.QFrame(self.centralwidget)
        # self.frmUpdateViewStudentData = QtWidgets.QFrame(self.centralwidget)
        self.frmCollegeAcademicStatus.setGeometry(QtCore.QRect(110, 70, 511, 421))
        self.frmCollegeAcademicStatusUi = FrameCollegeAcademicStatus()
        self.frmCollegeAcademicStatusUi.setupUi(self.frmCollegeAcademicStatus)
        self.frmCollegeAcademicStatus.setVisible(True)
        self.frmStudentsSkillToImprove.setVisible(False)
        self.frameStudentRegistration.setVisible(False)
        self.frmUpdateViewStudentData.setVisible(False)
        self.frmCheckStudentPerformance.setVisible(False)
        self.btnUpdateViewStudentData.setEnabled(True)
        self.btnStudentRegistration.setEnabled(True)
        self.btnCheckStudentPerformance.setEnabled(True)
        self.btnStudentsSkillToImprove.setEnabled(True)


    def funStudentsSkillToImprove(self):
        self.btnStudentsSkillToImprove.setEnabled(False)
        self.frmStudentsSkillToImprove = QtWidgets.QFrame(self.centralwidget)
        # self.frmUpdateViewStudentData = QtWidgets.QFrame(self.centralwidget)
        self.frmStudentsSkillToImprove.setGeometry(QtCore.QRect(110, 70, 511, 421))
        self.frmStudentsSkillToImproveUi = FrameStudentsSkillToImprove()
        self.frmStudentsSkillToImproveUi.setupUi(self.frmStudentsSkillToImprove)
        self.frmStudentsSkillToImprove.setVisible(True)
        self.frameStudentRegistration.setVisible(False)
        self.frmCheckStudentPerformance.setVisible(False)
        self.frmUpdateViewStudentData.setVisible(False)
        self.frmCollegeAcademicStatus.setVisible(False)
        self.btnUpdateViewStudentData.setEnabled(True)
        self.btnStudentRegistration.setEnabled(True)
        self.btnCheckStudentPerformance.setEnabled(True)
        self.btnCollegeAcademicStatus.setEnabled(True)


    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 533)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.createFrames()
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 70, 91, 426))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnStudentRegistration = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnStudentRegistration.setEnabled(False)
        self.btnStudentRegistration.setMinimumSize(QtCore.QSize(80, 80))
        self.btnStudentRegistration.setObjectName("pushButton_2")

        #================Adding Event to btnStudentRegistration==================
        self.btnStudentRegistration.clicked.connect(self.funStudentRegistration)
        #==========================================================================

        self.verticalLayout_2.addWidget(self.btnStudentRegistration)
        self.btnUpdateViewStudentData = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnUpdateViewStudentData.setMinimumSize(QtCore.QSize(80, 80))
        self.btnUpdateViewStudentData.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.btnUpdateViewStudentData)

        #================Adding Event to btnUpdateViewStudentData==================
        self.btnUpdateViewStudentData.clicked.connect(self.funUpdateViewStudentData)
        #==========================================================================

        self.btnCheckStudentPerformance = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnCheckStudentPerformance.setMinimumSize(QtCore.QSize(80, 80))
        self.btnCheckStudentPerformance.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.btnCheckStudentPerformance)

        #================Adding Event to btnCheckStudentPerformance==================
        self.btnCheckStudentPerformance.clicked.connect(self.funCheckStudentPerformance)
        #==========================================================================

        self.btnCollegeAcademicStatus = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnCollegeAcademicStatus.setMinimumSize(QtCore.QSize(80, 80))
        self.btnCollegeAcademicStatus.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.btnCollegeAcademicStatus)

        #================Adding Event to btnCollegeAcademicStatus==================
        self.btnCollegeAcademicStatus.clicked.connect(self.funCollegeAcademicStatus)
        #==========================================================================

        self.btnStudentsSkillToImprove = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnStudentsSkillToImprove.setMinimumSize(QtCore.QSize(80, 80))
        self.btnStudentsSkillToImprove.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.btnStudentsSkillToImprove)

        #================Adding Event to btnStudentsSkillToImprove==================
        self.btnStudentsSkillToImprove.clicked.connect(self.funStudentsSkillToImprove)
        #==========================================================================

        self.frameStudentRegistration = QtWidgets.QFrame(self.centralwidget)
        self.frameStudentRegistration.setGeometry(QtCore.QRect(110, 70, 511, 421))
        self.frameStudentRegistration.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameStudentRegistration.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameStudentRegistration.setObjectName("frameStudentRegistration")
        self.label_2 = QtWidgets.QLabel(self.frameStudentRegistration)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frameStudentRegistration)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frameStudentRegistration)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frameStudentRegistration)
        self.label_5.setGeometry(QtCore.QRect(40, 210, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtRollNo = QtWidgets.QLineEdit(self.frameStudentRegistration)
        self.txtRollNo.setGeometry(QtCore.QRect(190, 40, 251, 31))
        self.txtRollNo.setObjectName("lineEdit")
        self.txtName = QtWidgets.QLineEdit(self.frameStudentRegistration)
        self.txtName.setGeometry(QtCore.QRect(190, 90, 251, 31))
        self.txtName.setObjectName("lineEdit_2")
        self.cmbBoxGender = QtWidgets.QComboBox(self.frameStudentRegistration)
        self.cmbBoxGender.setGeometry(QtCore.QRect(190, 150, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cmbBoxGender.setFont(font)
        self.cmbBoxGender.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.cmbBoxGender.setEditable(False)
        self.cmbBoxGender.setObjectName("comboBox")
        self.cmbBoxGender.addItem("")
        self.cmbBoxGender.addItem("")
        self.cmbBoxAge = QtWidgets.QComboBox(self.frameStudentRegistration)
        self.cmbBoxAge.setGeometry(QtCore.QRect(190, 210, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cmbBoxAge.setFont(font)
        self.cmbBoxAge.setObjectName("comboBox_2")
        self.cmbBoxAge.addItem("")
        self.cmbBoxAge.addItem("")
        self.cmbBoxAge.addItem("")
        self.cmbBoxAge.addItem("")
        self.cmbBoxAge.addItem("")
        self.cmbBoxAge.addItem("")
        self.cmbBoxAge.addItem("")
        self.cmbBoxAge.addItem("")
        self.btnRegisterStudent = QtWidgets.QPushButton(self.frameStudentRegistration)
        self.btnRegisterStudent.setGeometry(QtCore.QRect(130, 300, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegisterStudent.setFont(font)
        self.btnRegisterStudent.setObjectName("pushButton_6")

        #================Adding Event to btnRegisterStudent==================
        self.btnRegisterStudent.clicked.connect(self.funEnterStudentDetails)
        #==========================================================================

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Admin DashBoard"))
        self.label.setText(_translate("MainWindow", "Admin DashBoard"))
        self.btnStudentRegistration.setText(_translate("MainWindow", "Student\n"
        "Registration\n"
        ""))
        self.btnUpdateViewStudentData.setText(_translate("MainWindow", "Update/View\n"
        "Student Data"))
        self.btnCheckStudentPerformance.setText(_translate("MainWindow", "Check\n"
        "Student\n"
        "Performance"))
        self.btnCollegeAcademicStatus.setText(_translate("MainWindow", "College\n"
        "Academic\n"
        "Status"))
        self.btnStudentsSkillToImprove.setText(_translate("MainWindow", "Students\n"
        "Skill to\n"
        "Improve"))
        self.label_2.setText(_translate("MainWindow", "Enter Roll No"))
        self.label_3.setText(_translate("MainWindow", "Enter Name"))
        self.label_4.setText(_translate("MainWindow", "Select Gender"))
        self.label_5.setText(_translate("MainWindow", "Select Age"))
        self.cmbBoxGender.setItemText(0, _translate("MainWindow", "Male"))
        self.cmbBoxGender.setItemText(1, _translate("MainWindow", "Female"))
        self.cmbBoxAge.setItemText(0, _translate("MainWindow", "15"))
        self.cmbBoxAge.setItemText(1, _translate("MainWindow", "16"))
        self.cmbBoxAge.setItemText(2, _translate("MainWindow", "17"))
        self.cmbBoxAge.setItemText(3, _translate("MainWindow", "18"))
        self.cmbBoxAge.setItemText(4, _translate("MainWindow", "19"))
        self.cmbBoxAge.setItemText(5, _translate("MainWindow", "20"))
        self.cmbBoxAge.setItemText(6, _translate("MainWindow", "21"))
        self.cmbBoxAge.setItemText(7, _translate("MainWindow", "22"))
        self.btnRegisterStudent.setText(_translate("MainWindow", "Register Student"))


# if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = WindowAdminDashBoard()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())
