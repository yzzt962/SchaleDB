import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox,QPushButton,QLabel)
from PySide6.QtCore import *
from PySide6.QtGui import QFont
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 262)
        Form.setMinimumSize(QSize(400, 262))
        Form.setMaximumSize(QSize(400, 262))
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        Form.setFont(font)
        
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 70, 191, 61))
        font1 = QFont()
        font1.setFamilies([u"Microsoft YaHei UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 170, 191, 61))
        self.pushButton_2.setFont(font1)
        
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 20, 171, 41))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)
        
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"学生信息修改", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"修改积分", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"修改姓名", None))
        self.label.setText(QCoreApplication.translate("Form", u"修改学生信息", None))

class StudentInfoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # 连接信号槽
        self.ui.pushButton.clicked.connect(self.modify_points)
        self.ui.pushButton_2.clicked.connect(self.modify_name)
        
        # 初始化进程对象
        self.process = QProcess(self)
        self.process.finished.connect(self.on_process_finished)
        
        # 窗口居中显示
        self.center_window()
    
    def center_window(self):

        frame = self.frameGeometry()
        center_pos = self.screen().availableGeometry().center()
        frame.moveCenter(center_pos)
        self.move(frame.topLeft())
    
    def get_exe_path(self, exe_name):
        try:
            if getattr(sys, 'frozen', False):
                # 打包后的环境
                base_path = os.path.dirname(sys.executable)
            else:
                # 开发环境
                base_path = os.path.dirname(__file__)
            
            path = os.path.join(base_path, exe_name)
            
            # 检查文件是否存在
            if not os.path.exists(path):
                raise FileNotFoundError(f"找不到 {exe_name}")
                
            return path
        except Exception as e:
            QMessageBox.critical(self, "错误", f"路径获取失败: {str(e)}")
            return None
    
    def modify_points(self):
        exe_path = self.get_exe_path("udpoint.exe")
        if exe_path:
            self.run_exe(exe_path)
            sys.exit(0)
    def modify_name(self):
        exe_path = self.get_exe_path("cnlauncher.exe")
        if exe_path:
            self.run_exe(exe_path)
            sys.exit(0)
    def run_exe(self, exe_path):
        try:
            self.setEnabled(False) 
            
            if sys.platform == "win32":
                success = self.process.startDetached(exe_path)
                if not success:
                    raise RuntimeError("无法启动程序")
            else:
                self.process.start(exe_path)
        except Exception as e:
            self.setEnabled(True)
            QMessageBox.critical(self, "错误", f"程序启动失败: {str(e)}")
    
    def on_process_finished(self):
        self.setEnabled(True)  
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentInfoEditor()
    window.show()
    sys.exit(app.exec())