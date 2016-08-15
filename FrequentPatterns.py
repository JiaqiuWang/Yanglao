class SequencePattern:
    def __init__(self, sequence, support):
        self.sequence = sequence
        self.support = support

    def append(self, p):
        self.sequence.extend(p.squence)
        self.support = min(self.support, p.support)
