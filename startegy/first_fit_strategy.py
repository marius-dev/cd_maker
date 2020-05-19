from cd import CD
from cd_item import CdItem
from startegy.cd_making_strategy import CdMakingStrategy


class FirstFitStrategy(CdMakingStrategy):
    def get_name(self):
        return "first_fit_with_random_data"

    def apply_strategy(self, item: CdItem):
        found_cd = False
        for used_cd in self.used_cd_list:
            if used_cd.remaining_capacity >= item.get_size():
                used_cd.add_data(item)
                found_cd = True
                break

        if found_cd is False:
            new_cd = CD(len(self.used_cd_list))
            new_cd.add_data(item)
            self.used_cd_list.append(new_cd)
