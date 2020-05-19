import sys

from cd import CD
from cd_item import CdItem
from startegy.cd_making_strategy import CdMakingStrategy


class BestFitStrategy(CdMakingStrategy):

    def get_name(self):
        return "best_fit"

    def __init__(self):
        super().__init__()

    def apply_strategy(self, item: CdItem):

        best_cd_index = 0
        min_cd_space = sys.maxsize

        for index, used_cd in enumerate(self.used_cd_list):
            if used_cd.remaining_capacity >= item.get_size() and used_cd.remaining_capacity - item.get_size() < min_cd_space:
                best_cd_index = index
                min_cd_space = used_cd.remaining_capacity - item.get_size()

        if min_cd_space == sys.maxsize:
            new_cd = CD(len(self.used_cd_list))
            new_cd.add_data(item)
            self.used_cd_list.append(new_cd)
        else:
            self.used_cd_list[best_cd_index].add_data(item)
