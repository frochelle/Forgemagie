"""
Item Class
"""


class Item:

    def __init__(self, name, stats):
        # stats is a dict like stats[carac] = value
        self.stats = stats
        self.well = 0
        self.name = name
