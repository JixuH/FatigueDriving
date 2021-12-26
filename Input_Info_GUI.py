import os
import shutil

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QVariant
from PyQt5.QtWidgets import QMessageBox

from data.areainfo import dicBorough, dictCity, dictPorovince
from MySQL_Connect import MySQL_Connect


class Ui_Info_Entry(QtWidgets.QMainWindow):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(432, 532)
        Form.setFixedSize(432, 532)

        # 分隔线0
        self.line_0 = QtWidgets.QLabel(Form)
        self.line_0.setGeometry(QtCore.QRect(30, 40, 371, 16))
        self.line_0.setObjectName("line_0")
        # 分隔线1
        self.line_1 = QtWidgets.QLabel(Form)
        self.line_1.setGeometry(QtCore.QRect(30, 210, 371, 16))
        self.line_1.setObjectName("line_1")
        # 分隔线2
        self.line_2 = QtWidgets.QLabel(Form)
        self.line_2.setGeometry(QtCore.QRect(30, 340, 371, 16))
        self.line_2.setObjectName("line_2")
        # 基本信息
        self.essential_information = QtWidgets.QLabel(Form)
        self.essential_information.setGeometry(QtCore.QRect(30, 20, 61, 16))
        self.essential_information.setObjectName("essential_information")
        # 地址信息
        self.address_information = QtWidgets.QLabel(Form)
        self.address_information.setGeometry(QtCore.QRect(30, 190, 54, 12))
        self.address_information.setObjectName("address_information")
        # 车辆信息
        self.vehicle_information = QtWidgets.QLabel(Form)
        self.vehicle_information.setGeometry(QtCore.QRect(30, 320, 54, 12))
        self.vehicle_information.setObjectName("vehicle_information")

        # 省份
        self.label_province = QtWidgets.QLabel(Form)
        self.label_province.setGeometry(QtCore.QRect(40, 230, 51, 21))
        self.label_province.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_province.setObjectName("label_province")
        self.province = QtWidgets.QComboBox(Form)
        self.province.setGeometry(QtCore.QRect(90, 230, 111, 22))
        self.province.setObjectName("province")
        self.province.addItem("")
        # 市/州
        self.label_city = QtWidgets.QLabel(Form)
        self.label_city.setGeometry(QtCore.QRect(230, 230, 51, 21))
        self.label_city.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_city.setObjectName("label_city")
        self.city = QtWidgets.QComboBox(Form)
        self.city.setGeometry(QtCore.QRect(280, 230, 111, 22))
        self.city.setObjectName("city")
        self.city.addItem("")
        # 区/县
        self.label_borough = QtWidgets.QLabel(Form)
        self.label_borough.setGeometry(QtCore.QRect(40, 280, 51, 21))
        self.label_borough.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_borough.setObjectName("label_borough")
        self.borough = QtWidgets.QComboBox(Form)
        self.borough.setGeometry(QtCore.QRect(90, 280, 111, 22))
        self.borough.setObjectName("borough")
        self.borough.addItem("")

        # 编号
        self.number = QtWidgets.QLabel(Form)
        self.number.setGeometry(QtCore.QRect(40, 60, 51, 21))
        self.number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.number.setObjectName("number")
        self.lineEdit_00 = QtWidgets.QLineEdit(Form)
        self.lineEdit_00.setGeometry(QtCore.QRect(90, 60, 111, 20))
        self.lineEdit_00.setText("")
        self.lineEdit_00.setObjectName("lineEdit_00")
        # 姓名
        self.name = QtWidgets.QLabel(Form)
        self.name.setGeometry(QtCore.QRect(230, 60, 51, 21))
        self.name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.name.setObjectName("name")
        self.lineEdit_01 = QtWidgets.QLineEdit(Form)
        self.lineEdit_01.setGeometry(QtCore.QRect(280, 60, 111, 20))
        self.lineEdit_01.setText("")
        self.lineEdit_01.setObjectName("lineEdit_01")
        # 性别
        self.sex = QtWidgets.QLabel(Form)
        self.sex.setGeometry(QtCore.QRect(40, 110, 51, 21))
        self.sex.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.sex.setObjectName("sex")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(90, 110, 111, 20))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        # 年龄
        self.age = QtWidgets.QLabel(Form)
        self.age.setGeometry(QtCore.QRect(230, 110, 51, 21))
        self.age.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.age.setObjectName("age")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(280, 110, 111, 20))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        # 身份证号
        self.id_number = QtWidgets.QLabel(Form)
        self.id_number.setGeometry(QtCore.QRect(30, 150, 61, 21))
        self.id_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.id_number.setObjectName("id_number")
        self.lineEdit_20 = QtWidgets.QLineEdit(Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(90, 150, 111, 20))
        self.lineEdit_20.setText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        # 联系电话
        self.contact_number = QtWidgets.QLabel(Form)
        self.contact_number.setGeometry(QtCore.QRect(220, 150, 61, 21))
        self.contact_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.contact_number.setObjectName("contact_number")
        self.lineEdit_21 = QtWidgets.QLineEdit(Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(280, 150, 111, 20))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setObjectName("lineEdit_21")
        # 车型
        self.model = QtWidgets.QLabel(Form)
        self.model.setGeometry(QtCore.QRect(40, 360, 51, 21))
        self.model.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.model.setObjectName("model")
        self.lineEdit_30 = QtWidgets.QLineEdit(Form)
        self.lineEdit_30.setGeometry(QtCore.QRect(90, 360, 111, 20))
        self.lineEdit_30.setText("")
        self.lineEdit_30.setObjectName("lineEdit_30")
        # 驾驶证编号
        self.driver_license_number = QtWidgets.QLabel(Form)
        self.driver_license_number.setGeometry(QtCore.QRect(200, 360, 81, 21))
        self.driver_license_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.driver_license_number.setObjectName("driver_license_number")
        self.lineEdit_31 = QtWidgets.QLineEdit(Form)
        self.lineEdit_31.setGeometry(QtCore.QRect(280, 360, 111, 20))
        self.lineEdit_31.setText("")
        self.lineEdit_31.setObjectName("lineEdit_31")
        # 车牌号
        self.license_number = QtWidgets.QLabel(Form)
        self.license_number.setGeometry(QtCore.QRect(40, 400, 51, 21))
        self.license_number.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.license_number.setObjectName("license_number")
        self.lineEdit_40 = QtWidgets.QLineEdit(Form)
        self.lineEdit_40.setGeometry(QtCore.QRect(90, 400, 111, 20))
        self.lineEdit_40.setText("")
        self.lineEdit_40.setObjectName("lineEdit_40")
        # 保存
        self.info_entry = QtWidgets.QPushButton(Form)
        self.info_entry.setGeometry(QtCore.QRect(90, 450, 75, 23))
        self.info_entry.setObjectName("info_entry")
        # 取消
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(260, 450, 75, 23))
        self.cancel.setObjectName("cancel")

        # 中心窗口
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 初始化省份数据
        self.province.clear()
        self.province.addItem('请选择')
        for key, value in dictPorovince.items():
            self.province.addItem(value, QVariant(key))

        # 按扭框被点击事件信号
        self.province.activated.connect(self.add_city)
        self.city.activated.connect(self.add_borough)
        self.borough.activated.connect(self.just_btn_enable)
        self.info_entry.clicked.connect(self.save_sql_ok)
        self.cancel.clicked.connect(self.close)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "个人信息登记"))
        # 基本信息
        self.essential_information.setText(_translate("Form", "<html><head/><body><p>基本信息<span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.line_0.setText(_translate("Form", "--------------------------------------------------------------------"))
        self.number.setText(_translate("Form", "编号："))
        self.name.setText(_translate("Form", "姓名："))
        self.sex.setText(_translate("Form", "性别："))
        self.age.setText(_translate("Form", "年龄："))
        self.id_number.setText(_translate("Form", "身份证号："))
        self.contact_number.setText(_translate("Form", "联系电话："))
        # 地址信息
        self.address_information.setText(_translate("Form", "<html><head/><body><p>地址信息<span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.line_1.setText(_translate("Form", "--------------------------------------------------------------------"))
        self.label_province.setText(_translate("Form", "省份："))
        self.province.setItemText(0, _translate("Form", "请选择"))
        self.label_city.setText(_translate("Form", "城市："))
        self.city.setItemText(0, _translate("Form", "请选择"))
        self.label_borough.setText(_translate("Form", "区/县："))
        self.borough.setItemText(0, _translate("Form", "请选择"))
        # 车辆信息
        self.vehicle_information.setText(_translate("Form", "<html><head/><body><p>车辆信息<span style=\" color:#ff0000;\">*</span></p></body></html>"))
        self.line_2.setText(_translate("Form", "--------------------------------------------------------------------"))
        self.model.setText(_translate("Form", "车型："))
        self.driver_license_number.setText(_translate("Form", "行驶证编号："))
        self.license_number.setText(_translate("Form", "车牌号："))
        # 按钮
        self.cancel.setText(_translate("Form", "取消"))
        self.info_entry.setText(_translate("Form", "录入"))

    # 当省份按钮被选择后添加对应的城市数据
    def add_city(self, index):
        pro_code = self.province.itemData(index)
        city_data = dictCity.get(pro_code, dict())
        self.city.clear()
        self.city.addItem('请选择')
        self.borough.clear()
        self.borough.addItem('请选择')
        if self.province.currentText() != '请选择':
            for key, value in city_data.items():
                self.city.addItem(value, QVariant(key))
        self.info_entry.setDisabled(True)
    # 当城市按钮被选择后添加对应的区县数据
    def add_borough(self, index):
        city_code = self.city.itemData(index)
        borough_data = dicBorough.get(city_code, dict())
        self.borough.clear()
        self.borough.addItem('请选择')
        if self.city.currentText() != '请选择':
            for key, value in borough_data.items():
                self.borough.addItem(value, QVariant(key))
        self.info_entry.setDisabled(True)
    # 导出按钮是否可用
    def just_btn_enable(self, txt):
        if self.borough.currentText() != '请选择':
            self.info_entry.setDisabled(False)
        else:
            self.info_entry.setDisabled(True)
    # 清空信息
    def clear(self):
        self.lineEdit_00.clear()
        self.lineEdit_01.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_20.clear()
        self.lineEdit_21.clear()
        self.province.clear()
        self.province.addItem('请选择')
        self.city.clear()
        self.city.addItem('请选择')
        self.borough.clear()
        self.borough.addItem('请选择')
        self.lineEdit_30.clear()
        self.lineEdit_31.clear()
        self.lineEdit_40.clear()
        # 初始化省按钮信息
        for key, value in dictPorovince.items():
            self.province.addItem(value, QVariant(key))
    # 点击保存后，信息确认
    def save_sql_ok(self):
        self.all_info = {}
        self.all_info['编号'] = self.lineEdit_00.text()
        self.all_info['姓名'] = self.lineEdit_01.text()
        self.all_info['性别'] = self.lineEdit_10.text()
        self.all_info['年龄'] = self.lineEdit_11.text()
        self.all_info['身份证号'] = self.lineEdit_20.text()
        self.all_info['联系电话'] = self.lineEdit_21.text()
        self.all_info['省份'] = self.province.currentText()
        self.all_info['城市'] = self.city.currentText()
        self.all_info['区/县'] = self.borough.currentText()
        self.all_info['车型'] = self.lineEdit_30.text()
        self.all_info['行驶证编号'] = self.lineEdit_31.text()
        self.all_info['车牌号'] = self.lineEdit_40.text()
        print(self.all_info)

        self.MySQL_Save = MySQL_Connect()
        self.MySQL_Save.MC_Save_User_Info(list_user_info=self.all_info)
        QMessageBox.information(self,
                                "请确认信息",
                                '''您的编号：{}
姓名：{}
性别：{}
年龄：{}
身份证号：{}
联系电话：{}
省份：{}
城市：{} 
区县：{}
车型：{}
行驶证编号：{}
车牌号：{}'''.format(self.lineEdit_00.text(),
                    self.lineEdit_01.text(),
                    self.lineEdit_10.text(),
                    self.lineEdit_11.text(),
                    self.lineEdit_20.text(),
                    self.lineEdit_21.text(),
                    self.province.currentText(),
                    self.city.currentText(),
                    self.borough.currentText(),
                    self.lineEdit_30.text(),
                    self.lineEdit_31.text(),
                    self.lineEdit_40.text()),
                                QMessageBox.Yes | QMessageBox.No)
        self.clear()

