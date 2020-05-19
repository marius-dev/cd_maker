from random import random

import cd_item


class CD:
    SIZE = 15

    def __init__(self, index):
        self.data = []
        self.capacity = self.SIZE  # default cd capacity
        self.remaining_capacity = self.capacity
        self.index = index

    def add_data(self, item: cd_item.CdItem):
        if self.remaining_capacity < item.get_size():
            raise Exception('CD is full')

        self.remaining_capacity -= item.get_size()
        self.data.append(item)
