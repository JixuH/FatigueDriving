import pymysql as sql
from PyQt5.QtWidgets import QMessageBox

class MySQL_Connect():
    def __init__(self):
        self.write_jud_user_info = 1
        self.write_user_info = "insert into `user_info` values("
        self.write_jud_violation_info = 1
        self.write_violation_info = "insert into `violation_info` values("

        # 加载数据库
        try:
            # 创建服务器连接对象(服务端的IP)
            self._con = sql.Connect(
                host="localhost",
                user="root",
                password="123456",
                database="fatiguedriving",
                port=3306,
                charset='utf8'
                )
        except Exception as e:
            print("ERROR: " + e)
            self._con.close()
            #pass

    # 编号判断
    def MC_Number_Judge(self, number):
        if len(number) != 12:
            return False
        else:
            return True

    # 性别判断
    def MC_Sex_Judge(self, sex):
        if sex != '男' and sex != '女':
            return False
        else:
            return True

    # 身份证判断
    def MC_Id_Card_Judge(self, id):
        if len(id) != 18:
            return False
        else:
            return True

    # 电话号判断
    def MC_Phone_Judge(self, tel):
        if len(tel) != 11:
            return False
        else:
            return True

    # 行驶证编号判断
    def MC_Driver_Licenise_Number_Judge(self, num):
        if len(num) != 12:
            return False
        else:
            return True

    # 车牌号判断
    def MC_Licenise_Number_Judge(self, num):
        if len(num) != 7:
            return False
        else:
            return True


    '''----------------------- 用户信息 -----------------------'''
    # 写入用户信息
    def MC_Save_User_Info(self, list_user_info):
        self.list_user_info = list_user_info
        cursor = self._con.cursor()

        if self.MC_Number_Judge(self.list_user_info['编号']):
            self.MC_Insert_User_Info(self.list_user_info['编号'])
        self.MC_Insert_User_Info(self.list_user_info['姓名'])
        if self.MC_Sex_Judge(self.list_user_info['性别']):
            self.MC_Insert_User_Info(self.list_user_info['性别'])
        self.MC_Insert_User_Info(self.list_user_info['年龄'])
        if self.MC_Id_Card_Judge(self.list_user_info['身份证号']):
            self.MC_Insert_User_Info(self.list_user_info['身份证号'])
        if self.MC_Phone_Judge(self.list_user_info['联系电话']):
            self.MC_Insert_User_Info(self.list_user_info['联系电话'])
        self.MC_Insert_User_Info(self.list_user_info['省份'])
        self.MC_Insert_User_Info(self.list_user_info['城市'])
        self.MC_Insert_User_Info(self.list_user_info['区/县'])
        self.MC_Insert_User_Info(self.list_user_info['车型'])
        if self.MC_Driver_Licenise_Number_Judge(self.list_user_info['行驶证编号']):
            self.MC_Insert_User_Info(self.list_user_info['行驶证编号'])
        if self.MC_Licenise_Number_Judge(self.list_user_info['车牌号']):
            self.MC_Insert_User_Info(self.list_user_info['车牌号'])

        self.write_user_info += ")"
        print(self.write_user_info)
        cursor.execute(self.write_user_info)
        self._con.commit()
        cursor.close()
        self.list_user_info.clear()

    # 读取数据库信息
    def MC_Read_User_Info(self):
        try:
            # 创建游标对象
            cursor = self._con.cursor()

            sql = 'SELECT * FROM `user_info`'
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print("ERROR: " + e)
            self._con.rollback()
            cursor.close()

        return result

    # 数据库语言 数据插入
    def MC_Insert_User_Info(self, new):
        if self.write_jud_user_info != 1:
            self.write_user_info += ", "
        self.write_user_info += "'" + new + "'"
        self.write_jud_user_info += 1
    
    # 根据单个变量查询
    def MC_SELECT_User_Info(self, local_info):
        #self.local_info = '434343434343'
        self.local_info = local_info
        try:
            # 创建游标对象
            cursor = self._con.cursor()

            sql = "SELECT * FROM `user_info` WHERE number=%s" % self.local_info
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print("ERROR: " + e)
            self._con.rollback()
            cursor.close()

        return result

    '''----------------------- 违规记录 -----------------------'''
    # 写入违规记录
    def MC_Save_Violation_Info(self, list_violation_info):
        self.list_violation_info = list_violation_info
        cursor = self._con.cursor()

        if self.MC_Number_Judge(self.list_violation_info['编号']):
            self.MC_Insert_Violation_Info(self.list_violation_info['编号'])
        self.MC_Insert_Violation_Info(self.list_violation_info['姓名'])
        if self.MC_Sex_Judge(self.list_violation_info['性别']):
            self.MC_Insert_Violation_Info(self.list_violation_info['性别'])
        self.MC_Insert_Violation_Info(self.list_violation_info['年龄'])
        if self.MC_Id_Card_Judge(self.list_violation_info['身份证号']):
            self.MC_Insert_Violation_Info(self.list_violation_info['身份证号'])
        if self.MC_Phone_Judge(self.list_violation_info['联系电话']):
            self.MC_Insert_Violation_Info(self.list_violation_info['联系电话'])
        self.MC_Insert_Violation_Info(self.list_violation_info['省份'])
        self.MC_Insert_Violation_Info(self.list_violation_info['城市'])
        self.MC_Insert_Violation_Info(self.list_violation_info['区/县'])
        self.MC_Insert_Violation_Info(self.list_violation_info['车型'])
        if self.MC_Driver_Licenise_Number_Judge(self.list_violation_info['行驶证编号']):
            self.MC_Insert_Violation_Info(self.list_violation_info['行驶证编号'])
        if self.MC_Licenise_Number_Judge(self.list_violation_info['车牌号']):
            self.MC_Insert_Violation_Info(self.list_violation_info['车牌号'])
        self.MC_Insert_Violation_Info(self.list_violation_info['违规时间'])
        self.MC_Insert_Violation_Info(self.list_violation_info['违规证据图像位置'])

        self.write_violation_info += ")"
        print(self.write_violation_info)
        cursor.execute(self.write_violation_info)
        self._con.commit()
        cursor.close()
        self.list_violation_info.clear()

    # 读取数据库信息
    def MC_Read_Violation_Info(self):
        try:
            # 创建游标对象
            cursor = self._con.cursor()

            sql = 'SELECT * FROM `violation_info`'
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
        except Exception as e:
            print("ERROR: " + e)
            self._con.rollback()
            cursor.close()

        return result

    # 数据库语言 信息插入
    def MC_Insert_Violation_Info(self, new):
        if self.write_jud_violation_info != 1:
            self.write_violation_info += ", "
        self.write_violation_info += "'" + new + "'"
        self.write_jud_violation_info += 1
