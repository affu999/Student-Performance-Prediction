from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox


class FrameUpdateViewStudentData(object):

    def funUpdateDetails(self):
        self.rollNo = str(self.txtRollNo.text())
        self.name = str(self.txtName.text())
        self.gender = str(self.cmbBoxGender.currentText())
        self.age = str(self.cmbBoxAge.currentText())

        if self.rollNo == "" or self.name == "" or self.gender == "" or self.age == "":
            QMessageBox.warning(self.Frame, "Warning", "Enter Complete Details!!!")
        else:
            try:
                con = sqlite3.connect("COLLEGE.db")
                cur = con.cursor()
                query = "UPDATE STUDENT SET NAME=?, sex=?, age=? WHERE ROLLNO=?"
                cur.execute(query, (self.name, self.gender, self.age, self.rollNo))
                con.commit()
                cur.close()
                con.close()
            except:
                QMessageBox.warning(self.Frame, "Warning", "Student Does not Exist!!!")
                # print("Student Does not exist!!!")
                

    def funViewDetails(self):
        self.rollNo = str(self.txtRollNo.text())
        if self.rollNo != "":
            try:
                con = sqlite3.connect("COLLEGE.db")
                cur = con.cursor()
                query = "SELECT * FROM STUDENT WHERE ROLLNO={}".format(self.rollNo)
                data = cur.execute(query).fetchall()
                if len(data) > 0:
                    self.textBrowser.setText("")
                    for row in data:
                        for i in row:
                            self.textBrowser.append(str(i))

                else:
                    QMessageBox.warning(self.Frame, "Warning", "Student Does not Exist!!!")
                    # print("Student does not Exist!!!")
                cur.close()
                con.close()
            except:
                QMessageBox.warning(self.Frame, "Warning", "Student Does not Exist!!!")
                # print("Student Does not exist!!!")
                
        else:
            QMessageBox.warning(self.Frame, "Warning", "Enter Roll Number!!!")
            # print("Enter Roll Number!!!")
            


    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setEnabled(True)
        Frame.resize(511, 421)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(150, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(40, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(40, 150, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(30, 240, 451, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textBrowser.setFont(font)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser.setObjectName("textBrowser")
        self.btnViewDetails = QtWidgets.QPushButton(Frame)
        self.btnViewDetails.setGeometry(QtCore.QRect(70, 350, 171, 31))
        self.btnViewDetails.setObjectName("pushButton")

        #------------------Adding Event to btnViewDetails---------------------------
        self.btnViewDetails.clicked.connect(self.funViewDetails)
        #--------------------------------------------------------------------------

        self.btnUpdateDetails = QtWidgets.QPushButton(Frame)
        self.btnUpdateDetails.setGeometry(QtCore.QRect(280, 350, 171, 31))
        self.btnUpdateDetails.setObjectName("pushButton_2")

        #------------------Adding Event to btnUpdateDetails---------------------------
        self.btnUpdateDetails.clicked.connect(self.funUpdateDetails)
        #--------------------------------------------------------------------------

        self.txtRollNo = QtWidgets.QLineEdit(Frame)
        self.txtRollNo.setGeometry(QtCore.QRect(180, 59, 261, 31))
        self.txtRollNo.setObjectName("lineEdit")
        self.txtName = QtWidgets.QLineEdit(Frame)
        self.txtName.setGeometry(QtCore.QRect(180, 100, 261, 31))
        self.txtName.setObjectName("lineEdit_2")

        #======================Gender==========================
        self.cmbBoxGender = QtWidgets.QComboBox(Frame)
        self.cmbBoxGender.setGeometry(QtCore.QRect(180, 150, 261, 31))
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
        #======================================================

        # self.txtGender = QtWidgets.QLineEdit(Frame)
        # self.txtGender.setGeometry(QtCore.QRect(180, 150, 261, 31))
        # self.txtGender.setObjectName("lineEdit_3")

        #=============================Age=======================
        self.cmbBoxAge = QtWidgets.QComboBox(Frame)
        self.cmbBoxAge.setGeometry(QtCore.QRect(180, 190, 261, 31))
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
        #=======================================================

        # self.txtAge = QtWidgets.QLineEdit(Frame)
        # self.txtAge.setGeometry(QtCore.QRect(180, 190, 261, 31))
        # self.txtAge.setObjectName("lineEdit_4")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        self.Frame = Frame

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Update/View Student Data"))
        self.label_2.setText(_translate("Frame", "Enter Roll No"))
        self.label_3.setText(_translate("Frame", "Name"))
        self.label_4.setText(_translate("Frame", "Gender"))
        self.label_5.setText(_translate("Frame", "Age"))
        self.btnViewDetails.setText(_translate("Frame", "View Details"))
        self.btnUpdateDetails.setText(_translate("Frame", "Update Details"))
        self.cmbBoxGender.setItemText(0, _translate("Frame", "Male"))
        self.cmbBoxGender.setItemText(1, _translate("Frame", "Female"))
        self.cmbBoxAge.setItemText(0, _translate("Frame", "15"))
        self.cmbBoxAge.setItemText(1, _translate("Frame", "16"))
        self.cmbBoxAge.setItemText(2, _translate("Frame", "17"))
        self.cmbBoxAge.setItemText(3, _translate("Frame", "18"))
        self.cmbBoxAge.setItemText(4, _translate("Frame", "19"))
        self.cmbBoxAge.setItemText(5, _translate("Frame", "20"))
        self.cmbBoxAge.setItemText(6, _translate("Frame", "21"))
        self.cmbBoxAge.setItemText(7, _translate("Frame", "22"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Frame = QtWidgets.QFrame()
#     ui = FrameUpdateViewStudentData()
#     ui.setupUi(Frame)
#     Frame.show()
#     sys.exit(app.exec_())
