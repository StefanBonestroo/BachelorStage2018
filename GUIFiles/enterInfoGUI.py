# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'enterInfoGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_enterInfoWindow(object):
    def setupUi(self, enterInfoWindow):
        enterInfoWindow.setObjectName("enterInfoWindow")
        enterInfoWindow.resize(1110, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(enterInfoWindow.sizePolicy().hasHeightForWidth())
        enterInfoWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(enterInfoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setGeometry(QtCore.QRect(10, 10, 1091, 531))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setLineWidth(2)
        self.mainFrame.setObjectName("mainFrame")
        self.frame = QtWidgets.QFrame(self.mainFrame)
        self.frame.setGeometry(QtCore.QRect(220, 10, 481, 511))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(10, 10, 461, 491))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout_5.addWidget(self.label_31)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_39 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_39.setObjectName("label_39")
        self.horizontalLayout_15.addWidget(self.label_39)
        self.chamberNumberSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.chamberNumberSpinBox.setMinimum(1)
        self.chamberNumberSpinBox.setMaximum(4)
        self.chamberNumberSpinBox.setObjectName("chamberNumberSpinBox")
        self.horizontalLayout_15.addWidget(self.chamberNumberSpinBox)
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_15.addWidget(self.label_32)
        self.familyNameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.familyNameEdit.setText("")
        self.familyNameEdit.setObjectName("familyNameEdit")
        self.horizontalLayout_15.addWidget(self.familyNameEdit)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_33 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_33.setObjectName("label_33")
        self.horizontalLayout_11.addWidget(self.label_33)
        self.lineNameEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineNameEdit.setText("")
        self.lineNameEdit.setObjectName("lineNameEdit")
        self.horizontalLayout_11.addWidget(self.lineNameEdit)
        self.label_34 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout_11.addWidget(self.label_34)
        self.ageSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.ageSpinBox.setMinimum(0)
        self.ageSpinBox.setMaximum(31)
        self.ageSpinBox.setProperty("value", 2)
        self.ageSpinBox.setObjectName("ageSpinBox")
        self.horizontalLayout_11.addWidget(self.ageSpinBox)
        self.label_40 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_40.setObjectName("label_40")
        self.horizontalLayout_11.addWidget(self.label_40)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_5.addWidget(self.line_6)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_20.addWidget(self.label_11)
        self.preExperimentSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.preExperimentSpinBox.setMaximum(200)
        self.preExperimentSpinBox.setProperty("value", 120)
        self.preExperimentSpinBox.setObjectName("preExperimentSpinBox")
        self.horizontalLayout_20.addWidget(self.preExperimentSpinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_19.addWidget(self.label_21)
        self.timeFrameSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.timeFrameSpinBox.setMaximum(60)
        self.timeFrameSpinBox.setProperty("value", 30)
        self.timeFrameSpinBox.setObjectName("timeFrameSpinBox")
        self.horizontalLayout_19.addWidget(self.timeFrameSpinBox)
        self.verticalLayout_16.addLayout(self.horizontalLayout_19)
        self.horizontalLayout.addLayout(self.verticalLayout_16)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.stimulusLengthSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.stimulusLengthSpinBox.setMaximum(100)
        self.stimulusLengthSpinBox.setProperty("value", 1)
        self.stimulusLengthSpinBox.setObjectName("stimulusLengthSpinBox")
        self.horizontalLayout_16.addWidget(self.stimulusLengthSpinBox)
        self.verticalLayout_15.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_17.addWidget(self.label_10)
        self.intervalLengthSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.intervalLengthSpinBox.setMaximum(200)
        self.intervalLengthSpinBox.setProperty("value", 120)
        self.intervalLengthSpinBox.setObjectName("intervalLengthSpinBox")
        self.horizontalLayout_17.addWidget(self.intervalLengthSpinBox)
        self.verticalLayout_15.addLayout(self.horizontalLayout_17)
        self.horizontalLayout.addLayout(self.verticalLayout_15)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.line_8 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.verticalLayout_5.addWidget(self.line_8)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conOneEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conOneEdit.setText("")
        self.conOneEdit.setObjectName("conOneEdit")
        self.verticalLayout.addWidget(self.conOneEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conTwoEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conTwoEdit.setText("")
        self.conTwoEdit.setObjectName("conTwoEdit")
        self.verticalLayout_2.addWidget(self.conTwoEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conThreeEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conThreeEdit.setText("")
        self.conThreeEdit.setObjectName("conThreeEdit")
        self.verticalLayout_4.addWidget(self.conThreeEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conFourEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conFourEdit.setText("")
        self.conFourEdit.setObjectName("conFourEdit")
        self.verticalLayout_3.addWidget(self.conFourEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.conOneRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.conOneRadioButton.setAutoExclusive(False)
        self.conOneRadioButton.setObjectName("conOneRadioButton")
        self.verticalLayout_6.addWidget(self.conOneRadioButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conOneFamilyLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conOneFamilyLabel.setEnabled(False)
        self.conOneFamilyLabel.setObjectName("conOneFamilyLabel")
        self.verticalLayout_6.addWidget(self.conOneFamilyLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conOneFamilyEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conOneFamilyEdit.setEnabled(False)
        self.conOneFamilyEdit.setObjectName("conOneFamilyEdit")
        self.verticalLayout_6.addWidget(self.conOneFamilyEdit)
        self.conOneLineLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conOneLineLabel.setEnabled(False)
        self.conOneLineLabel.setObjectName("conOneLineLabel")
        self.verticalLayout_6.addWidget(self.conOneLineLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conOneLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conOneLineEdit.setEnabled(False)
        self.conOneLineEdit.setObjectName("conOneLineEdit")
        self.verticalLayout_6.addWidget(self.conOneLineEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.conOneAgeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conOneAgeLabel.setEnabled(False)
        self.conOneAgeLabel.setObjectName("conOneAgeLabel")
        self.horizontalLayout_4.addWidget(self.conOneAgeLabel)
        self.conOneAgeSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.conOneAgeSpinBox.setEnabled(False)
        self.conOneAgeSpinBox.setMinimum(0)
        self.conOneAgeSpinBox.setMaximum(31)
        self.conOneAgeSpinBox.setObjectName("conOneAgeSpinBox")
        self.horizontalLayout_4.addWidget(self.conOneAgeSpinBox, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_3.addWidget(self.line_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.conTwoRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.conTwoRadioButton.setAutoExclusive(False)
        self.conTwoRadioButton.setObjectName("conTwoRadioButton")
        self.verticalLayout_8.addWidget(self.conTwoRadioButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conTwoFamilyLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conTwoFamilyLabel.setEnabled(False)
        self.conTwoFamilyLabel.setObjectName("conTwoFamilyLabel")
        self.verticalLayout_8.addWidget(self.conTwoFamilyLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conTwoFamilyEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conTwoFamilyEdit.setEnabled(False)
        self.conTwoFamilyEdit.setObjectName("conTwoFamilyEdit")
        self.verticalLayout_8.addWidget(self.conTwoFamilyEdit)
        self.conTwoLineLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conTwoLineLabel.setEnabled(False)
        self.conTwoLineLabel.setObjectName("conTwoLineLabel")
        self.verticalLayout_8.addWidget(self.conTwoLineLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conTwoLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conTwoLineEdit.setEnabled(False)
        self.conTwoLineEdit.setObjectName("conTwoLineEdit")
        self.verticalLayout_8.addWidget(self.conTwoLineEdit)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.conTwoAgeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conTwoAgeLabel.setEnabled(False)
        self.conTwoAgeLabel.setObjectName("conTwoAgeLabel")
        self.horizontalLayout_7.addWidget(self.conTwoAgeLabel)
        self.conTwoAgeSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.conTwoAgeSpinBox.setEnabled(False)
        self.conTwoAgeSpinBox.setMinimum(0)
        self.conTwoAgeSpinBox.setMaximum(31)
        self.conTwoAgeSpinBox.setObjectName("conTwoAgeSpinBox")
        self.horizontalLayout_7.addWidget(self.conTwoAgeSpinBox, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.conThreeRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.conThreeRadioButton.setAutoExclusive(False)
        self.conThreeRadioButton.setObjectName("conThreeRadioButton")
        self.verticalLayout_7.addWidget(self.conThreeRadioButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conThreeFamilyLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conThreeFamilyLabel.setEnabled(False)
        self.conThreeFamilyLabel.setObjectName("conThreeFamilyLabel")
        self.verticalLayout_7.addWidget(self.conThreeFamilyLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conThreeFamilyEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conThreeFamilyEdit.setEnabled(False)
        self.conThreeFamilyEdit.setObjectName("conThreeFamilyEdit")
        self.verticalLayout_7.addWidget(self.conThreeFamilyEdit)
        self.conThreeLineLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conThreeLineLabel.setEnabled(False)
        self.conThreeLineLabel.setObjectName("conThreeLineLabel")
        self.verticalLayout_7.addWidget(self.conThreeLineLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conThreeLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conThreeLineEdit.setEnabled(False)
        self.conThreeLineEdit.setObjectName("conThreeLineEdit")
        self.verticalLayout_7.addWidget(self.conThreeLineEdit)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.conThreeAgeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conThreeAgeLabel.setEnabled(False)
        self.conThreeAgeLabel.setObjectName("conThreeAgeLabel")
        self.horizontalLayout_6.addWidget(self.conThreeAgeLabel)
        self.conThreeAgeSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.conThreeAgeSpinBox.setEnabled(False)
        self.conThreeAgeSpinBox.setMinimum(0)
        self.conThreeAgeSpinBox.setMaximum(31)
        self.conThreeAgeSpinBox.setObjectName("conThreeAgeSpinBox")
        self.horizontalLayout_6.addWidget(self.conThreeAgeSpinBox, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_5)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.conFourRadioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_5)
        self.conFourRadioButton.setAutoExclusive(False)
        self.conFourRadioButton.setObjectName("conFourRadioButton")
        self.verticalLayout_9.addWidget(self.conFourRadioButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conFourFamilyLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conFourFamilyLabel.setEnabled(False)
        self.conFourFamilyLabel.setObjectName("conFourFamilyLabel")
        self.verticalLayout_9.addWidget(self.conFourFamilyLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conFourFamilyEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conFourFamilyEdit.setEnabled(False)
        self.conFourFamilyEdit.setObjectName("conFourFamilyEdit")
        self.verticalLayout_9.addWidget(self.conFourFamilyEdit)
        self.conFourLineLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conFourLineLabel.setEnabled(False)
        self.conFourLineLabel.setObjectName("conFourLineLabel")
        self.verticalLayout_9.addWidget(self.conFourLineLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.conFourLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.conFourLineEdit.setEnabled(False)
        self.conFourLineEdit.setObjectName("conFourLineEdit")
        self.verticalLayout_9.addWidget(self.conFourLineEdit)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.conFourAgeLabel = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.conFourAgeLabel.setEnabled(False)
        self.conFourAgeLabel.setObjectName("conFourAgeLabel")
        self.horizontalLayout_5.addWidget(self.conFourAgeLabel)
        self.conFourAgeSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_5)
        self.conFourAgeSpinBox.setEnabled(False)
        self.conFourAgeSpinBox.setMinimum(0)
        self.conFourAgeSpinBox.setMaximum(31)
        self.conFourAgeSpinBox.setProperty("value", 2)
        self.conFourAgeSpinBox.setObjectName("conFourAgeSpinBox")
        self.horizontalLayout_5.addWidget(self.conFourAgeSpinBox, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.mainFrame)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(710, 10, 371, 481))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_12.addWidget(self.label_30, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_12.addWidget(self.label_28)
        self.habituationSetUpSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_13)
        self.habituationSetUpSpinBox.setProperty("value", 10)
        self.habituationSetUpSpinBox.setObjectName("habituationSetUpSpinBox")
        self.horizontalLayout_12.addWidget(self.habituationSetUpSpinBox)
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_12.addWidget(self.label_29)
        self.habituationLightsSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_13)
        self.habituationLightsSpinBox.setProperty("value", 10)
        self.habituationLightsSpinBox.setObjectName("habituationLightsSpinBox")
        self.horizontalLayout_12.addWidget(self.habituationLightsSpinBox)
        self.verticalLayout_12.addLayout(self.horizontalLayout_12)
        self.verticalLayout_13.addLayout(self.verticalLayout_12)
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget_13)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_13.addWidget(self.line_5)
        self.label_35 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.verticalLayout_13.addWidget(self.label_35)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_8.addWidget(self.label_15, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.temperatureSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_13)
        self.temperatureSpinBox.setProperty("value", 24)
        self.temperatureSpinBox.setObjectName("temperatureSpinBox")
        self.horizontalLayout_8.addWidget(self.temperatureSpinBox)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_9.addWidget(self.label_17, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.humiditySpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_13)
        self.humiditySpinBox.setProperty("value", 33)
        self.humiditySpinBox.setObjectName("humiditySpinBox")
        self.horizontalLayout_9.addWidget(self.humiditySpinBox)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_9.addWidget(self.label_18, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_10.addWidget(self.label_19, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.flowSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_13)
        self.flowSpinBox.setProperty("value", 17)
        self.flowSpinBox.setObjectName("flowSpinBox")
        self.horizontalLayout_10.addWidget(self.flowSpinBox)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_10.addWidget(self.label_20)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_18.addLayout(self.verticalLayout_11)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_36 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_36.setObjectName("label_36")
        self.verticalLayout_14.addWidget(self.label_36, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_37 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_13.addWidget(self.label_37)
        self.experimentDaySpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_13)
        self.experimentDaySpinBox.setMinimum(1)
        self.experimentDaySpinBox.setMaximum(31)
        self.experimentDaySpinBox.setProperty("value", 4)
        self.experimentDaySpinBox.setObjectName("experimentDaySpinBox")
        self.horizontalLayout_13.addWidget(self.experimentDaySpinBox)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_13.addWidget(self.label_7)
        self.experimentMonthSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_13)
        self.experimentMonthSpinBox.setMinimum(1)
        self.experimentMonthSpinBox.setMaximum(12)
        self.experimentMonthSpinBox.setProperty("value", 4)
        self.experimentMonthSpinBox.setObjectName("experimentMonthSpinBox")
        self.horizontalLayout_13.addWidget(self.experimentMonthSpinBox)
        self.verticalLayout_14.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_38 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_38.setObjectName("label_38")
        self.horizontalLayout_14.addWidget(self.label_38)
        self.experimentHourSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_13)
        self.experimentHourSpinBox.setMaximum(23)
        self.experimentHourSpinBox.setProperty("value", 16)
        self.experimentHourSpinBox.setObjectName("experimentHourSpinBox")
        self.horizontalLayout_14.addWidget(self.experimentHourSpinBox)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_14.addWidget(self.label_8)
        self.experimentMinutesSpinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget_13)
        self.experimentMinutesSpinBox.setMaximum(59)
        self.experimentMinutesSpinBox.setObjectName("experimentMinutesSpinBox")
        self.horizontalLayout_14.addWidget(self.experimentMinutesSpinBox)
        self.verticalLayout_14.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_18.addLayout(self.verticalLayout_14)
        self.verticalLayout_13.addLayout(self.horizontalLayout_18)
        self.line_7 = QtWidgets.QFrame(self.verticalLayoutWidget_13)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout_13.addWidget(self.line_7)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.notesTextEdit = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_13)
        self.notesTextEdit.setPlainText("")
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.verticalLayout_10.addWidget(self.notesTextEdit)
        self.verticalLayout_13.addLayout(self.verticalLayout_10)
        self.saveOutputButton = QtWidgets.QPushButton(self.mainFrame)
        self.saveOutputButton.setGeometry(QtCore.QRect(710, 490, 371, 31))
        self.saveOutputButton.setObjectName("saveOutputButton")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.mainFrame)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 201, 511))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_17.addWidget(self.label_6)
        self.rawDataList = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.rawDataList.setObjectName("rawDataList")
        self.verticalLayout_17.addWidget(self.rawDataList)
        self.setRawDataDirectoryButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.setRawDataDirectoryButton.setObjectName("setRawDataDirectoryButton")
        self.verticalLayout_17.addWidget(self.setRawDataDirectoryButton)
        self.line_9 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.verticalLayout_17.addWidget(self.line_9)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_17.addWidget(self.label_13)
        self.outputDataList = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.outputDataList.setObjectName("outputDataList")
        self.verticalLayout_17.addWidget(self.outputDataList)
        self.setOutputDataDirectoryButton = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.setOutputDataDirectoryButton.setObjectName("setOutputDataDirectoryButton")
        self.verticalLayout_17.addWidget(self.setOutputDataDirectoryButton)
        enterInfoWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(enterInfoWindow)
        self.statusbar.setObjectName("statusbar")
        enterInfoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(enterInfoWindow)
        QtCore.QMetaObject.connectSlotsByName(enterInfoWindow)

    def retranslateUi(self, enterInfoWindow):
        _translate = QtCore.QCoreApplication.translate
        enterInfoWindow.setWindowTitle(_translate("enterInfoWindow", "Enter Info"))
        self.label_31.setText(_translate("enterInfoWindow", "Individual"))
        self.label_39.setText(_translate("enterInfoWindow", "Chamber:"))
        self.label_32.setText(_translate("enterInfoWindow", "Family name:"))
        self.label_33.setText(_translate("enterInfoWindow", "Line:"))
        self.label_34.setText(_translate("enterInfoWindow", "Age:"))
        self.label_40.setText(_translate("enterInfoWindow", "day(s)"))
        self.label_12.setText(_translate("enterInfoWindow", "Stimulus protocol"))
        self.label_11.setText(_translate("enterInfoWindow", "Pre-experiment time (s):"))
        self.label_21.setText(_translate("enterInfoWindow", "Time frame (s):"))
        self.label_9.setText(_translate("enterInfoWindow", "Stimulus length (s):"))
        self.label_10.setText(_translate("enterInfoWindow", "Interval length (s):"))
        self.label_5.setText(_translate("enterInfoWindow", "Conditions"))
        self.label.setText(_translate("enterInfoWindow", "1"))
        self.label_2.setText(_translate("enterInfoWindow", "2"))
        self.label_3.setText(_translate("enterInfoWindow", "3"))
        self.label_4.setText(_translate("enterInfoWindow", "4"))
        self.conOneRadioButton.setText(_translate("enterInfoWindow", "Add Info"))
        self.conOneFamilyLabel.setText(_translate("enterInfoWindow", "Family name"))
        self.conOneLineLabel.setText(_translate("enterInfoWindow", "Line"))
        self.conOneAgeLabel.setText(_translate("enterInfoWindow", "Age"))
        self.conTwoRadioButton.setText(_translate("enterInfoWindow", "Add Info"))
        self.conTwoFamilyLabel.setText(_translate("enterInfoWindow", "Family name"))
        self.conTwoLineLabel.setText(_translate("enterInfoWindow", "Line"))
        self.conTwoAgeLabel.setText(_translate("enterInfoWindow", "Age"))
        self.conThreeRadioButton.setText(_translate("enterInfoWindow", "Add Info"))
        self.conThreeFamilyLabel.setText(_translate("enterInfoWindow", "Family name"))
        self.conThreeFamilyEdit.setText(_translate("enterInfoWindow", "HV Family"))
        self.conThreeLineLabel.setText(_translate("enterInfoWindow", "Line"))
        self.conThreeLineEdit.setText(_translate("enterInfoWindow", "HV Line"))
        self.conThreeAgeLabel.setText(_translate("enterInfoWindow", "Age"))
        self.conFourRadioButton.setText(_translate("enterInfoWindow", "Add Info"))
        self.conFourFamilyLabel.setText(_translate("enterInfoWindow", "Family name"))
        self.conFourFamilyEdit.setText(_translate("enterInfoWindow", "HS Family"))
        self.conFourLineLabel.setText(_translate("enterInfoWindow", "Line"))
        self.conFourLineEdit.setText(_translate("enterInfoWindow", "HS Line"))
        self.conFourAgeLabel.setText(_translate("enterInfoWindow", "Age"))
        self.label_30.setText(_translate("enterInfoWindow", "Habituation times (minutes):"))
        self.label_28.setText(_translate("enterInfoWindow", "In set-up:"))
        self.label_29.setText(_translate("enterInfoWindow", "Lights on:"))
        self.label_35.setText(_translate("enterInfoWindow", "Environment:"))
        self.label_15.setText(_translate("enterInfoWindow", "Temperature:"))
        self.label_16.setText(_translate("enterInfoWindow", "° C"))
        self.label_17.setText(_translate("enterInfoWindow", "Humidity:"))
        self.label_18.setText(_translate("enterInfoWindow", "%"))
        self.label_19.setText(_translate("enterInfoWindow", "Flow:"))
        self.label_36.setText(_translate("enterInfoWindow", "Additional data:"))
        self.label_37.setText(_translate("enterInfoWindow", "Date:"))
        self.label_7.setText(_translate("enterInfoWindow", "-"))
        self.label_38.setText(_translate("enterInfoWindow", "Time:"))
        self.label_8.setText(_translate("enterInfoWindow", ":"))
        self.label_14.setText(_translate("enterInfoWindow", "Notes"))
        self.saveOutputButton.setText(_translate("enterInfoWindow", "Save Output"))
        self.label_6.setText(_translate("enterInfoWindow", "Raw data input"))
        self.setRawDataDirectoryButton.setText(_translate("enterInfoWindow", "Set Input Directory..."))
        self.label_13.setText(_translate("enterInfoWindow", "Output data file"))
        self.setOutputDataDirectoryButton.setText(_translate("enterInfoWindow", "Set Output Directory..."))

