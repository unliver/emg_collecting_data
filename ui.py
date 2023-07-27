# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import numpy as np

from threading import Thread
import concurrent.futures

import matplotlib as plt
from PyQt5.QtGui import QFont

plt.use('agg')

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure

from scipy.fftpack import fft

import time
from config import *
from PyQt5 import QtCore, QtGui, QtWidgets
from device import jidian_device
from clock import clock
from show_image import ImageBox
from direct_img import direct_img
import os
from multiprocessing import Process
from test_image.experience1.experience1 import experience_1
from test_image.experience2.experience2 import experience_2
from test_image.experience3.experience3 import experience_3
from test_image.experience4.experience4 import experience_4

class Ui_Form(QWidget):

    switch = pyqtSignal()
    direct = pyqtSignal()

    def __init__(self, imform):

        super(Ui_Form, self).__init__()

        self.imformation = imform     #主界面传的信息
        print(self.imformation)

        if self.imformation[0] == "experience_1":
            self.experience = experience_1()
        elif self.imformation[0] == "experience_2":
            self.experience = experience_2()
        elif self.imformation[0] == "experience_3":
            self.experience = experience_3()
        elif self.imformation[0] == "experience_4":
            self.experience = experience_4()
        self.clock = clock(self.experience.re_time())
        # self.clock.trigger.connect(self.countTime)
        self.path, self.name = os.path.split(self.experience.re_path())   #展示图片路径
        self.position = -1   #图片次序
        self.out_path = 'D:\python\pythonProject\colect_data\data' + '\\' + self.imformation[1] + '\\' +self.imformation[0]
        print(self.out_path)
        self.mydevice = jidian_device('127.0.0.1', 2100, 2101, self.experience.re_time(), self.out_path)
        # self.mydevice = jidian_device('127.0.0.1', 2100, 2101, 50, self.out_path)
        print(self.out_path)

        # self.mydevice.trigger.connect(self.estimate)
        # self.clock.trigger.connect(self.estimate)
        self.direct.connect(self.estimate)

        self.setupUi()

    def setupUi(self):

        self.setWindowTitle("jidian")
        self.setFixedSize(1400, 920)

        font = QFont()
        # 设置字体的点大小
        font.setPointSize(10)

        self.pushButton = QPushButton("begin collecting")
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.start_collect)
        self.pushButton.setFixedSize(200, 80)

        # layout = QHBoxLayout()
        # layout.addWidget(self.pushButton)
        # self.setLayout(layout)
        print(self.experience.re_path())
        self.image = ImageBox(self.experience.re_path())
        # self.image.resize(400,400)
        print('a')

        self.pushButton_2 = QPushButton("begin experience")
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(self.next_terminate_collect)
        self.pushButton_2.setFixedSize(200, 80)

        layoutV = QVBoxLayout()

        wh = QWidget(self)
        layout = QHBoxLayout()

        # layout.addWidget(self.clock)
        # layout.addWidget(self.pushButton)

        w = QWidget(self)
        layout2 = QVBoxLayout()
        layout2.addWidget(self.image)
        # self.true_path = self.path + '\\' + self.name.replace('0', str(self.position))
        # self.image.set_image(self.true_path)
        layout2.addWidget(self.pushButton_2)
        layout2.setAlignment(Qt.AlignCenter)
        w.setLayout(layout2)

        layout.addWidget(w)

        dynamic_canvas = FigureCanvas(Figure(figsize=(8,4)))
        layout.addWidget(dynamic_canvas)
        self.x = []  # 建立空的x轴数组和y轴数组
        self.y = []
        self.n = 0
        self._dynamic_ax = dynamic_canvas.figure.subplots()


        # self.clock.timer.timeout.connect(self._update_canvas)

        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)
        wh.setLayout(layout)

        layoutV.addWidget(wh)

        wh2 = QWidget(self)
        layout2 = QHBoxLayout()

        self.direct_img1 = direct_img(1)
        self.direct_img2 = direct_img(2)

        w_clock = QWidget(self)
        layout_clock = QVBoxLayout()
        layout_clock.addWidget(self.clock)
        layout_clock.addWidget(self.pushButton)
        w_clock.setLayout(layout_clock)

        layout2.addWidget(w_clock)
        layout2.addWidget(self.direct_img1)
        layout2.addWidget(self.direct_img2)
        layout2.setAlignment(Qt.AlignHCenter)

        wh2.setLayout(layout2)

        layoutV.addWidget(wh2)

        self.setLayout(layoutV)

        # self.true_path = self.path+'\\'+self.name.replace('0',str(self.position))
        # self.image.set_image(self.true_path)

        self.mydevice.change_label(self.experience.re_label(self.position))
        self.direct_img1.setBackground()
        self.direct_img2.setBackground()

    def _update_canvas(self):
        # self._dynamic_ax.clear()
        self.n = 0
        self.x = []
        self.y = []
        self.mydevice.pos = 0
        self.mydevice.end_l = 0
        self.mydevice.pos_l = 0
        self.mydevice.out_info = []
        print('update')
        while True:


            out_info,flag = self.mydevice.support_data()
            if flag == True:
                if len(out_info) == 0:
                    break
                # print(out_info)

                self._dynamic_ax.clear()
                print('aaa')

                # lines = self._dynamic_ax.get_lines()  # 获取当前轴上的所有线
                # for line in lines:
                #     line.set_data([], [])  # 清空线的数据

                t = 1/(self.mydevice.Fs*100)
                # print("cleared")
                if isinstance(out_info, np.ndarray) and out_info.ndim == 1:
                    # out_info 是一个一维数组
                    self.n += 1
                    self.x.append(self.n * t)  # x加入一个值
                else:
                    # out_info 不是一个一维数组
                    for line in out_info[self.mydevice.end_l-100:]:
                        self.n += 1
                        self.x.append(self.n * t)  # x加入一个值

                xx = np.array(self.x)

                if isinstance(out_info, np.ndarray) and out_info.ndim == 1:
                    # out_info 是一个一维数组
                    for item in out_info:
                        self._dynamic_ax.plot(xx, item)

                    print("out_info 是一个一维数组")
                else:
                    # out_info 不是一个一维数组
                    for item in range(out_info.shape[1]):
                        self._dynamic_ax.plot(xx, out_info[:,item]+500+(7-item)*1000)

                # if isinstance(out_info, np.ndarray) and out_info.ndim == 1:
                #     # out_info 是一个一维数组
                #     for item, line in zip(out_info, lines):
                #         line.set_data(xx, item)
                # else:
                #     # out_info 不是一个一维数组
                #     for item, line in zip(range(out_info.shape[1]), lines):
                #         line.set_data(xx, out_info[:, item] + 500 + (7 - item) * 1000)

                self._dynamic_ax.set_xlim(int(self.n//(self.mydevice.Fs*100)), int(self.n//(self.mydevice.Fs*100))+1)
                self._dynamic_ax.set_ylim(0,8000)
                y_ticks = [500,1500,2500,3500,4500,5500,6500,7500]
                y_tick_labels = ['emg8','emg7','emg6','emg5','emg4','emg3','emg2','emg1']
                self._dynamic_ax.set_yticks(y_ticks)
                self._dynamic_ax.set_yticklabels(y_tick_labels)
                self._dynamic_ax.figure.canvas.draw()
                self.direct.emit()
                # plt.show()


                # print(self.x[0])
                # print(self.x[-1])

    # def countTime(self):
    #     self.clock.time -= 1
    #     # LED显示数字+1
    #     self.clock.lcdNumber.display(self.clock.time)
    #     print(self.clock.time)
    #     if self.clock.time == 0:
    #         self.clock.timer.stop()
    #         self.clock.time = self.clock.t
    #         # self.clock.trigger.emit()
    #         print("end")



    def start_collect(self):
        l = []
        self.mydevice.num = self.mydevice.n_pre * self.mydevice.Fs
        self.mydevice.out_info = []
        self.mydevice.out_info_d = []
        # print(self.num)
        self.mydevice.end_l = 0
        self.mydevice.direct_num = 500
        self.mydevice.flag = True
        self.mydevice.down_f = 500
        self.direct_img1.reset_color()
        self.direct_img2.reset_color()
        # self._dynamic_ax.clear()
        # self._dynamic_ax.figure.canvas.draw()
        print("start")
        # thread_clock = Thread(target=self.clock.work)
        # thread_clock.start()
        # l.append(thread_clock)
        self.clock.work()
        # thread_show = Thread(target=self.image.play)
        # thread_show.start()
        # l.append(thread_show)
        self.image.play()
        thread_device = Thread(target=self.mydevice.build_socket)
        thread_device.start()
        l.append(thread_device)
        # thread_direct = Thread(target=self.estimate)
        # thread_direct.start()
        # l.append(thread_direct)
        thread_plot = Thread(target=self._update_canvas)
        thread_plot.start()
        l.append(thread_plot)


        # #创建线程池
        # executor = concurrent.futures.ThreadPoolExecutor()
        #
        # # 提交绘图任务到线程池
        # future = executor.submit(self._update_canvas)

        # 获取绘图结果（可选）
        # result = future.result()

    def next_terminate_collect(self):
        if self.position == -1:
            self.pushButton_2.setText("next paradigm")
        if self.pushButton_2.text() == "finished":
            self.switch.emit()
        else:
            self.position += 1
            self.true_path = self.path + '\\' + self.name.replace('0', str(self.position))
            if os.path.exists(self.true_path):
                self.image.changeGIF(self.true_path)
                print('draw')
                self.direct_img1.reset_color()
                self.direct_img2.reset_color()
                self.mydevice.change_label(self.experience.re_label(self.position))
            else:
                self.pushButton_2.setText("finished")

    def FFT(self, Fs, data):
        """
        对输入信号进行FFT
        :param Fs:  采样频率
        :param data:待FFT的序列
        :return:
        """
        L = len(data)  # 信号长度
        N = np.power(2, np.ceil(np.log2(L)))  # 下一个最近二次幂，也即N个点的FFT
        # print(N)
        result = np.abs(fft(x=data, n=int(N))) / L * 2  # N点FFT
        axisFreq = np.arange(int(N / 2)) * Fs / N  # 频率坐标
        result = result[range(int(N / 2))]  # 因为图形对称，所以取一半
        return result

    def sum_power(self, data, N):
        # print(data)
        condition = np.logical_and(data > 5, data < 120)
        arr_con = data[condition]
        # print(arr_con)
        dx = 1 / N
        result = np.sum(dx * arr_con)
        return result

    # def estimate(self):
    #     print('estimate')
    #     while True:
    #         direct_info, flag = self.mydevice.support_direct()
    #         # print(len(direct_info))
    #         if flag == False:
    #             continue
    #         elif len(direct_info) == 0:
    #             print("break")
    #             break
    #         # print(len(direct_info))
    #         self.estimate_result = []
    #         for i in range(8):
    #             data = self.FFT(500, direct_info[:,i])
    #             self.estimate_result.append(self.sum_power(data, len(data)))
    #
    #         self.direct_img1.change_color(1,self.estimate_result[0]/0.35)
    #         self.direct_img1.change_color(2,self.estimate_result[1]/2.5)
    #         self.direct_img1.change_color(3,self.estimate_result[2]/0.25)
    #         self.direct_img1.change_color(4,self.estimate_result[3]/0.05)
    #
    #         self.direct_img2.change_color(1,self.estimate_result[4]/0.05)
    #         self.direct_img2.change_color(2,self.estimate_result[5]/0.005)
    #         self.direct_img2.change_color(3,self.estimate_result[6]/0.75)
    #         self.direct_img2.change_color(4,self.estimate_result[7]/1.5)

    def estimate(self):
        print('estimate')
        direct_info = self.mydevice.support_direct()
        if len(direct_info) > 0:
            # print(len(direct_info))

            # print(len(direct_info))
            self.estimate_result = []
            for i in range(8):
                data = self.FFT(500, direct_info[:, i])
                self.estimate_result.append(self.sum_power(data, len(data)))

            self.direct_img1.change_color(1, self.estimate_result[0] / 0.35)
            self.direct_img1.change_color(2, self.estimate_result[1] / 2.5)
            self.direct_img1.change_color(3, self.estimate_result[2] / 0.25)
            self.direct_img1.change_color(4, self.estimate_result[3] / 0.05)

            self.direct_img2.change_color(1, self.estimate_result[4] / 0.05)
            self.direct_img2.change_color(2, self.estimate_result[5] / 0.005)
            self.direct_img2.change_color(3, self.estimate_result[6] / 0.75)
            self.direct_img2.change_color(4, self.estimate_result[7] / 1.5)




        # if self.mydevice.direct.shape != ():
        #     self.estimate_result = []
        #     print('aaaa')
        #     for i in range(8):
        #         data = self.FFT(500, self.mydevice.support_direct())
        #         self.estimate_result.append(self.sum_power(data, len(data)))
        #     # print(self.estimate_result)
        #     if self.estimate_result[0] < 0.7:
        #         self.direct_img1.change_color(1)
        #     if self.estimate_result[1] < 5:
        #         self.direct_img1.change_color(2)
        #     if self.estimate_result[2] < 0.5:
        #         self.direct_img1.change_color(3)
        #     if self.estimate_result[3] < 0.1:
        #         self.direct_img1.change_color(4)
        #
        #     if self.estimate_result[0] < 0.1:
        #         self.direct_img2.change_color(1)
        #     if self.estimate_result[1] < 0.01:
        #         self.direct_img2.change_color(2)
        #     if self.estimate_result[2] < 1.5:
        #         self.direct_img2.change_color(3)
        #     if self.estimate_result[3] < 0.7:
        #         self.direct_img2.change_color(4)



