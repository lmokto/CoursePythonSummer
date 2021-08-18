def try_except_input():
    """ It should write two values int
    >>> try_except_input()
    Tell me one number: 1
    Tell me another number: 2
    a/b =  0.5
    a+b =  3
    Success flow...
    End.
    """
    try:
        a = int(input('Tell me one number: '))
        b = int(input('Tell me another number: '))
        print('a/b = ', a/b)
        print('a+b = ', a+b)
    except ValueError:
        print('Could not convert to a number.')
    except ZeroDivisionError:
        print('Can not divide by zero')
    except KeyboardInterrupt:
        print('This script was interrupted')
    except:
        raise ValueError('Something went very wrong!')
    else:
        print('Success flow...')
    finally:
        print('End.')


def main():
    try_except_input()


if __name__ == '__main__':
    main()

