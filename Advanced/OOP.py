class Genes(object):

    def __init__(self):
        self.genes = ['gatA', 2108, 3583, 'agaccta']

    def name(self):
        return self.genes[0]

    def testing(self):
        return self.name

    def length(self):
        return len(self.genes)

    def gc_content(self):
        return self.genes


class GenesSpecialMethods(object):
    def __init__(self, **kwargs):
        self.__props = kwargs.get('props', [])
    def __str__(self):
        return str(self.__props)
    def __getitem__(self, index):
        try:
            if isinstance(index, slice):
                return self.__props[index.start:index.stop]
            return self.__props[index]
        except Exception as Error:
            return ValueError(Error)
    def get_props(self):
        return self.__props
    def set_props(self, value):
        if value not in self.__props:
            self.__props.append(value)
            return True
        raise IndexError('El valor ya esta en props')


class GenesSample(object):

    def __init__(self, **kwargs):
        self.__props = kwargs.get('props', [])

    def __str__(self):
        return str(self.__props)

    def get_props(self):
        return self.__props

    def set_props(self, value):
        if value not in self.__props:
            self.__props.append(value)
            return True
        raise IndexError('El valor ya esta en props')


def main():
    gen1 = Genes()
    gen2 = Genes()
    gen3 = Genes()
    genes = [gen1, gen2, gen3]
    gen_values = [gen.name() for gen in genes]
    print(gen_values)


if __name__ == "__main__":
    main()
