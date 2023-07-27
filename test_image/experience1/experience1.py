import os
from test_image.experience import experience

class experience_1(experience):
    def __init__(self):
        super(experience_1,self).__init__()
        self.path = 'D:\python\pythonProject\colect_data\\test_image\experience1\im0.png'
        self.label = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n'
                      'o','p','q','r','s','t','u','v','w','x','y','z']
        self.time = 5

    # def re_path(self):
    #     return self.path
    #
    # def re_label(self, pos: int):
    #     return self.label[pos]
    #
    # def re_time(self):
    #     return self.time
