from abc import ABCMeta, abstractmethod


class CdItem:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_size(self): raise NotImplementedError