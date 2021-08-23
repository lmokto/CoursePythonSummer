def printName(func):
    # func is the function to be wrapped
    def pn(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return pn


@printName
def add2Num(x, y):
    # add two numbers
    # print("add")
    return(x+y)


class DateDecorator(object):
    def instantMethodDecorator(self, func):
        def printDate(*arg, **kwargs):
            print('Instance method decorator at time: {value}'.format(value=datetime.today()))
            return func(*arg, **kwargs)
        return printDate
    @classmethod
    def classMethodDecorator(self, func):
        def printDate(*arg, **kwargs):
            print('Instance method decorator at time: {value}'.format(value=datetime.today()))
            return func(*arg, **kwargs)
        return printDate


def handle_except(func):
    def pn(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as Exp:
            print('Controlling exception {msg}'.format(msg=Exp))
    return pn


@handle_except
def testing():
    return 1+'a'


def main():
    # decorator: instance method
    a = DateDecorator()

    @a.instantMethodDecorator
    def add(a, b):
        return a + b

    # decorator: class method
    @DateDecorator.classMethodDecorator
    def sub(a, b):
        return a - b

    sum = add(2, 3)
    # Instance method decorator at time :
    #  2017-02-04 13:31:27.742283

    diff = sub(2, 3)
    # Class method decorator at time :
    #  2017-02-04 13:31:27.742435
    print(sum)
    print(diff)
    print(testing)
    print(add2Num(2, 4))


if __name__ == '__main__':
    main()
