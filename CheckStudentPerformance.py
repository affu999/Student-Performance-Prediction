from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from DataMining import DataMining
from PyQt5.QtWidgets import QMessageBox


class FrameCheckStudentPerformance(object):

    def funCheckPerformance(self):
        self.btnCheckPerformance.setEnabled(False)
        self.rollNo = str(self.txtRollNo.text())
        if self.rollNo != "":
            try:
                con = sqlite3.connect("COLLEGE.db")
                cur = con.cursor()
                query = "SELECT * FROM STUDENT WHERE ROLLNO=?"
                data = cur.execute(query,(self.rollNo)).fetchall()
                if len(data) > 0:
                    for row in data:
                        row = list(row)[2:-1]
                        if row[0] == "Male":
                            row[0] = "M"
                        else:
                            row[0]= "F"
                        self.result = DataMining.result(row)
                        self.txtResult.setText(self.result)
                else:
                    QMessageBox.warning(self.Frame, "Warning", "Student Does not Exist!!!")
                    # print("Student Does not Exist!!!")
                cur.close()
                con.close()

            except:
                QMessageBox.warning(self.Frame, "Warning", "Student Details not Updated!!!")
                # print("Could not Connect!!!")
        else:
            QMessageBox.warning(self.Frame, "Warning", "Enter Roll Number!!!")
            # print("RollNo is Empty!!!")
        self.btnCheckPerformance.setEnabled(True)


    def setupUi(self, Frame):
        self.Frame = Frame
        Frame.setObjectName("Frame")
        Frame.resize(511, 421)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(130, 20, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.txtRollNo = QtWidgets.QLineEdit(Frame)
        self.txtRollNo.setGeometry(QtCore.QRect(180, 70, 281, 31))
        self.txtRollNo.setObjectName("lineEdit")
        self.btnCheckPerformance = QtWidgets.QPushButton(Frame)
        self.btnCheckPerformance.setGeometry(QtCore.QRect(180, 120, 141, 41))
        self.btnCheckPerformance.setObjectName("pushButton")

        #------------------Adding Event to btnCheckPerformance---------------------------
        self.btnCheckPerformance.clicked.connect(self.funCheckPerformance)
        #--------------------------------------------------------------------------

        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtResult = QtWidgets.QLineEdit(Frame)
        self.txtResult.setEnabled(False)
        self.txtResult.setGeometry(QtCore.QRect(180, 180, 281, 31))
        self.txtResult.setObjectName("lineEdit_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Check Student Performance"))
        self.label_2.setText(_translate("Frame", "Enter Roll No"))
        self.btnCheckPerformance.setText(_translate("Frame", "Check Performance"))
        self.label_3.setText(_translate("Frame", "Result:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = FrameCheckStudentPerformance()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
