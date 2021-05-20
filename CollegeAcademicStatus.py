from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox


class FrameCollegeAcademicStatus(object):

    def setPassFail(self):
        try:
            con = sqlite3.connect("COLLEGE.db")
            cur = con.cursor()
            data = cur.execute("SELECT G3 FROM STUDENT").fetchall()
            self.results = [list(row)[0] for row in list(data) if list(row)[0] != None]
            self.failed = [i for i in self.results if i < 8]
            self.passed = [i for i in self.results if i >= 8]
            self.passed = len(self.passed) / len(self.results) * 100
            self.failed = len(self.failed) / len(self.results) * 100
            cur.close()
            con.close()

        except:
            QMessageBox.warning(self.Frame, "Warning", "Could Not Connect!!!")
            

    def setupUi(self, Frame):
        self.setPassFail()
        Frame.setObjectName("Frame")
        Frame.resize(511, 421)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(150, 20, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txtPassed = QtWidgets.QLineEdit(Frame)
        self.txtPassed.setEnabled(False)
        self.txtPassed.setGeometry(QtCore.QRect(220, 60, 251, 31))
        self.txtPassed.setObjectName("lineEdit")
        self.txtFailed = QtWidgets.QLineEdit(Frame)
        self.txtFailed.setEnabled(False)
        self.txtFailed.setGeometry(QtCore.QRect(220, 110, 251, 31))
        self.txtFailed.setObjectName("lineEdit_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

        self.txtPassed.setText(str(self.passed))
        self.txtFailed.setText(str(self.failed))

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "College Academic Status"))
        self.label_2.setText(_translate("Frame", "Passing Student(%)"))
        self.label_3.setText(_translate("Frame", "Failing Student(%)"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Frame = QtWidgets.QFrame()
#     ui = FrameCollegeAcademicStatus()
#     ui.setupUi(Frame)
#     Frame.show()
#     sys.exit(app.exec_())
