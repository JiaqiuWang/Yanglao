class SequencesFP:
    def __init__(self, sequence, support):
        self.sequence = []
        self.sequence = sequence
        self.support = support

    def get_sequence(self):
        return self.sequence

    def get_support(self):
        return self.support

    def set_sequence(self, var_seq):
        self.sequence = var_seq

    def set_support(self, var_sup):
        self.support = var_sup
