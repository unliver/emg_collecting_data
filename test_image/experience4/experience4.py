import os
from test_image.experience import experience

class experience_4(experience):
    def __init__(self):
        super(experience_4,self).__init__()
        self.path = 'D:\python\pythonProject\colect_data\\test_image\experience4\im0.png'
        self.label = ['a','b','c','d','e']
        self.time = 10

    # def re_path(self):
    #     return self.path
    #
    # def re_label(self, pos: int):
    #     return self.label[pos]
    #
    # def re_time(self):
    #     return self.time
