# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled1.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QWidget,QMessageBox)
from fastapi import requests
from sqlalchemy.sql.coercions import expect

from shared_manager import shared
import sys
import requests
import os
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(353, 136)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, 90, 341, 32))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 61, 20))
        self.label.setFont(font)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 30, 113, 20))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 61, 20))
        self.label_2.setFont(font)
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 60, 113, 20))
        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(250, 30, 67, 22))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(self.point)
        QMetaObject.connectSlotsByName(Dialog)
    # setupUi
    def point(self):
        try:
            id1 = int (self.lineEdit.text())
            dps = int (self.lineEdit_2.text())
            command = self.comboBox.currentIndex()
            dta = self.get_stu_info(id1)
            currentpoint = dta['point']
            if(command == 0):
                requests.put(f"http://{shared.ip}:8000/update/{id1}/1/a/{currentpoint+dps}")
                #os.system(f"curl -X PUT http://{shared.ip}:8000/update/{id1}/1/{currentpoint+dps}/a")
            elif(command == 1):
                if(currentpoint - dps < 0):
                    QMessageBox.critical(None,"错误","积分不足")
                    return
                requests.put(f"http://{shared.ip}:8000/update/{id1}/1/a/{currentpoint-dps}")
                #os.system(f"curl -X PUT http://{shared.ip}:8000/update/{id1}/1/{currentpoint-dps}/a")
            elif(command == 2):
                requests.put(f"http://{shared.ip}:8000/update/{id1}/1/a/{dps}")
                #os.system(f"curl -X PUT http://{shared.ip}:8000/update/{id1}/1/{dps}/a")
            QMessageBox.information(None,"信息","修改成功")
        except ValueError:
            QMessageBox.critical(None,"错误","参数非法")
        except requests.HTTPError as e:
            if(e.response.status_code == 404):
                QMessageBox.critical(None,"错误","找不到学生")
            else:
                QMessageBox.critical(None,"错误",f"错误代码为{e}！请联系开发者")
        except requests.exceptions.RequestException as e:
                QMessageBox.critical(None,"错误",f"请求异常，请联系开发者")
    def get_stu_info(self,id):
        id = int(id)
        response = requests.get(f"http://{shared.ip}:8000/student/{id}",timeout=5)
        response.raise_for_status()
        return response.json()['data']
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u5b66\u751fid", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u79ef\u5206\u53d8\u5316\u91cf:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u589e\u52a0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u51cf\u5c11", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u4fee\u6539", None))

    # retranslateUi

