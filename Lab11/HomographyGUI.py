# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomographyGUI.ui'
#
# Created: Thu Dec  1 14:59:03 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(916, 713)
        self.acq_points_pb = QtGui.QPushButton(Form)
        self.acq_points_pb.setGeometry(QtCore.QRect(450, 560, 161, 27))
        self.acq_points_pb.setObjectName("acq_points_pb")
        self.acq_points_pb.setCheckable(True)
        self.reset_pb = QtGui.QPushButton(Form)
        self.reset_pb.setGeometry(QtCore.QRect(720, 680, 92, 27))
        self.reset_pb.setObjectName("reset_pb")
        self.Effect_label = QtGui.QLabel(Form)
        self.Effect_label.setGeometry(QtCore.QRect(560, 640, 62, 17))
        self.Effect_label.setObjectName("Effect_label")
        self.source_image_gv = QtGui.QGraphicsView(Form)
        self.source_image_gv.setGeometry(QtCore.QRect(0, 40, 451, 511))
        self.source_image_gv.setObjectName("source_image_gv")
        self.target_image_gv = QtGui.QGraphicsView(Form)
        self.target_image_gv.setGeometry(QtCore.QRect(460, 40, 451, 511))
        self.target_image_gv.setObjectName("target_image_gv")
        self.load_source_pb = QtGui.QPushButton(Form)
        self.load_source_pb.setGeometry(QtCore.QRect(0, 10, 161, 27))
        self.load_source_pb.setObjectName("load_source_pb")
        self.Effect_option_cb = QtGui.QComboBox(Form)
        self.Effect_option_cb.setGeometry(QtCore.QRect(620, 630, 291, 27))
        self.Effect_option_cb.setObjectName("Effect_option_cb")
        self.Effect_option_cb.addItem("")
        self.Effect_option_cb.addItem("")
        self.Effect_option_cb.addItem("")
        self.Effect_option_cb.addItem("")
        self.Effect_option_cb.addItem("")
        self.Effect_option_cb.addItem("")
        self.Effect_option_cb.addItem("")
        self.save_pb = QtGui.QPushButton(Form)
        self.save_pb.setGeometry(QtCore.QRect(820, 680, 92, 27))
        self.save_pb.setObjectName("save_pb")
        self.low_right_le = QtGui.QLineEdit(Form)
        self.low_right_le.setGeometry(QtCore.QRect(770, 590, 141, 27))
        self.low_right_le.setObjectName("low_right_le")
        self.load_target_pb = QtGui.QPushButton(Form)
        self.load_target_pb.setGeometry(QtCore.QRect(460, 10, 161, 27))
        self.load_target_pb.setObjectName("load_target_pb")
        self.up_left_le = QtGui.QLineEdit(Form)
        self.up_left_le.setGeometry(QtCore.QRect(620, 560, 141, 27))
        self.up_left_le.setObjectName("up_left_le")
        self.up_right_le = QtGui.QLineEdit(Form)
        self.up_right_le.setGeometry(QtCore.QRect(770, 560, 141, 27))
        self.up_right_le.setObjectName("up_right_le")
        self.low_left_le = QtGui.QLineEdit(Form)
        self.low_left_le.setGeometry(QtCore.QRect(620, 590, 141, 27))
        self.low_left_le.setObjectName("low_left_le")
        self.transform_pb = QtGui.QPushButton(Form)
        self.transform_pb.setGeometry(QtCore.QRect(620, 680, 92, 27))
        self.transform_pb.setObjectName("transform_pb")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.acq_points_pb.setText(QtGui.QApplication.translate("Form", "Acquire Points", None, QtGui.QApplication.UnicodeUTF8))
        self.reset_pb.setText(QtGui.QApplication.translate("Form", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.Effect_label.setText(QtGui.QApplication.translate("Form", "EFFECT", None, QtGui.QApplication.UnicodeUTF8))
        self.load_source_pb.setText(QtGui.QApplication.translate("Form", "Load Source ...", None, QtGui.QApplication.UnicodeUTF8))
        self.Effect_option_cb.setItemText(0, QtGui.QApplication.translate("Form", "Nothing", None, QtGui.QApplication.UnicodeUTF8))
        self.Effect_option_cb.setItemText(1, QtGui.QApplication.translate("Form", "Rotate 90", None, QtGui.QApplication.UnicodeUTF8))
        self.Effect_option_cb.setItemText(2, QtGui.QApplication.translate("Form", "Rotate 180", None, QtGui.QApplication.UnicodeUTF8))
        self.Effect_option_cb.setItemText(3, QtGui.QApplication.translate("Form", "Rotate 270", None, QtGui.QApplication.UnicodeUTF8))
        self.Effect_option_cb.setItemText(4, QtGui.QApplication.translate("Form", "Flip Horizontally", None, QtGui.QApplication.UnicodeUTF8))
        self.Effect_option_cb.setItemText(5, QtGui.QApplication.translate("Form", "Flip Vertically", None, QtGui.QApplication.UnicodeUTF8))
        self.Effect_option_cb.setItemText(6, QtGui.QApplication.translate("Form", "Transpose", None, QtGui.QApplication.UnicodeUTF8))
        self.save_pb.setText(QtGui.QApplication.translate("Form", "Save ...", None, QtGui.QApplication.UnicodeUTF8))
        self.load_target_pb.setText(QtGui.QApplication.translate("Form", "Load Target ...", None, QtGui.QApplication.UnicodeUTF8))
        self.transform_pb.setText(QtGui.QApplication.translate("Form", "Transform", None, QtGui.QApplication.UnicodeUTF8))

