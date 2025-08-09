# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled3.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget,QMessageBox)
from sqlalchemy.sql.coercions import expect

from shared_manager import shared
import os
import sys
import requests
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(226, 118)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-140, 80, 341, 32))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 61, 20))
        self.label_2.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 20, 113, 20))
        self.lineEdit_3 = QLineEdit(Dialog)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 50, 113, 20))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 50, 61, 20))
        self.label_3.setFont(font)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(self.createstu)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    def createstu(self):
        name = self.lineEdit_2.text()
        point = self.lineEdit_3.text()
        try:
            point = int(point)
            requests.post(f"http://{shared.ip}:8000/create/{name}/{point}")
            QMessageBox.information(None,"提示","创建成功")
        except ValueError:
            QMessageBox.critical(None,"错误","积分数据不合法")
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u65b0\u59d3\u540d", None))
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u521d\u59cb\u79ef\u5206", None))
    # retranslateUi

