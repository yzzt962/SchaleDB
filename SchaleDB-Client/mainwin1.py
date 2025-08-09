import sys
import os
import json
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QTimer,
    QSize, QTime, QUrl, Qt, QProcess)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QToolBar, QWidget, QMessageBox)
from PySide6.QtNetwork import *
# 假设 shared.py 存在并包含IP信息
try:
    from shared_manager import shared
except ImportError:
    class Shared:
        ip = "localhost"  # 默认值
    shared = Shared()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(423, 494)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        
        # 创建动作
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.action_5 = QAction(MainWindow)
        self.action_5.setObjectName(u"action_5")
        self.action_6 = QAction(MainWindow)
        self.action_6.setObjectName(u"action_6")
        self.action_7 = QAction(MainWindow)
        self.action_7.setObjectName(u"action_7")
        self.action_8 = QAction(MainWindow)
        self.action_8.setObjectName(u"action_8")
        self.action_9 = QAction(MainWindow)
        self.action_9.setObjectName(u"action_9")
        self.action_10 = QAction(MainWindow)
        self.action_10.setObjectName(u"action_10")
        self.action_11 = QAction(MainWindow)
        self.action_11.setObjectName(u"action_11")

        # 中央部件
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")

        # 按钮和标签
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei UI"])
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.gridLayout.addWidget(self.pushButton_3, 13, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(40)
        self.label.setFont(font1)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(10)
        self.label_2.setFont(font2)
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        # 表格部件
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.gridLayout.addWidget(self.tableWidget, 5, 0, 1, 4)

        # 更多界面元素...
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font)
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)
        self.gridLayout.addWidget(self.pushButton, 6, 1, 1, 3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 2)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font)
        self.gridLayout.addWidget(self.pushButton_4, 13, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        
        # 菜单栏
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 423, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        
        # 状态栏
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # 工具栏
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        # 连接信号槽
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_11)
        self.menu_2.addAction(self.action_5)
        self.menu_3.addAction(self.action_9)
        self.menu_3.addAction(self.action_10)
        self.toolBar.addAction(self.action)
        self.toolBar.addAction(self.action_2)
        
        # 按钮连接
        self.pushButton_2.clicked.connect(self.action.triggered)
        self.pushButton.clicked.connect(self.action_2.triggered)
        self.pushButton_4.clicked.connect(self.action_11.triggered)
        self.pushButton_3.clicked.connect(self.action_4.triggered)
        
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"学生管理系统", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"添加学生", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"修改学生信息", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"修改姓名", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"删除学生", None))
        self.action_5.setText(QCoreApplication.translate("MainWindow", u"服务器连接", None))
        self.action_6.setText(QCoreApplication.translate("MainWindow", u"致谢", None))
        self.action_7.setText(QCoreApplication.translate("MainWindow", u"使用帮助", None))
        self.action_8.setText(QCoreApplication.translate("MainWindow", u"联系作者", None))
        self.action_9.setText(QCoreApplication.translate("MainWindow", u"更新日志", None))
        self.action_10.setText(QCoreApplication.translate("MainWindow", u"关于", None))
        self.action_11.setText(QCoreApplication.translate("MainWindow", u"退出", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"删除学生", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"SchaleDB Client", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"基于MySQL的学生管理客户端", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"学号(id)", None))
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"姓名", None))
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"积分", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"添加学生", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"修改学生信息", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"您的班级", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"退出", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"文件", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"设置", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"帮助", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))

class StudentInfoEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # 初始化进程对象
        self.process = QProcess(self)
        self.process.finished.connect(self.on_process_finished)
        
        # 网络管理器
        self.network_manager = QNetworkAccessManager()
        self.network_manager.finished.connect(self.handle_response)
        
        # 定时刷新
        self.refresh_timer = QTimer()
        self.refresh_timer.timeout.connect(self.fetch_student_data)
        self.refresh_interval = 5000  # 5秒刷新一次
        
        self.center_window()
        self.ui.action.triggered.connect(lambda: self.creates())
        self.ui.action_2.triggered.connect(lambda: self.modify())
        self.ui.action_4.triggered.connect(lambda: self.dele())
        self.ui.action_5.triggered.connect(lambda: self.cs())
        self.ui.action_9.triggered.connect(lambda: self.udlog())
        self.ui.action_10.triggered.connect(lambda: self.ab())
        self.ui.action_11.triggered.connect(sys.exit)
        
        # 初始加载数据
        self.fetch_student_data()
        self.start_auto_refresh()
        self.safety_timer = QTimer()
        self.safety_timer.setSingleShot(True)
        self.safety_timer.timeout.connect(lambda: self.setEnabled(True))
        self.safety_timer.start(10000)
    def center_window(self):
        """居中显示窗口"""
        frame = self.frameGeometry()
        center_pos = self.screen().availableGeometry().center()
        frame.moveCenter(center_pos)
        self.move(frame.topLeft())
    
    def start_auto_refresh(self):
        """启动自动刷新定时器"""
        self.refresh_timer.start(self.refresh_interval)
    
    def stop_auto_refresh(self):
        """停止自动刷新"""
        self.refresh_timer.stop()
    
    def fetch_student_data(self):
        """从服务器获取学生数据"""
        if not hasattr(self, 'network_manager'):
            return
            
        # 显示加载状态
        self.ui.tableWidget.setEnabled(False)
        
        # 构建请求URL
        url = QUrl(f"http://{shared.ip}:8000/list")
        request = QNetworkRequest(url)
        self.network_manager.get(request)
    def handle_response(self, reply):
        try:
            self.ui.tableWidget.setEnabled(True)
        
            error = reply.error()
            if error != QNetworkReply.NoError:
                error_msg = {
                    QNetworkReply.ConnectionRefusedError: "连接被拒绝",
                    QNetworkReply.HostNotFoundError: "找不到服务器",
                    QNetworkReply.TimeoutError: "请求超时",
                    QNetworkReply.UnknownNetworkError: "未知网络错误"
                }.get(error, reply.errorString())
            
                self.show_error_message(f"网络请求失败({error}): {error_msg}")
                return
        
        # 检查HTTP状态码
            status_code = reply.attribute(QNetworkRequest.HttpStatusCodeAttribute)
            if status_code != 200:
                self.show_error_message(f"服务器返回错误状态码: {status_code}")
                return
            
            data = reply.readAll().data().decode('utf-8')
            print(f"服务器响应: {data}")  # 调试输出
        
            try:
                result = json.loads(data)
                if result['status'] == "success":
                    self.populate_table(result['students'])
                else:
                    self.show_warning_message(f"服务器返回错误: {result.get('message', '未知错误')}")
            except json.JSONDecodeError:
                self.show_error_message(f"无法解析服务器响应: {data}")
        except Exception as e:
            self.show_error_message(f"处理响应时出现异常: {str(e)}")
    def populate_table(self, students):
        """填充表格数据"""
        try:
            table = self.ui.tableWidget
            table.setRowCount(0)  # 清空表格
            
            for row, student in enumerate(students):
                table.insertRow(row)
                
                # ID列
                id_item = QTableWidgetItem(str(student['ID']))
                id_item.setFlags(id_item.flags() & ~Qt.ItemIsEditable)  # 不可编辑
                table.setItem(row, 0, id_item)
                
                # 姓名列
                table.setItem(row, 1, QTableWidgetItem(student['Name']))
                
                # 积分列
                point_item = QTableWidgetItem(str(student['Point']))
                point_item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row, 2, point_item)
        except Exception as e:
            self.show_error_message(f"填充表格时出错: {str(e)}")
    
    def show_error_message(self, message):
        """显示错误消息"""
        QMessageBox.critical(self, "错误", message)
    
    def show_warning_message(self, message):
        """显示警告消息"""
        QMessageBox.warning(self, "警告", message)
    
    def get_exe_path(self, exe_name):
        """获取可执行文件路径"""
        try:
            if getattr(sys, 'frozen', False):
                base_path = os.path.dirname(sys.executable)
            else:
                base_path = os.path.dirname(__file__)
            
            path = os.path.join(base_path, exe_name)
            if not os.path.exists(path):
                raise FileNotFoundError(f"找不到 {exe_name}")
            return path
        except Exception as e:
            QMessageBox.critical(self, "错误", f"路径获取失败: {str(e)}")
            return None
    
    def creates(self):
        """添加学生"""
        exe_path = self.get_exe_path("createlauncher.exe")
        if exe_path:
            self.run_exe(exe_path)
    
    def modify(self):
        """修改学生信息"""
        exe_path = self.get_exe_path("choice.exe")
        if exe_path:
            self.run_exe(exe_path)
    
    def dele(self):
        """删除学生"""
        exe_path = self.get_exe_path("delete.exe")
        if exe_path:
            self.run_exe(exe_path)
    
    def cs(self):
        """连接服务器"""
        exe_path = self.get_exe_path("connectlauncher.exe")
        if exe_path:
            self.run_exe(exe_path)
    
    def udlog(self):
        """更新日志"""
        exe_path = self.get_exe_path("udloglauncher.exe")
        if exe_path:
            self.run_exe(exe_path)
    
    def ab(self):
        """关于"""
        exe_path = self.get_exe_path("aboutlauncher.exe")
        if exe_path:
            self.run_exe(exe_path)
    
    def run_exe(self, exe_path):
        """运行外部程序"""
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
        """外部程序完成回调"""
        self.setEnabled(True)
        # 外部程序完成后刷新数据
        self.fetch_student_data()
    
    def closeEvent(self, event):
        """窗口关闭事件"""
        self.stop_auto_refresh()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    try:
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # 2秒超时
        result = sock.connect_ex((shared.ip, 8000))
        sock.close()
        if result != 0:
            QMessageBox.critical(None, "连接失败", f"无法连接到服务器 {shared.ip}:8000")
            sys.exit(1)
    except Exception as e:
        QMessageBox.critical(None, "连接错误", f"检查服务器连接时出错: {str(e)}")
        sys.exit(1)
    window = StudentInfoEditor()
    window.show()
    sys.exit(app.exec())
    