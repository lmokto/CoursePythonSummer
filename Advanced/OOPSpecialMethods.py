class BioSeq(object):
    def __init__(self, name, letters):
        self.name = name
        self.letters = letters
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self.letters[index.start:index.stop]
        return self.letters[index]
    def __eq__(self, other):
        return self.letters == other.letters
    def __add__(self, other):
        return BioSeq(self.name+"_"+other.name, self.letters+other.letters)
    def __str__(self):
        return self.name+":"+self.letters
    def __len__(self):
        return len(self.letters)
