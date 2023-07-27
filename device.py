import socket
import numpy as np
import os
import threading
from config import *

MAX_BYTES = 65535

class jidian_device(QObject):

    trigger = pyqtSignal()
    global n_pre

    def __init__(self, ip: str, port_server: int, port_client: int, num: int, out_path: str):
        super(jidian_device,self).__init__()
        self.port_server = port_server    #监听端口
        self.port_client = port_client  #服务器端口
        self.ip = ip    #监听ip
        self.socket = None
        self.flag = False   #接收状态
        self.text = []    #接收到的初始数据
        self.n_pre = num
        self.pos = 0    #标志读取text位置
        self.end = 0
        self.pos_d = 0  # 标志读取text位置
        self.end_d = 0
        self.pos_l = 0  #标志读取划分后列表位置
        self.end_l = 0
        self.out_info = []
        self.out_info_d = []
        self.down_f = 500
        self.lock = threading.Lock()    #对num访问
        self.Fs = 8
        self.direct_num = 500
        self.num = self.n_pre*self.Fs
        print(out_path)
        if os.path.exists(out_path) == False:
            print(out_path)
            os.makedirs(out_path)
            print(out_path)
        print(out_path)
        self.out_path_pre = out_path
        print(self.out_path_pre)

    # 建立socket
    def build_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port_server))
        print('Listening at {}'.format(self.socket.getsockname()))
        self.collect_data()

    # 接收udp信息
    def collect_data(self):
        if self.flag == True:
            start = 'S'
            start = start.encode("ascii")
            address = (self.ip, self.port_client)
            self.socket.sendto(start, address)
        self.text = []
        self.num = self.n_pre*self.Fs
        self.out_info = []
        self.out_info_d = []
        # print(self.num)
        self.end_l = 0
        self.direct_num = 500
        while True:

            if self.num == 0:
                self.stop_collect()
                break
            else:
                data,address = self.socket.recvfrom(MAX_BYTES)
                text = data.decode('ascii')
                print('The client at {} says {!r}'.format(address, text))
                self.text.append(text)
                self.end = len(self.text)
                self.end_d = len(self.text)
            self.lock.acquire()
            self.num -= 1
            self.lock.release()
        # print(self.end)
        if self.text != None:
            self.direct = self.data_load()
            self.trigger.emit()

    def stop_collect(self):
        # print("0")
        terminal = 'T'
        terminal = terminal.encode("ascii")
        address = (self.ip, self.port_client)
        self.socket.sendto(terminal, address)
        self.socket.close()

    # 数据处理存储
    def data_load(self):
        print("data load")
        out_info = []
        self.out_path = self.out_path_pre + '\\' + '{}{}'.format(self.label, '.txt')
        print(self.out_path)
        for epoch in self.text:
            lines = epoch.split('\t\r\n')
            lines.pop()
            for line in lines:
                line_np = line.split('\t')
                # line_np.append(self.label)
                line_np_change = [float(element) for element in line_np]
                line_np_change.append(self.label)
                out_info.append(line_np_change)
                # print(line_np)
        np.savetxt(self.out_path, out_info, fmt="%s")
        return np.array(out_info)

    # 修改标签
    def change_label(self, label):
        self.label = label

    def support_data(self):
        if self.pos != self.end:
            # print(self.pos)
            # print(self.end)
            for epoch in self.text[self.pos:self.end]:
                lines = epoch.split('\t\r\n')
                lines.pop()
                for line in lines:
                    line_np = line.split('\t')
                    self.out_info.append(line_np)
                    # print(line_np)
        self.pos = self.end
        # print(len(self.out_info))

        if len(self.out_info) == 0:
            # print(np.array(['0','0','0','0','0','0','0','0']))
            return np.array([0,0,0,0,0,0,0,0]),False
        else:
            self.pos_l = self.end_l
            self.end_l = len(self.out_info)
            print(self.end_l)
            # print(self.pos)
            # print(self.end_l)
            # print(self.end)
            self.lock.acquire()
            if self.pos_l != self.end_l:
                # self.end = len(self.out_info)
                # float_lst = [float(item) for item in lst]
                # print(self.out_info[self.end-1])
                # print(self.pos_l)
                # print(self.end_l)
                out_info = [[float(element) for element in sublist] for sublist in self.out_info[0:self.end_l]]

                # print(self.pos_l)
                # print(self.end_l)
                # # print(len(out_info))
                # # print(self.num)
                # print(len(self.out_info))
                self.lock.release()
                # self.down_f += 500
                print(len(out_info))
                return np.array(out_info),True

            elif self.num != 0:
                # print(self.num)
                self.lock.release()
                return [],False
            else:
                # print(self.num)
                self.lock.release()
                return [],True

    def support_direct(self):
        # if self.pos_d != self.end_d:
        #     # print(self.pos)
        #     # print(self.end)
        #     for epoch in self.text[self.pos_d:self.end_d]:
        #         lines = epoch.split('\t\r\n')
        #         lines.pop()
        #         for line in lines:
        #             line_np = line.split('\t')
        #             self.out_info_d.append(line_np)
        #             # print(line_np)
        # self.pos_d = self.end_d
        # if len(self.out_info_d) > self.direct_num:
        #     out_info = [[float(element) for element in sublist]
        #                 for sublist in self.out_info_d[self.direct_num-500:self.direct_num]]
        #     self.direct_num += 500
        #     return np.array(out_info),True
        # elif self.num == 0:
        #     return [],True
        # else:
        #     return [],False
        if self.end_l > 100:
            return np.array(self.out_info[self.end_l-100:])
        else:
            return []




