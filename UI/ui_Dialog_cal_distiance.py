# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_cal_distiance.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(642, 444)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_m_1 = QtWidgets.QWidget(self.groupBox_6)
        self.widget_m_1.setObjectName("widget_m_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_m_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_dd_1 = QtWidgets.QLineEdit(self.widget_m_1)
        self.lineEdit_dd_1.setObjectName("lineEdit_dd_1")
        self.horizontalLayout.addWidget(self.lineEdit_dd_1)
        self.pushButton_dd2dm = QtWidgets.QPushButton(self.widget_m_1)
        self.pushButton_dd2dm.setObjectName("pushButton_dd2dm")
        self.horizontalLayout.addWidget(self.pushButton_dd2dm)
        self.lineEdit_dm_1 = QtWidgets.QLineEdit(self.widget_m_1)
        self.lineEdit_dm_1.setObjectName("lineEdit_dm_1")
        self.horizontalLayout.addWidget(self.lineEdit_dm_1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_m_1)
        self.widget_4 = QtWidgets.QWidget(self.groupBox_6)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_dm_2 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_dm_2.setObjectName("lineEdit_dm_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_dm_2)
        self.pushButton_dm2dd = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_dm2dd.setObjectName("pushButton_dm2dd")
        self.horizontalLayout_3.addWidget(self.pushButton_dm2dd)
        self.lineEdit_dd_2 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_dd_2.setText("")
        self.lineEdit_dd_2.setObjectName("lineEdit_dd_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_dd_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_3 = QtWidgets.QWidget(self.groupBox_6)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_dd_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_dd_3.setObjectName("lineEdit_dd_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_dd_3)
        self.pushButton_dd2dms = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_dd2dms.setObjectName("pushButton_dd2dms")
        self.horizontalLayout_2.addWidget(self.pushButton_dd2dms)
        self.lineEdit_d_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_d_3.setText("")
        self.lineEdit_d_3.setObjectName("lineEdit_d_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_d_3)
        self.lineEdit_m_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_m_3.setText("")
        self.lineEdit_m_3.setObjectName("lineEdit_m_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_m_3)
        self.lineEdit_s_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_s_3.setText("")
        self.lineEdit_s_3.setObjectName("lineEdit_s_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_s_3)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_5 = QtWidgets.QWidget(self.groupBox_6)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_d_4 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_d_4.setObjectName("lineEdit_d_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_d_4)
        self.lineEdit_m_4 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_m_4.setObjectName("lineEdit_m_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_m_4)
        self.lineEdit_s_4 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_s_4.setText("")
        self.lineEdit_s_4.setObjectName("lineEdit_s_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_s_4)
        self.pushButton_dms2dd = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_dms2dd.setObjectName("pushButton_dms2dd")
        self.horizontalLayout_4.addWidget(self.pushButton_dms2dd)
        self.lineEdit_dd_4 = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_dd_4.setText("")
        self.lineEdit_dd_4.setObjectName("lineEdit_dd_4")
        self.horizontalLayout_4.addWidget(self.lineEdit_dd_4)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.verticalLayout_4.addWidget(self.groupBox_6)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.groupBox)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.widget_6)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.lineEdit_lat1 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_lat1.setObjectName("lineEdit_lat1")
        self.horizontalLayout_5.addWidget(self.lineEdit_lat1)
        self.label_8 = QtWidgets.QLabel(self.widget_6)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.lineEdit_lon1 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_lon1.setObjectName("lineEdit_lon1")
        self.horizontalLayout_5.addWidget(self.lineEdit_lon1)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.widget_9 = QtWidgets.QWidget(self.groupBox)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.widget_9)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.lineEdit_lat2 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_lat2.setObjectName("lineEdit_lat2")
        self.horizontalLayout_6.addWidget(self.lineEdit_lat2)
        self.label_9 = QtWidgets.QLabel(self.widget_9)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.lineEdit_lon2 = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_lon2.setObjectName("lineEdit_lon2")
        self.horizontalLayout_6.addWidget(self.lineEdit_lon2)
        self.verticalLayout_3.addWidget(self.widget_9)
        self.widget_8 = QtWidgets.QWidget(self.groupBox)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_2distance = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_2distance.setObjectName("pushButton_2distance")
        self.horizontalLayout_7.addWidget(self.pushButton_2distance)
        self.lineEdit_distance = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_distance.setText("")
        self.lineEdit_distance.setObjectName("lineEdit_distance")
        self.horizontalLayout_7.addWidget(self.lineEdit_distance)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.widget_8)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "距离计算工具"))
        self.groupBox_6.setTitle(_translate("Dialog", "经纬度转换"))
        self.lineEdit_dd_1.setPlaceholderText(_translate("Dialog", "ddd.dddddd"))
        self.pushButton_dd2dm.setText(_translate("Dialog", "度转度分"))
        self.lineEdit_dm_1.setPlaceholderText(_translate("Dialog", "dddmm.mmmm"))
        self.lineEdit_dm_2.setPlaceholderText(_translate("Dialog", "dddmm.mmmm"))
        self.pushButton_dm2dd.setText(_translate("Dialog", "度分转度"))
        self.lineEdit_dd_2.setPlaceholderText(_translate("Dialog", "度"))
        self.lineEdit_dd_3.setPlaceholderText(_translate("Dialog", "ddd.dddddd"))
        self.pushButton_dd2dms.setText(_translate("Dialog", "度转度分秒"))
        self.lineEdit_d_3.setPlaceholderText(_translate("Dialog", "ddd"))
        self.lineEdit_m_3.setPlaceholderText(_translate("Dialog", "mm"))
        self.lineEdit_s_3.setPlaceholderText(_translate("Dialog", "ss.ssss"))
        self.lineEdit_d_4.setPlaceholderText(_translate("Dialog", "ddd"))
        self.lineEdit_m_4.setPlaceholderText(_translate("Dialog", "mm"))
        self.lineEdit_s_4.setPlaceholderText(_translate("Dialog", "ss.ssss"))
        self.pushButton_dms2dd.setText(_translate("Dialog", "度分秒转度"))
        self.lineEdit_dd_4.setPlaceholderText(_translate("Dialog", "ddd.dddddd"))
        self.groupBox.setTitle(_translate("Dialog", "距离计算"))
        self.label_10.setText(_translate("Dialog", "纬度1："))
        self.lineEdit_lat1.setPlaceholderText(_translate("Dialog", "单位：度"))
        self.label_8.setText(_translate("Dialog", "经度1："))
        self.lineEdit_lon1.setPlaceholderText(_translate("Dialog", "单位：度"))
        self.label_11.setText(_translate("Dialog", "纬度2："))
        self.lineEdit_lat2.setPlaceholderText(_translate("Dialog", "单位：度"))
        self.label_9.setText(_translate("Dialog", "经度2："))
        self.lineEdit_lon2.setPlaceholderText(_translate("Dialog", "单位：度"))
        self.pushButton_2distance.setText(_translate("Dialog", "计算距离（米）"))
