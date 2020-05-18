from cd_item import CdItem


class Song(CdItem):
    def __init__(self, name, duration):
        self.name = name
        self.duration = float(duration)

    def get_size(self):
        return self.duration

    def get_name(self):
        return self.name

    def get_duration(self):
        return self.duration
