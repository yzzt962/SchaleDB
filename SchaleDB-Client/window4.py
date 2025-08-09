# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
                               QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
                               QWidget,QMessageBox)
from shared_manager import shared
import requests

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(226, 118)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-150, 80, 341, 32))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setBold(True)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 61, 20))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei"])
        self.label.setFont(font1)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 30, 113, 20))

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(70, 60, 68, 16))
        self.checkBox.setFont(font)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.buttonBox.accepted.connect(self.del_stu)

        QMetaObject.connectSlotsByName(Dialog)
    def del_stu(self):
        if not self.checkBox.isChecked():
            QMessageBox.warning(None, "注意", "请确认删除")
            return

        try:
            stid = int(self.lineEdit.text())
            #print(f"curl -X DELETE http://{shared.ip}:8000/delete/{stid}")
            res = requests.delete(f"http://{shared.ip}:8000/delete/{stid}")
            QMessageBox.information(None, "信息", "删除成功")
            return
        except ValueError:
            QMessageBox.critical(None, "错误", "输入信息不合法")
            return
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"学生id", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"确认删除", None))