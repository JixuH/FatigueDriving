from PyQt5.QtCore import QVariant
from PyQt5 import QtCore, QtGui, QtWidgets

from data.areainfo import dictPorovince, dictCity, dicBorough

from Input_Info_GUI import Ui_Info_Entry
from MySQL_Connect import MySQL_Connect
from EvidenceIm_GUI import Ui_EvidenceIm

# 子窗口 -- 信息录入
class Ui_Info_Entry_Child(Ui_Info_Entry):
    """docstring for Ui_Info_Entry_Child"""
    def __init__(self):
        super(Ui_Info_Entry_Child, self).__init__()
        self.setupUi(self)
# 子窗口 -- 违规信息可视化
class Ui_EvidenceIm_Child(Ui_EvidenceIm):
    """docstring for Ui_EvidenceIm_Child"""

    def __init__(self, impath, oneinfo):
        super(Ui_EvidenceIm_Child, self).__init__(impath,oneinfo)
        self.setupUi(self)
        self.impath = impath
        self.oneinfo = oneinfo
# 主窗口 -- 数据库信息可视化
class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        #self.line = 5
        self.row_num = 1
        self.MainWindow = QtWidgets.QMainWindow()
        self.Info_Entry_Windows = Ui_Info_Entry_Child()
        self.setupUi(self.MainWindow)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1455, 969)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # 省份
        self.server_label_province = QtWidgets.QLabel(self.centralwidget)
        self.server_label_province.setGeometry(QtCore.QRect(0, 10, 51, 21))
        self.server_label_province.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.server_label_province.setObjectName("server_label_province")
        self.server_province = QtWidgets.QComboBox(self.centralwidget)
        self.server_province.setGeometry(QtCore.QRect(60, 10, 111, 22))
        self.server_province.setObjectName("server_province")
        # 市/州
        self.server_label_city = QtWidgets.QLabel(self.centralwidget)
        self.server_label_city.setGeometry(QtCore.QRect(190, 10, 51, 21))
        self.server_label_city.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.server_label_city.setObjectName("server_label_city")
        self.server_city = QtWidgets.QComboBox(self.centralwidget)
        self.server_city.setGeometry(QtCore.QRect(250, 10, 111, 22))
        self.server_city.setObjectName("server_city")
        # 区县
        self.server_label_borough = QtWidgets.QLabel(self.centralwidget)
        self.server_label_borough.setGeometry(QtCore.QRect(380, 10, 51, 21))
        self.server_label_borough.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.server_label_borough.setObjectName("server_label_borough")
        self.server_borough = QtWidgets.QComboBox(self.centralwidget)
        self.server_borough.setGeometry(QtCore.QRect(440, 10, 111, 22))
        self.server_borough.setObjectName("server_borough")
        # 导入
        self.pushButton_import = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_import.setGeometry(QtCore.QRect(590, 10, 111, 23))
        self.pushButton_import.setObjectName("pushButton_import")
        # 更新
        self.pushButton_update = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_update.setGeometry(QtCore.QRect(740, 10, 111, 23))
        self.pushButton_update.setObjectName("pushButton_update")
        # 信息录入
        self.pushButton_info_entry = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_info_entry.setGeometry(QtCore.QRect(1300, 10, 111, 23))
        self.pushButton_info_entry.setObjectName("pushButton_info_entry")
        # 数据表格
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setSelectionBehavior(
        #     QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 1435, 901))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setRowCount(self.row_num)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 初始化省份数据
        self.server_province.clear()
        self.server_province.addItem('请选择')
        for key, value in dictPorovince.items():
            self.server_province.addItem(value, QVariant(key))
        # 按扭框被点击事件信号
        self.server_province.activated.connect(self.add_city)
        self.server_city.activated.connect(self.add_borough)
        self.server_borough.activated.connect(self.just_btn_enable)
        self.pushButton_import.clicked.connect(self.import_ok)
        self.pushButton_update.clicked.connect(self.import_ok)
        self.pushButton_info_entry.clicked.connect(self.show_info_entry_windows)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "疲劳驾驶监测数据终端平台"))
        self.server_label_province.setText(_translate("MainWindow", "省份"))
        self.server_label_city.setText(_translate("MainWindow", "市/州"))
        self.server_label_borough.setText(_translate("MainWindow", "区/县"))
        self.pushButton_import.setText(_translate("MainWindow", "导出"))
        self.pushButton_update.setText(_translate("MainWindow", "刷新"))
        self.pushButton_info_entry.setText(_translate("MainWindow", "信息录入"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "年龄"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "身份证号"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "联系电话"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "省份"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "市/州"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "区/县"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "车型"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "行驶证编号"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "车牌号"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "违规时间"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "操作"))
    # 当省份按钮被选择后添加对应的城市数据
    def add_city(self, index):
        pro_code = self.server_province.itemData(index)
        city_data = dictCity.get(pro_code, dict())
        self.server_city.clear()
        self.server_city.addItem('请选择')
        self.server_borough.clear()
        self.server_borough.addItem('请选择')
        if self.server_province.currentText() != '请选择':
            for key, value in city_data.items():
                self.server_city.addItem(value, QVariant(key))
        self.pushButton_import.setDisabled(True)

    # 当城市按钮被选择后添加对应的区县数据
    def add_borough(self, index):
        city_code = self.server_city.itemData(index)
        borough_data = dicBorough.get(city_code, dict())
        self.server_borough.clear()
        self.server_borough.addItem('请选择')
        if self.server_city.currentText() != '请选择':
            for key, value in borough_data.items():
                self.server_borough.addItem(value, QVariant(key))
        self.pushButton_import.setDisabled(True)

    # 导出按钮是否可用
    def just_btn_enable(self, txt):
        if self.server_borough.currentText() != '请选择':
            self.pushButton_import.setDisabled(False)
        else:
            self.pushButton_import.setDisabled(True)

    # 根据省市县筛选信息导出
    def import_ok(self):
        if self.server_province.currentText() == '请选择':
            QtWidgets.QMessageBox.warning(self, "警告", "请选择省/市/县信息", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        else:
            self.MySQL_Read = MySQL_Connect()
            self.info_all = self.MySQL_Read.MC_Read_Violation_Info()
            # 根据省市县筛选得到的信息存放
            self.info_realdata = []
            # 提取筛选后的各数据对应图片地址
            self.info_realimpath = []
            # 按钮名称
            self.btn_realname = []
            # 遍历提取相应数据
            for i in range(len(self.info_all)):
                if self.info_all[i][6] == self.server_province.currentText() and self.info_all[i][7] == self.server_city.currentText() and self.info_all[i][8] == self.server_borough.currentText():
                    self.info_realdata.append(list(self.info_all[i]))
                    self.info_realimpath.append(str(self.info_all[i][-1]))
                    self.btn_realname.append(str('详情：'+self.info_all[i][1]+' - '+self.info_all[i][-2]))
            self.pushbutton_list()
            for m in range(len(self.info_realdata)):  # m行 n列
                for n in range(14):
                    item = QtWidgets.QTableWidgetItem(str(self.info_realdata[m][n]))
                    self.tableWidget.setItem(m, n, item)

    # 创建详情按钮
    def pushbutton_list(self):
        self.tableWidget.setRowCount(len(self.info_realdata))
        for n in range(len(self.info_realdata)):
            self.btn = QtWidgets.QPushButton()
            self.btn.setDown(True)
            self.btn.setStyleSheet('QPushButton{margin:3px}'
                                   'QPushButton{padding:1px 1px}')
            self.tableWidget.setCellWidget(n, 13, self.btn)
            #此处将字传入按钮
            self.btn.setText(self.btn_realname[n])
            #传达参数，这里sender将接收你点击的字并传入函数
            self.btn.clicked.connect(
                lambda: self.btn_clicked(self.btn_realname.index(self.sender().text())))

    # 显示子页面 -- 信息录入
    def show_info_entry_windows(self):
        self.Info_Entry_Windows.show()

    # 显示子页面 -- 证据图像
    def btn_clicked(self,n):
        #self.nn = list.index(self.line[self.n])
        self.impath = self.info_realimpath[n]
        self.oneinfo = self.btn_realname[n]
        self.EvidenceIm_Windows = Ui_EvidenceIm_Child(
            self.impath, self.oneinfo)
        self.EvidenceIm_Windows.show()

# 重写QtWidgets.QMainWindow类关闭事件
class MainWindow(QtWidgets.QMainWindow):
    def closeEvent(self, event):  # 关闭窗口触发以下事件
        reply = QtWidgets.QMessageBox.question(
            self, '本程序', '你确定要退出吗?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()  # 接受关闭事件
        else:
            event.ignore()  # 忽略关闭事件
