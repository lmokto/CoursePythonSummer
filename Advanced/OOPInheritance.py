class Engine(object):
    def __init__(self, **kwargs):
        self.speed_max = kwargs.get('max', 150)
        self.speed_min = kwargs.get('min', 10)


class Car(Engine):

    def __init__(self, name, brand, **kwargs):
        Engine.__init__(
            self,
            max=kwargs.get('speed_max', 220),
            min=kwargs.get('speed_min', 10)
        )
        self.brand = brand
        self.name = name

    def get_speed_max(self):
        return self.speed_max

    def get_speed_min(self):
        return self.speed_min


class BrandStandard(object):
    def __init__(self, **kwargs):
        self.speed_max = kwargs.get('speed_max')
        self.speed_min = kwargs.get('speed_min')
        self.message = kwargs.get('message')
        self.name = kwargs.get('name')
        self.last_model = kwargs.get('last_model')

    def get_model(self):
        return self.last_model



class CarInformation(object):
    def __init__(self):
        self.message = """
            El auto es de la marca: {brand} y su nombre es :{name}
            y tiene una velocidad minima {speed_min} y maxima {speed_max}
        """

    def get_information(self, car):
        if isinstance(car, Car):
            return self.message.format(
                brand=car.brand,
                name=car.name,
                speed_min=car.get_speed_min(),
                speed_max=car.get_speed_max()
            )
        return ValueError('El auto a instanciar no es una clase')


def main():

    audi = BrandStandard(
        speed_max=250,
        speed_min=20,
        name='Audi',
        message='Das velocity Wagen',
        last_model='A1'
    )

    volkswagen = BrandStandard(
        speed_max=150,
        speed_min=20,
        name='Volkswagen',
        message='Das Wagen',
        last_model='Polo'
    )

    information = CarInformation()

    polo = Car(
        volkswagen.get_model(),
        volkswagen.name,
        speed_min=volkswagen.speed_min,
        speed_max=volkswagen.speed_max
    )

    a1 = Car(
        audi.get_model(),
        audi.name,
        speed_min=audi.speed_min,
        speed_max=audi.speed_max
    )

    polo_info = information.get_information(polo)
    a1_info = information.get_information(a1)

    print(polo_info)
    print(a1_info)


if __name__ == '__main__':
    main()
