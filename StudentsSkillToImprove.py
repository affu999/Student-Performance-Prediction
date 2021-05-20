from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import ReturnSkillsToImprove as rs
from PyQt5.QtWidgets import QMessageBox


class FrameStudentsSkillToImprove(object):

    def funDisplaySkills(self):
        try:
            self.textBrowser.clear()
            self.result = []
            self.rollNo = self.txtRollNo.text()
            if self.rollNo != "":
                con = sqlite3.connect("COLLEGE.db")
                cur = con.cursor()
                # print("Connected!!!")
                query = "SELECT * FROM STUDENT WHERE ROLLNO=?"
                # print(self.rollNo)
                data = cur.execute(query, (self.rollNo)).fetchall()
                # print("Extracted!!!")
                # print(len(data))
                if len(data) > 0:
                    for row in data:
                        # print(list(row))
                        self.result = rs.returnSkills(list(row))
                        # send(list(row))
                    for i in self.result:
                        self.textBrowser.append(i + "\n")
                else:
                    QMessageBox.warning(self.Frame, "Warning", "Student Does Not Exist!!!")
                cur.close()
                con.close()
            else:
                QMessageBox.warning(self.Frame, "Warning", "Enter Roll Number!!!")
                # print("RollNo is Empty!!!")
            
        except:
            QMessageBox.warning(self.Frame, "Warning", "Student Details Not Updated!!!")

    def setupUi(self, Frame):
        self.Frame = Frame
        Frame.setObjectName("Frame")
        Frame.resize(511, 421)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(150, 30, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtRollNo = QtWidgets.QLineEdit(Frame)
        self.txtRollNo.setGeometry(QtCore.QRect(190, 80, 281, 31))
        self.txtRollNo.setObjectName("lineEdit")
        self.btnDisplaySkills = QtWidgets.QPushButton(Frame)
        self.btnDisplaySkills.setGeometry(QtCore.QRect(190, 140, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDisplaySkills.setFont(font)
        self.btnDisplaySkills.setObjectName("pushButton")

        #------------------Adding Event to btnDisplaySkills---------------------------
        self.btnDisplaySkills.clicked.connect(self.funDisplaySkills)
        #--------------------------------------------------------------------------

        self.textBrowser = QtWidgets.QTextBrowser(Frame)
        self.textBrowser.setGeometry(QtCore.QRect(60, 210, 411, 171))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Students Skill To Improve"))
        self.label_2.setText(_translate("Frame", "Enter Roll No"))
        self.btnDisplaySkills.setText(_translate("Frame", "Display Skills"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Frame = QtWidgets.QFrame()
#     ui = FrameStudentsSkillToImprove()
#     ui.setupUi(Frame)
#     Frame.show()
#     sys.exit(app.exec_())
