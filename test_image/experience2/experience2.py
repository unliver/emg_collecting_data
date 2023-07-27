import os
from test_image.experience import experience

class experience_2(experience):
    def __init__(self):
        super(experience_2,self).__init__()
        self.path = 'D:\python\pythonProject\colect_data\\test_image\experience2\im0.png'
        self.label = ['up','down','fist']
        self.time = 5

    # def re_path(self):
    #     return self.path
    #
    # def re_label(self, pos: int):
    #     return self.label[pos]
    #
    # def re_time(self):
    #     return self.time
