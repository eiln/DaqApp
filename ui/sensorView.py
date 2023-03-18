# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui\sensorView.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sensorView(object):
    def setupUi(self, sensorView):
        sensorView.setObjectName("sensorView")
        sensorView.resize(1771, 320)
        self.gridLayout = QtWidgets.QGridLayout(sensorView)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(sensorView)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_22 = DAQVariableDisplay(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_5.addWidget(self.label_22)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = CANVariableDisplay(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = CANVariableDisplay(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_25 = DAQVariableDisplay(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.verticalLayout.addWidget(self.label_25)
        self.label_26 = DAQVariableDisplay(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.verticalLayout.addWidget(self.label_26)
        self.label_14 = CANVariableDisplay(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_23 = DAQVariableDisplay(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        self.label_15 = CANVariableDisplay(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_11 = CANVariableDisplay(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_3.addWidget(self.label_11)
        self.label_12 = CANVariableDisplay(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.label_27 = DAQVariableDisplay(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_3.addWidget(self.label_27)
        self.label_13 = CANVariableDisplay(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_24 = DAQVariableDisplay(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_3.addWidget(self.label_24)
        self.label_16 = CANVariableDisplay(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox_2, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(sensorView)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = CANVariableDisplay(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = CANVariableDisplay(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = CANVariableDisplay(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = CANVariableDisplay(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = CANVariableDisplay(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.cal_steer_btn = QtWidgets.QPushButton(self.groupBox)
        self.cal_steer_btn.setObjectName("cal_steer_btn")
        self.verticalLayout_2.addWidget(self.cal_steer_btn)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(sensorView)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_17 = CANVariableDisplay(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_4.addWidget(self.label_17)
        self.label_18 = CANVariableDisplay(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_4.addWidget(self.label_18)
        self.label_19 = CANVariableDisplay(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_4.addWidget(self.label_19)
        self.label_20 = CANVariableDisplay(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_4.addWidget(self.label_20)
        self.label_21 = CANVariableDisplay(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_4.addWidget(self.label_21)
        self.gridLayout.addWidget(self.groupBox_5, 0, 0, 1, 1)

        self.retranslateUi(sensorView)
        QtCore.QMetaObject.connectSlotsByName(sensorView)

    def retranslateUi(self, sensorView):
        _translate = QtCore.QCoreApplication.translate
        sensorView.setWindowTitle(_translate("sensorView", "Form"))
        self.groupBox_2.setTitle(_translate("sensorView", "Cooling"))
        self.label_22.setText(_translate("sensorView", "Main_Module.daq_response_MAIN_MODULE.cooling_daq_override"))
        self.groupBox_3.setTitle(_translate("sensorView", "Battery Loop"))
        self.label_9.setText(_translate("sensorView", "Main_Module.flowrate_temps.battery_in_temp"))
        self.label_10.setText(_translate("sensorView", "Main_Module.flowrate_temps.battery_out_temp"))
        self.label_25.setText(_translate("sensorView", "Main_Module.daq_response_MAIN_MODULE.bat_pump"))
        self.label_26.setText(_translate("sensorView", "Main_Module.daq_response_MAIN_MODULE.bat_pump_aux"))
        self.label_14.setText(_translate("sensorView", "Main_Module.flowrate_temps.battery_flowrate"))
        self.label_23.setText(_translate("sensorView", "Main_Module.daq_response_MAIN_MODULE.bat_fan"))
        self.label_15.setText(_translate("sensorView", "Main_Module.flowrate_temps.battery_fan_speed"))
        self.groupBox_4.setTitle(_translate("sensorView", "Drivetrain Loop"))
        self.label_11.setText(_translate("sensorView", "Main_Module.flowrate_temps.drivetrain_in_temp"))
        self.label_12.setText(_translate("sensorView", "Main_Module.flowrate_temps.drivetrain_out_temp"))
        self.label_27.setText(_translate("sensorView", "Main_Module.daq_response_MAIN_MODULE.dt_pump"))
        self.label_13.setText(_translate("sensorView", "Main_Module.flowrate_temps.drivetrain_flowrate"))
        self.label_24.setText(_translate("sensorView", "Main_Module.daq_response_MAIN_MODULE.dt_fan"))
        self.label_16.setText(_translate("sensorView", "Main_Module.flowrate_temps.drivetrain_fan_speed"))
        self.groupBox.setTitle(_translate("sensorView", "Steering Angle"))
        self.label_4.setText(_translate("sensorView", "Steering.LWS_Standard.LWS_ANGLE"))
        self.label_5.setText(_translate("sensorView", "Steering.LWS_Standard.LWS_SPEED"))
        self.label_6.setText(_translate("sensorView", "Steering.LWS_Standard.Ok"))
        self.label_7.setText(_translate("sensorView", "Steering.LWS_Standard.Cal"))
        self.label_8.setText(_translate("sensorView", "Steering.LWS_Standard.Trim"))
        self.cal_steer_btn.setText(_translate("sensorView", "Calibrate"))
        self.groupBox_5.setTitle(_translate("sensorView", "Pedals"))
        self.label_17.setText(_translate("sensorView", "Dashboard.raw_throttle_brake.throttle"))
        self.label_18.setText(_translate("sensorView", "Dashboard.raw_throttle_brake.throttle_right"))
        self.label_19.setText(_translate("sensorView", "Dashboard.raw_throttle_brake.brake"))
        self.label_20.setText(_translate("sensorView", "Dashboard.raw_throttle_brake.brake_right"))
        self.label_21.setText(_translate("sensorView", "Dashboard.raw_throttle_brake.brake_pot"))
from display_widgets.variables.can_variable_display import CANVariableDisplay
from display_widgets.variables.daq_variable_display import DAQVariableDisplay
