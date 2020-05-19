import time
from random import randint

from startegy.best_fit_strategy import BestFitStrategy
from cd import CD
from song import Song
from startegy.first_fit_startegy_with_trees import FirstFitStrategyWithTrees
from startegy.first_fit_strategy import FirstFitStrategy
from startegy.first_fit_strategy_with_sorted_data import FirstFitStrategyWithSortedData

if __name__ == '__main__':
    songs = []

    for i in range(1, 100000):
        songs.append(
            Song('song ' + str(i), randint(1, CD.SIZE))
        )

    strategies = [
        # FirstFitStrategyWithTrees(),
        FirstFitStrategy(),
        FirstFitStrategyWithSortedData(),
        BestFitStrategy()
    ]

    for strategy in strategies:
        start_time = time.time()
        strategy.make_cds(songs)

        print('Strategy: ' + str(strategy.get_name()))
        print('Unused capacity: ' + str(strategy.unused_cd_capacity))
        print('Unused CD\'s: ' + str(len(strategy.used_cd_list)))
        print("Execution time %s seconds ---" % (time.time() - start_time))

        print('\n')
