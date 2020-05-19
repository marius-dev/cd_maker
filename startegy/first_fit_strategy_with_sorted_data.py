from typing import List

from cd_item import CdItem
from startegy.first_fit_strategy import FirstFitStrategy


class FirstFitStrategyWithSortedData(FirstFitStrategy):

    def get_name(self):
        return "first_fit_with_sorted_data"

    def make_cds(self, items: List[CdItem]):
        sorted_items = sorted(items, key=lambda x: x.get_size(), reverse=True)
        super().make_cds(sorted_items)