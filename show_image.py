# from config import *
#
# class ImageBox(QWidget):
#
#     clicked = pyqtSignal()
#
#     def __init__(self):
#         super(ImageBox, self).__init__()
#
#         self.setMinimumSize(200,200)
#         self.img = None
#         self.scaled_img = None
#         self.start_point = QPoint(0,10)
#         self.scale = 1
#
#     def init_ui(self):
#         self.setWindowTitle("ImageBox")
#
#     def set_image(self, img_path):
#         """
#         open image file
#         :param img_path: image file path
#         :return:
#         """
#         print(img_path)
#         self.img = QPixmap(img_path)
#         self.scaled_img = self.img.scaled(self.size())
#
#     def paintEvent(self, e):
#         """
#         receive paint events
#         :param e: QPaintEvent
#         :return:
#         """
#         if self.scaled_img:
#             # print('draw')
#             painter = QPainter()
#             painter.begin(self)
#             painter.scale(self.scale, self.scale)
#             painter.drawPixmap(self.start_point, self.scaled_img)
#             painter.end()
#
import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QMovie
from config import *


class ImageBox(QLabel):
    def __init__(self,path):
        super().__init__()

        self.setMinimumSize(360,360)
        self.setMaximumSize(360,360)

        # 创建 QMovie 对象并加载 GIF 文件
        self.movie = QMovie(path)

        # 设置 QMovie 对象循环播放
        # self.movie.setLoopCount(-1)
        # self.movie.loopCount(-1)

        # 将 QMovie 对象设置为标签的动画
        self.setMovie(self.movie)

        # 开始播放 GIF
        # self.movie.start()

    def changeGIF(self, gif_file):
        # 停止当前的动画
        self.movie.stop()

        # 设置新的 GIF 文件路径
        self.movie.setFileName(gif_file)

        # 开始播放新的 GIF
        self.movie.start()

    def play(self):
        print('show')
        self.movie.stop()
        self.movie.start()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     # 创建 GIFViewer 实例并传入 GIF 文件路径
#     gif_viewer = GIFViewer("C:\\Users\\42523\Desktop\绘制\\1.gif")
#
#     gif_viewer.show()
#     sys.exit(app.exec_())

