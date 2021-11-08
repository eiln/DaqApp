# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui\preferencesEditor.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_preferencesEditor(object):
    def setupUi(self, preferencesEditor):
        preferencesEditor.setObjectName("preferencesEditor")
        preferencesEditor.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(preferencesEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(preferencesEditor)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.xRangeSpin = QtWidgets.QSpinBox(preferencesEditor)
        self.xRangeSpin.setObjectName("xRangeSpin")
        self.horizontalLayout.addWidget(self.xRangeSpin)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.resetButton = QtWidgets.QPushButton(preferencesEditor)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_2.addWidget(self.resetButton)
        self.saveButton = QtWidgets.QPushButton(preferencesEditor)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(preferencesEditor)
        QtCore.QMetaObject.connectSlotsByName(preferencesEditor)

    def retranslateUi(self, preferencesEditor):
        _translate = QtCore.QCoreApplication.translate
        preferencesEditor.setWindowTitle(_translate("preferencesEditor", "Preferences"))
        self.label.setText(_translate("preferencesEditor", "Plot scrolling X range (seconds):"))
        self.resetButton.setText(_translate("preferencesEditor", "Reset"))
        self.saveButton.setText(_translate("preferencesEditor", "Save and Close"))
