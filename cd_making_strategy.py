from abc import ABCMeta, abstractmethod
from typing import List

from cd import CD
from cd_item import CdItem


class CdMakingStrategy:
    __metaclass__ = ABCMeta

    cd_capacity: float
    used_cd_list: List[CD]
    unused_cd_capacity: float

    def __init__(self):
        self.cd_capacity = CD.SIZE
        self.used_cd_list = []
        self.unused_cd_capacity = 0

    def add_item(self, cd_item: CdItem, cd_index):
        if cd_index < 0 or cd_index >= len(self.used_cd_list):
            cd_index = len(self.used_cd_list)
            self.used_cd_list.append(CD(cd_index))

        self.used_cd_list[cd_index].add_data(cd_item)

    def total_capacity(self):
        total = 0
        for cd in self.used_cd_list:
            total += cd.capacity
        return total

    def make(self, items: List[CdItem]):
        for item in items:
            self.apply_strategy(item)

        self.unused_cd_capacity = 0
        for used_cd in self.used_cd_list:
            self.unused_cd_capacity += used_cd.remaining_capacity

    @abstractmethod
    def apply_strategy(self, item: CdItem):
        raise NotImplementedError
