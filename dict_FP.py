class ItemPattern:
    def __init__(self, item, support):

        self.key = "service"

    def append(self, p):
        self.sequence.extend(p.squence)
        self.support = min(self.support, p.support)

