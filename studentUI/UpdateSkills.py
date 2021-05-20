from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox


class FrameUpdateSkills(object):

    #================================Functions to clean Attribute Values=======================

    def cleanAddress(self, address):
        if address == "Address":
            return ""
        else:
            return address

    def cleanFamilySize(self, familySize):
        if familySize == "Family Size":
            return ""
        else:
            return familySize

    def cleanMothersEducation(self, mothersEducation):
        if mothersEducation == "MothersEducation":
            return ""
        else:
            if mothersEducation == "Primary":
                return 1
            if mothersEducation == "HighSchool":
                return 2
            if mothersEducation == "PUC":
                return 3
            if mothersEducation == "Degree":
                return 4
            if mothersEducation == "None":
                return 0

    def cleanFathersEducation(self, fathersEducation):
        if fathersEducation == "FathersEducation":
            return ""
        else:
            if fathersEducation == "Primary":
                return 1
            if fathersEducation == "HighSchool":
                return 2
            if fathersEducation == "PUC":
                return 3
            if fathersEducation == "Degree":
                return 4
            if fathersEducation == "None":
                return 0

    def cleanMothersJob(self, mothersJob):
        if mothersJob == "Mothers Job":
            return ""
        else:
            if mothersJob == "Teacher":
                return "teacher"
            if mothersJob == "Healthcare":
                return "health"
            if mothersJob == "CivilServices":
                return "services"
            if mothersJob == "AtHome":
                return "at_home"
            if mothersJob == "Other":
                return "other"

    def cleanFathersJob(self, fathersJob):
        if fathersJob == "Fathers Job":
            return ""
        else:
            if fathersJob == "Teacher":
                return "teacher"
            if fathersJob == "Healthcare":
                return "health"
            if fathersJob == "CivilServices":
                return "services"
            if fathersJob == "AtHome":
                return "at_home"
            if fathersJob == "Other":
                return "other"

    def cleanGuardian(self, guardian):
        if guardian == "Guardian":
            return ""
        else:
            if guardian == "Mother":
                return "mother"
            if guardian == "Father":
                return "father"
            if guardian == "Other":
                return "other"

    def cleanTravelTime(self, travelTime):
        if travelTime == "TravelTime":
            return ""
        else:
            if travelTime == "15min":
                return 1
            if travelTime == "30min":
                return 2
            if travelTime == "1hr":
                return 3
            if travelTime == ">1hr":
                return 4

    def cleanStudyTime(self, studyTime):
        if studyTime == "TravelTime":
            return ""
        else:
            if studyTime == "<2hr":
                return 1
            if studyTime == "2 to 5hr":
                return 2
            if studyTime == "5 to 10hr":
                return 3
            if studyTime == ">10hr":
                return 4

    def cleanPastFails(self, pastFails):
        if pastFails == "Past Fails":
            return ""
        else:
            return int(pastFails)

    def cleanExtraEducationSupport(self, extraEducationSupport):
        if extraEducationSupport == "ExtraEduSupport":
            return ""
        else:
            return extraEducationSupport

    def cleanFamilySupport(self, familySupport):
        if familySupport == "FamilySupport":
            return ""
        else:
            return familySupport

    def cleanTuitions(self, tuitions):
        if tuitions == "Tuitions":
            return ""
        else:
            return tuitions

    def cleanExtraActivities(self, extraActivities):
        if extraActivities == "ExtraActivities":
            return ""
        else:
            return extraActivities

    def cleanHigherEducation(self, higherEducation):
        if higherEducation == "HigherEducation":
            return ""
        else:
            return higherEducation

    def cleanNetAccess(self, netAccess):
        if netAccess == "NetAccess":
            return ""
        else:
            return netAccess

    def cleanRomantic(self, romantic):
        if romantic == "Romantic":
            return ""
        else:
            return romantic

    def cleanFreeTime(self, freeTime):
        if freeTime == "FreeTime":
            return ""
        else:
            return int(freeTime)

    def cleanGoingOut(self, goingOut):
        if goingOut == "GoingOut":
            return ""
        else:
            return int(goingOut)

    def cleanAlcoholConsumption(self, alcoholConsumption):
        if alcoholConsumption == "AlcoholConsumption":
            return ""
        else:
            return int(alcoholConsumption)

    def cleanHealth(self, health):
        if health == "Health":
            return ""
        else:
            return int(health)

    #==========================================================================================

    #================================btnUpdateSkills Function to get Attribute Values==========

    def funUpdateSkills(self):
        try:
            self.address = str(self.cmbAddress.currentText())
            self.address = str(self.cleanAddress(self.address))

            self.familySize = str(self.cmbFamilySize.currentText())
            self.familySize = str(self.cleanFamilySize(self.familySize))

            self.mothersEducation = str(self.cmbMothersEducation.currentText())
            self.mothersEducation = int(self.cleanMothersEducation(self.mothersEducation))

            self.fathersEducation = str(self.cmbFathersEducation.currentText())
            self.fathersEducation = int(self.cleanFathersEducation(self.fathersEducation))

            self.mothersJob = str(self.cmbMothersJob.currentText())
            self.mothersJob = str(self.cleanMothersJob(self.mothersJob))

            self.fathersJob = str(self.cmbFathersJob.currentText())
            self.fathersJob = str(self.cleanFathersJob(self.fathersJob))

            self.gaurdian = str(self.cmbGuardian.currentText())
            self.gaurdian = str(self.cleanGuardian(self.gaurdian))

            self.travelTime = str(self.cmbTravelTime.currentText())
            self.travelTime = int(self.cleanTravelTime(self.travelTime))

            self.studyTime = str(self.cmbStudyTime.currentText())
            self.studyTime = int(self.cleanStudyTime(self.studyTime))

            self.pastFails = str(self.cmbPastFails.currentText())
            self.pastFails = int(self.cleanPastFails(self.pastFails))

            self.extraEducationSupport = str(self.cmbExtraEducationSupport.currentText())
            self.extraEducationSupport = str(self.cleanExtraEducationSupport(self.extraEducationSupport))

            self.familySupport = str(self.cmbFamilySupport.currentText())
            self.familySupport = str(self.cleanFamilySupport(self.familySupport))

            self.tuitions = str(self.cmbTuitions.currentText())
            self.tuitions = str(self.cleanTuitions(self.tuitions))

            self.extraActivities = str(self.cmbExtraActivities.currentText())
            self.extraActivities = str(self.cleanExtraActivities(self.extraActivities))

            self.higherEducation = str(self.cmbHigherEducation.currentText())
            self.higherEducation = str(self.cleanHigherEducation(self.higherEducation))

            self.netAccess = str(self.cmbNetAccess.currentText())
            self.netAccess = str(self.cleanNetAccess(self.netAccess))

            self.romantic = str(self.cmbRomantic.currentText())
            self.romantic = str(self.cleanRomantic(self.romantic))

            self.freeTime = str(self.cmbFreeTime.currentText())
            self.freeTime = int(self.cleanFreeTime(self.freeTime))

            self.goingOut = str(self.cmbGoingOut.currentText())
            self.goingOut = int(self.cleanGoingOut(self.goingOut))

            self.alcoholConsumption = str(self.cmbAlcoholConsumption.currentText())
            self.alcoholConsumption = int(self.cleanAlcoholConsumption(self.alcoholConsumption))

            self.health = str(self.cmbHealth.currentText())
            self.health = int(self.cleanHealth(self.health))

            self.absences = int(self.spnAbsences.value())

            self.G1 = int(self.spnG1.value())

            self.G2 = int(self.spnG2.value())


            # print("Success!!!")
            # print(self.address, self.familySize, self.mothersEducation,
            #     self.fathersEducation, self.mothersJob, self.fathersJob, self.gaurdian, 
            #     self.travelTime, self.studyTime, self.pastFails, self.extraEducationSupport, 
            #     self.familySupport, self.tuitions, self.extraActivities, self.higherEducation, 
            #     self.netAccess, self.romantic, self.freeTime, self.goingOut, 
            #     self.alcoholConsumption, self.health, self.absences, self.G1, self.G2, self.rollNo)
            # print("Done!!!")


            
            con = sqlite3.connect("COLLEGE.db")
            cur = con.cursor()
            query = "UPDATE STUDENT SET address=?, famsize=?, Medu=?, Fedu=?, Mjob=?, Fjob=?, \
            guardian=?, traveltime=?, studytime=?, failures=?, schoolsup=?, famsup=?, paid=?, \
            activities=?, higher=?, internet=?, romantic=?, freetime=?, goout=?, Walc=?, \
            health=?, absences=?, G1=?, G2=? WHERE ROLLNO=?"

            cur.execute(query, (self.address, self.familySize, self.mothersEducation,
            self.fathersEducation, self.mothersJob, self.fathersJob, self.gaurdian, 
            self.travelTime, self.studyTime, self.pastFails, self.extraEducationSupport, 
            self.familySupport, self.tuitions, self.extraActivities, self.higherEducation, 
            self.netAccess, self.romantic, self.freeTime, self.goingOut, 
            self.alcoholConsumption, self.health, self.absences, self.G1, self.G2, self.rollNo))

            con.commit()
            cur.close()
            con.close()

            QMessageBox.information(self.Frame, "Info", "Successfully Updated!!!")

        except:
            QMessageBox.warning(self.Frame, "Warning", "Field Value Missing")


    #=========================================================================================


    def setupUi(self, Frame, rollNo):
        self.Frame = Frame
        self.rollNo = rollNo
        Frame.setObjectName("Frame")
        Frame.resize(492, 351)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(190, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cmbAddress = QtWidgets.QComboBox(Frame)
        self.cmbAddress.setGeometry(QtCore.QRect(20, 50, 111, 22))
        self.cmbAddress.setObjectName("cmbAddress")
        self.cmbAddress.addItem("")
        self.cmbAddress.addItem("")
        self.cmbAddress.addItem("")
        self.cmbFamilySize = QtWidgets.QComboBox(Frame)
        self.cmbFamilySize.setGeometry(QtCore.QRect(140, 50, 111, 22))
        self.cmbFamilySize.setObjectName("cmbFamilySize")
        self.cmbFamilySize.addItem("")
        self.cmbFamilySize.addItem("")
        self.cmbFamilySize.addItem("")
        self.cmbMothersEducation = QtWidgets.QComboBox(Frame)
        self.cmbMothersEducation.setGeometry(QtCore.QRect(260, 50, 111, 22))
        self.cmbMothersEducation.setObjectName("cmbMothersEducation")
        self.cmbMothersEducation.addItem("")
        self.cmbMothersEducation.addItem("")
        self.cmbMothersEducation.addItem("")
        self.cmbMothersEducation.addItem("")
        self.cmbMothersEducation.addItem("")
        self.cmbMothersEducation.addItem("")
        self.cmbMothersJob = QtWidgets.QComboBox(Frame)
        self.cmbMothersJob.setGeometry(QtCore.QRect(20, 90, 111, 22))
        self.cmbMothersJob.setObjectName("cmbMothersJob")
        self.cmbMothersJob.addItem("")
        self.cmbMothersJob.addItem("")
        self.cmbMothersJob.addItem("")
        self.cmbMothersJob.addItem("")
        self.cmbMothersJob.addItem("")
        self.cmbMothersJob.addItem("")
        self.cmbGuardian = QtWidgets.QComboBox(Frame)
        self.cmbGuardian.setGeometry(QtCore.QRect(260, 90, 111, 22))
        self.cmbGuardian.setObjectName("cmbGuardian")
        self.cmbGuardian.addItem("")
        self.cmbGuardian.addItem("")
        self.cmbGuardian.addItem("")
        self.cmbGuardian.addItem("")
        self.cmbTravelTime = QtWidgets.QComboBox(Frame)
        self.cmbTravelTime.setGeometry(QtCore.QRect(380, 90, 101, 22))
        self.cmbTravelTime.setObjectName("cmbTravelTime")
        self.cmbTravelTime.addItem("")
        self.cmbTravelTime.addItem("")
        self.cmbTravelTime.addItem("")
        self.cmbTravelTime.addItem("")
        self.cmbTravelTime.addItem("")
        self.cmbStudyTime = QtWidgets.QComboBox(Frame)
        self.cmbStudyTime.setGeometry(QtCore.QRect(20, 130, 111, 22))
        self.cmbStudyTime.setObjectName("cmbStudyTime")
        self.cmbStudyTime.addItem("")
        self.cmbStudyTime.addItem("")
        self.cmbStudyTime.addItem("")
        self.cmbStudyTime.addItem("")
        self.cmbStudyTime.addItem("")
        self.cmbExtraEducationSupport = QtWidgets.QComboBox(Frame)
        self.cmbExtraEducationSupport.setGeometry(QtCore.QRect(260, 130, 111, 22))
        self.cmbExtraEducationSupport.setObjectName("cmbExtraEducationSupport")
        self.cmbExtraEducationSupport.addItem("")
        self.cmbExtraEducationSupport.addItem("")
        self.cmbExtraEducationSupport.addItem("")
        self.cmbPastFails = QtWidgets.QComboBox(Frame)
        self.cmbPastFails.setGeometry(QtCore.QRect(140, 130, 111, 22))
        self.cmbPastFails.setObjectName("cmbPastFails")
        self.cmbPastFails.addItem("")
        self.cmbPastFails.addItem("")
        self.cmbPastFails.addItem("")
        self.cmbPastFails.addItem("")
        self.cmbPastFails.addItem("")
        self.cmbFamilySupport = QtWidgets.QComboBox(Frame)
        self.cmbFamilySupport.setGeometry(QtCore.QRect(380, 130, 101, 22))
        self.cmbFamilySupport.setObjectName("cmbFamilySupport")
        self.cmbFamilySupport.addItem("")
        self.cmbFamilySupport.addItem("")
        self.cmbFamilySupport.addItem("")
        self.cmbTuitions = QtWidgets.QComboBox(Frame)
        self.cmbTuitions.setGeometry(QtCore.QRect(20, 170, 111, 22))
        self.cmbTuitions.setObjectName("cmbTuitions")
        self.cmbTuitions.addItem("")
        self.cmbTuitions.addItem("")
        self.cmbTuitions.addItem("")
        self.cmbHigherEducation = QtWidgets.QComboBox(Frame)
        self.cmbHigherEducation.setGeometry(QtCore.QRect(260, 170, 111, 22))
        self.cmbHigherEducation.setObjectName("cmbHigherEducation")
        self.cmbHigherEducation.addItem("")
        self.cmbHigherEducation.addItem("")
        self.cmbHigherEducation.addItem("")
        self.cmbExtraActivities = QtWidgets.QComboBox(Frame)
        self.cmbExtraActivities.setGeometry(QtCore.QRect(140, 170, 111, 22))
        self.cmbExtraActivities.setObjectName("cmbExtraActivities")
        self.cmbExtraActivities.addItem("")
        self.cmbExtraActivities.addItem("")
        self.cmbExtraActivities.addItem("")
        self.cmbNetAccess = QtWidgets.QComboBox(Frame)
        self.cmbNetAccess.setGeometry(QtCore.QRect(380, 170, 101, 22))
        self.cmbNetAccess.setObjectName("cmbNetAccess")
        self.cmbNetAccess.addItem("")
        self.cmbNetAccess.addItem("")
        self.cmbNetAccess.addItem("")
        self.cmbRomantic = QtWidgets.QComboBox(Frame)
        self.cmbRomantic.setGeometry(QtCore.QRect(20, 210, 111, 22))
        self.cmbRomantic.setObjectName("cmbRomantic")
        self.cmbRomantic.addItem("")
        self.cmbRomantic.addItem("")
        self.cmbRomantic.addItem("")
        self.cmbGoingOut = QtWidgets.QComboBox(Frame)
        self.cmbGoingOut.setGeometry(QtCore.QRect(260, 210, 111, 22))
        self.cmbGoingOut.setObjectName("cmbGoingOut")
        self.cmbGoingOut.addItem("")
        self.cmbGoingOut.addItem("")
        self.cmbGoingOut.addItem("")
        self.cmbGoingOut.addItem("")
        self.cmbGoingOut.addItem("")
        self.cmbGoingOut.addItem("")
        self.cmbFreeTime = QtWidgets.QComboBox(Frame)
        self.cmbFreeTime.setGeometry(QtCore.QRect(140, 210, 111, 22))
        self.cmbFreeTime.setObjectName("cmbFreeTime")
        self.cmbFreeTime.addItem("")
        self.cmbFreeTime.addItem("")
        self.cmbFreeTime.addItem("")
        self.cmbFreeTime.addItem("")
        self.cmbFreeTime.addItem("")
        self.cmbFreeTime.addItem("")
        self.cmbAlcoholConsumption = QtWidgets.QComboBox(Frame)
        self.cmbAlcoholConsumption.setGeometry(QtCore.QRect(380, 210, 101, 22))
        self.cmbAlcoholConsumption.setObjectName("cmbAlcoholConsumption")
        self.cmbAlcoholConsumption.addItem("")
        self.cmbAlcoholConsumption.addItem("")
        self.cmbAlcoholConsumption.addItem("")
        self.cmbAlcoholConsumption.addItem("")
        self.cmbAlcoholConsumption.addItem("")
        self.cmbAlcoholConsumption.addItem("")
        self.cmbHealth = QtWidgets.QComboBox(Frame)
        self.cmbHealth.setGeometry(QtCore.QRect(40, 250, 69, 22))
        self.cmbHealth.setObjectName("cmbHealth")
        self.cmbHealth.addItem("")
        self.cmbHealth.addItem("")
        self.cmbHealth.addItem("")
        self.cmbHealth.addItem("")
        self.cmbHealth.addItem("")
        self.cmbHealth.addItem("")
        self.cmbFathersEducation = QtWidgets.QComboBox(Frame)
        self.cmbFathersEducation.setGeometry(QtCore.QRect(380, 50, 101, 22))
        self.cmbFathersEducation.setObjectName("cmbFathersEducation")
        self.cmbFathersEducation.addItem("")
        self.cmbFathersEducation.addItem("")
        self.cmbFathersEducation.addItem("")
        self.cmbFathersEducation.addItem("")
        self.cmbFathersEducation.addItem("")
        self.cmbFathersEducation.addItem("")
        self.cmbFathersJob = QtWidgets.QComboBox(Frame)
        self.cmbFathersJob.setGeometry(QtCore.QRect(140, 90, 111, 22))
        self.cmbFathersJob.setObjectName("cmbFathersJob")
        self.cmbFathersJob.addItem("")
        self.cmbFathersJob.addItem("")
        self.cmbFathersJob.addItem("")
        self.cmbFathersJob.addItem("")
        self.cmbFathersJob.addItem("")
        self.cmbFathersJob.addItem("")
        self.spnAbsences = QtWidgets.QSpinBox(Frame)
        self.spnAbsences.setGeometry(QtCore.QRect(200, 250, 41, 22))
        self.spnAbsences.setMaximum(93)
        self.spnAbsences.setObjectName("spnAbsences")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(140, 250, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(270, 250, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.spnG1 = QtWidgets.QSpinBox(Frame)
        self.spnG1.setGeometry(QtCore.QRect(300, 250, 41, 22))
        self.spnG1.setMaximum(20)
        self.spnG1.setObjectName("spnG1")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(390, 250, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spnG2 = QtWidgets.QSpinBox(Frame)
        self.spnG2.setGeometry(QtCore.QRect(420, 250, 41, 22))
        self.spnG2.setMaximum(20)
        self.spnG2.setObjectName("spnG2")
        self.btnUpdateSkills = QtWidgets.QPushButton(Frame)
        self.btnUpdateSkills.setGeometry(QtCore.QRect(180, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btnUpdateSkills.setFont(font)
        self.btnUpdateSkills.setObjectName("btnUpdateSkills")

        #===========================Adding Event to btnUpdateSkills==========================

        self.btnUpdateSkills.clicked.connect(self.funUpdateSkills)

        #====================================================================================

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Update Skills"))
        self.cmbAddress.setItemText(0, _translate("Frame", "Address"))
        self.cmbAddress.setItemText(1, _translate("Frame", "U"))
        self.cmbAddress.setItemText(2, _translate("Frame", "R"))
        self.cmbFamilySize.setItemText(0, _translate("Frame", "Family Size"))
        self.cmbFamilySize.setItemText(1, _translate("Frame", "LE3"))
        self.cmbFamilySize.setItemText(2, _translate("Frame", "GT3"))
        self.cmbMothersEducation.setItemText(0, _translate("Frame", "MothersEducation"))
        self.cmbMothersEducation.setItemText(1, _translate("Frame", "None"))
        self.cmbMothersEducation.setItemText(2, _translate("Frame", "Primary"))
        self.cmbMothersEducation.setItemText(3, _translate("Frame", "HighSchool"))
        self.cmbMothersEducation.setItemText(4, _translate("Frame", "PUC"))
        self.cmbMothersEducation.setItemText(5, _translate("Frame", "Degree"))
        self.cmbMothersJob.setItemText(0, _translate("Frame", "Mothers Job"))
        self.cmbMothersJob.setItemText(1, _translate("Frame", "Teacher"))
        self.cmbMothersJob.setItemText(2, _translate("Frame", "HealthCare"))
        self.cmbMothersJob.setItemText(3, _translate("Frame", "CivilServices"))
        self.cmbMothersJob.setItemText(4, _translate("Frame", "AtHome"))
        self.cmbMothersJob.setItemText(5, _translate("Frame", "Other"))
        self.cmbGuardian.setItemText(0, _translate("Frame", "Guardian"))
        self.cmbGuardian.setItemText(1, _translate("Frame", "Mother"))
        self.cmbGuardian.setItemText(2, _translate("Frame", "Father"))
        self.cmbGuardian.setItemText(3, _translate("Frame", "Other"))
        self.cmbTravelTime.setItemText(0, _translate("Frame", "TravelTime"))
        self.cmbTravelTime.setItemText(1, _translate("Frame", "15min"))
        self.cmbTravelTime.setItemText(2, _translate("Frame", "30min"))
        self.cmbTravelTime.setItemText(3, _translate("Frame", "1hr"))
        self.cmbTravelTime.setItemText(4, _translate("Frame", ">1hr"))
        self.cmbStudyTime.setItemText(0, _translate("Frame", "StudyTime"))
        self.cmbStudyTime.setItemText(1, _translate("Frame", "<2hr"))
        self.cmbStudyTime.setItemText(2, _translate("Frame", "2 to 5hr"))
        self.cmbStudyTime.setItemText(3, _translate("Frame", "5 to 10hr"))
        self.cmbStudyTime.setItemText(4, _translate("Frame", ">10hr"))
        self.cmbExtraEducationSupport.setItemText(0, _translate("Frame", "ExtraEduSupport"))
        self.cmbExtraEducationSupport.setItemText(1, _translate("Frame", "yes"))
        self.cmbExtraEducationSupport.setItemText(2, _translate("Frame", "no"))
        self.cmbPastFails.setItemText(0, _translate("Frame", "Past Fails"))
        self.cmbPastFails.setItemText(1, _translate("Frame", "0"))
        self.cmbPastFails.setItemText(2, _translate("Frame", "1"))
        self.cmbPastFails.setItemText(3, _translate("Frame", "2"))
        self.cmbPastFails.setItemText(4, _translate("Frame", "3"))
        self.cmbFamilySupport.setItemText(0, _translate("Frame", "FamilySupport"))
        self.cmbFamilySupport.setItemText(1, _translate("Frame", "yes"))
        self.cmbFamilySupport.setItemText(2, _translate("Frame", "no"))
        self.cmbTuitions.setItemText(0, _translate("Frame", "Tuitions"))
        self.cmbTuitions.setItemText(1, _translate("Frame", "yes"))
        self.cmbTuitions.setItemText(2, _translate("Frame", "no"))
        self.cmbHigherEducation.setItemText(0, _translate("Frame", "HigherEducation"))
        self.cmbHigherEducation.setItemText(1, _translate("Frame", "yes"))
        self.cmbHigherEducation.setItemText(2, _translate("Frame", "no"))
        self.cmbExtraActivities.setItemText(0, _translate("Frame", "ExtraActivities"))
        self.cmbExtraActivities.setItemText(1, _translate("Frame", "yes"))
        self.cmbExtraActivities.setItemText(2, _translate("Frame", "no"))
        self.cmbNetAccess.setItemText(0, _translate("Frame", "NetAccess"))
        self.cmbNetAccess.setItemText(1, _translate("Frame", "yes"))
        self.cmbNetAccess.setItemText(2, _translate("Frame", "no"))
        self.cmbRomantic.setItemText(0, _translate("Frame", "Romantic"))
        self.cmbRomantic.setItemText(1, _translate("Frame", "yes"))
        self.cmbRomantic.setItemText(2, _translate("Frame", "no"))
        self.cmbGoingOut.setItemText(0, _translate("Frame", "GoingOut"))
        self.cmbGoingOut.setItemText(1, _translate("Frame", "1"))
        self.cmbGoingOut.setItemText(2, _translate("Frame", "2"))
        self.cmbGoingOut.setItemText(3, _translate("Frame", "3"))
        self.cmbGoingOut.setItemText(4, _translate("Frame", "4"))
        self.cmbGoingOut.setItemText(5, _translate("Frame", "5"))
        self.cmbFreeTime.setItemText(0, _translate("Frame", "FreeTime"))
        self.cmbFreeTime.setItemText(1, _translate("Frame", "1"))
        self.cmbFreeTime.setItemText(2, _translate("Frame", "2"))
        self.cmbFreeTime.setItemText(3, _translate("Frame", "3"))
        self.cmbFreeTime.setItemText(4, _translate("Frame", "4"))
        self.cmbFreeTime.setItemText(5, _translate("Frame", "5"))
        self.cmbAlcoholConsumption.setItemText(0, _translate("Frame", "AlcoholConsumption"))
        self.cmbAlcoholConsumption.setItemText(1, _translate("Frame", "1"))
        self.cmbAlcoholConsumption.setItemText(2, _translate("Frame", "2"))
        self.cmbAlcoholConsumption.setItemText(3, _translate("Frame", "3"))
        self.cmbAlcoholConsumption.setItemText(4, _translate("Frame", "4"))
        self.cmbAlcoholConsumption.setItemText(5, _translate("Frame", "5"))
        self.cmbHealth.setItemText(0, _translate("Frame", "Health"))
        self.cmbHealth.setItemText(1, _translate("Frame", "1"))
        self.cmbHealth.setItemText(2, _translate("Frame", "2"))
        self.cmbHealth.setItemText(3, _translate("Frame", "3"))
        self.cmbHealth.setItemText(4, _translate("Frame", "4"))
        self.cmbHealth.setItemText(5, _translate("Frame", "5"))
        self.cmbFathersEducation.setItemText(0, _translate("Frame", "FathersEducation"))
        self.cmbFathersEducation.setItemText(1, _translate("Frame", "None"))
        self.cmbFathersEducation.setItemText(2, _translate("Frame", "Primary"))
        self.cmbFathersEducation.setItemText(3, _translate("Frame", "HighSchool"))
        self.cmbFathersEducation.setItemText(4, _translate("Frame", "PUC"))
        self.cmbFathersEducation.setItemText(5, _translate("Frame", "Degree"))
        self.cmbFathersJob.setItemText(0, _translate("Frame", "Fathers Job"))
        self.cmbFathersJob.setItemText(1, _translate("Frame", "Teacher"))
        self.cmbFathersJob.setItemText(2, _translate("Frame", "HealthCare"))
        self.cmbFathersJob.setItemText(3, _translate("Frame", "CivilServices"))
        self.cmbFathersJob.setItemText(4, _translate("Frame", "AtHome"))
        self.cmbFathersJob.setItemText(5, _translate("Frame", "Other"))
        self.label_2.setText(_translate("Frame", "Absences"))
        self.label_3.setText(_translate("Frame", "G1"))
        self.label_4.setText(_translate("Frame", "G2"))
        self.btnUpdateSkills.setText(_translate("Frame", "Update Skills"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = FrameUpdateSkills()
    ui.setupUi(Frame, 3)
    Frame.show()
    sys.exit(app.exec_())
