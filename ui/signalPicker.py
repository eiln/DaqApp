# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui\signalPicker.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signalPicker(object):
    def setupUi(self, signalPicker):
        signalPicker.setObjectName("signalPicker")
        signalPicker.resize(246, 227)
        self.verticalLayout = QtWidgets.QVBoxLayout(signalPicker)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(signalPicker)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nodeCombo = QtWidgets.QComboBox(signalPicker)
        self.nodeCombo.setObjectName("nodeCombo")
        self.verticalLayout.addWidget(self.nodeCombo)
        self.msgCombo = QtWidgets.QComboBox(signalPicker)
        self.msgCombo.setObjectName("msgCombo")
        self.verticalLayout.addWidget(self.msgCombo)
        self.signalList = QtWidgets.QListWidget(signalPicker)
        self.signalList.setObjectName("signalList")
        self.verticalLayout.addWidget(self.signalList)
        self.selectButton = QtWidgets.QPushButton(signalPicker)
        self.selectButton.setObjectName("selectButton")
        self.verticalLayout.addWidget(self.selectButton)

        self.retranslateUi(signalPicker)
        QtCore.QMetaObject.connectSlotsByName(signalPicker)

    def retranslateUi(self, signalPicker):
        _translate = QtCore.QCoreApplication.translate
        signalPicker.setWindowTitle(_translate("signalPicker", "Signal Picker"))
        self.label.setText(_translate("signalPicker", "Choose a Signal to Display"))
        self.selectButton.setText(_translate("signalPicker", "Select"))
