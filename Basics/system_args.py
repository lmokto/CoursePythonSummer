import sys


def add(a, b):
    return 'Result of th sum its {total}'.format(total=a+b)


def main():
    message = "El modulo es: {module}, args={argv}"
    try:
        args = sys.argv
        filename = args[0]
        kargs = args[1:]
        result = add(int(args[1]), int(args[2]))
        print(message.format(module=filename, argv=kargs))
        print(result)
    except:
        print("No dispone de suficientes argumentos para utilizar el script")
    finally:
        print('end of the script')


if __name__ == '__main__':
    main()

