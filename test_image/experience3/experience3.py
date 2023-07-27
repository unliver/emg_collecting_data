import os
from test_image.experience import experience

class experience_3(experience):
    def __init__(self):
        super(experience_3,self).__init__()
        self.path = 'D:\python\pythonProject\colect_data\\test_image\experience3\\0.gif'
        self.label = ['0','1','2','3','4','5','6','7','8','9']
        self.time = 5

    # def re_path(self):
    #     return self.path
    #
    # def re_label(self, pos: int):
    #     return self.label[pos]
    #
    # def re_time(self):
    #     return self.time
