import sys

from cd_item import CdItem
from cd_making_strategy import CdMakingStrategy
from util.tree import Tree


class FirstFitStrategy(CdMakingStrategy):

    def __init__(self):
        super().__init__()
        self.tree = Tree()
        self.cd_number = 0

    def apply_strategy(self, item: CdItem):
        index = self.tree.find(item.get_size())

        if index == sys.maxsize:
            self.add_item(item, self.cd_number)
            self.tree.add(self.cd_number, self.used_cd_list[self.cd_number].remaining_capacity)
            self.cd_number += 1
            return

        cd = self.used_cd_list[index]
        self.tree.delete(cd.index, cd.remaining_capacity)
        cd.add_data(item)
        self.tree.add(cd.index, cd.remaining_capacity)
        self.used_cd_list[cd.index] = cd