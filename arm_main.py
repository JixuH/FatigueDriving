import os
import _thread
import sys
import time
import threading
import cv2
import numpy as np
import pygame
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from watchdog.events import *
from watchdog.observers import Observer
from MySQL_Connect import MySQL_Connect

# 执行预测-raspi端
def run_detection_raspi(sh_name):
    subprocess.run(sh_name, shell=True)


# 转换为可存储到数据库的格式
def save_received_info(user_info, iolations_time, new_filename):
    user_all_info = {}
    user_all_info['编号'] = user_info[0]
    user_all_info['姓名'] = user_info[1]
    user_all_info['性别'] = user_info[2]
    user_all_info['年龄'] = user_info[3]
    user_all_info['身份证号'] = user_info[4]
    user_all_info['联系电话'] = user_info[5]
    user_all_info['省份'] = user_info[6]
    user_all_info['城市'] = user_info[7]
    user_all_info['区/县'] = user_info[8]
    user_all_info['车型'] = user_info[9]
    user_all_info['行驶证编号'] = user_info[10]
    user_all_info['车牌号'] = user_info[11]
    user_all_info['违规时间'] = iolations_time
    user_all_info['违规证据图像位置'] = new_filename
    print(user_all_info)
    return user_all_info

# 信息记录至SQL
def ToSQL(a, module_name):
    # 初始化SQL
    MySQL = MySQL_Connect()
    # 拉取用户数据
    number = module_name[1:13]
    iolations_time = module_name[13:17]+'-'+module_name[17:19] + \
        '-'+module_name[19:21]+' '+module_name[21:23]+':'+module_name[23:25]
    user_info = MySQL.MC_SELECT_User_Info(local_info=number)[0]
    # 生成数据列表
    user_list_violation_info = save_received_info(
        user_info, iolations_time, a)

    MySQL.MC_Save_Violation_Info(user_list_violation_info)

# 播放警示音频
class Play_Audio():
    def __init__(self, audio):
        self.audio = audio

    def run(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.audio)  # './audio/warning.mp3'
        pygame.mixer.music.play()
        time.sleep(3)
        pygame.mixer.music.stop()

class MyDirEventHandler(FileSystemEventHandler):

    def __init__(self):
        FileSystemEventHandler.__init__(self)
        self.audio = './audio/warning.mp3'
        self.warning = Play_Audio(self.audio)

    def on_created(self, event):

        print("file created:{0}".format(event.src_path))
        a = str(event.src_path)
        #
        self.warning.run(self.audio)

        directory, module_name = os.path.split(a)
        module_name = os.path.splitext(module_name)[0]

        ToSQL(a, module_name)


# 监控文件的变化
def run_scan_file(file_name):
    # 创建观察者对象
    observer = Observer()
    # 创建事件处理对象
    fileHandler = MyDirEventHandler()
    # 为观察者设置观察对象与处理事件对象
    observer.schedule(
        fileHandler, file_name, True)
    observer.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

"""
多线程
run_detection 执行预测程序
run_scan_file 监控文件的变化
"""
if __name__ == '__main__':
    try:
        # 识别线程
        command='./real_time.sh'
        getDetect = threading.Thread(target=run_detection_raspi, args=(command, ))
        getDetect.start()
        # 警示线程
        file_name="C:/project/FatigueDriving/screenshots"
        getWarning = threading.Thread(target=run_scan_file, args=(file_name, ))
        getWarning.start()
    except Exception as e:
        print("多线程异常，异常信息：{}".format(e))