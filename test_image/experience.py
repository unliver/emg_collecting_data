import os

class experience():
    def __init__(self):
        self.path = None
        self.label = []
        self.time = 0

    def re_path(self):
        return self.path

    def re_label(self, pos: int):
        return self.label[pos]

    def re_time(self):
        return self.time
