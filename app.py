from random import randint

from best_fit_strategy import BestFitStrategy
from first_fit_strategy import FirstFitStrategy
from song import Song

if __name__ == '__main__':
    songs = []

    for i in range(1, 1000):
        songs.append(
            Song('song ' + str(i), randint(1,10))
        )

    cd_making_strategy = FirstFitStrategy()
    cd_making_strategy.make(songs)

    print('\n unused capacity: ' + str(cd_making_strategy.unused_cd_capacity))
    print('\n total capacity: ' + str(cd_making_strategy.total_capacity()))
