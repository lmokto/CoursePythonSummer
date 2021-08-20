class BioSeq(object):
    def __init__(self, name, letters):
        self.name = name
        self.letters = letters

    def toFasta(self):
        return ">"+self.name+"\n"+self.letters

    def __getitem__(self,index):
        return self.letters[index.start:index.stop]


class DNASeq(BioSeq):
    _alpha = {'a':'t', 't':'a', 'c':'g', 'g':'c'}

    def __init__(self, name, letters):
        BioSeq.__init__(self, name, letters.lower())
        if not all(True for c in self.letters if c in self._alpha.keys()):
            raise ValueError('Invalid nucleotide:'+c)

    def revcomp(self):
        return "".join(self._alpha[c] for c in reversed(self.letters))

    @classmethod
    def alphabet(cls):
        return cls._alpha.keys()


def main():
    seq = DNASeq('AC1004', 'TTGACA')
    print(seq.revcomp())
    print(DNASeq.alphabet())


if __name__ == '__main__':
    main()
