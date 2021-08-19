import argparse
import os


def openfile(filename, mode):
    try:
        with open(filename, mode) as file:
            print(file.readlines())
    except Exception as Error:
        print(Error)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help="introducing the name of filename to read", type=str)
    parser.add_argument('--mode', help="create/read/append", default='r', type=str)
    args = parser.parse_args()
    if os.path.isfile(args.filename):
        openfile(args.filename, mode=args.mode)
    else:
        print("The filename doesnt exist {arg}".format(arg=args.filename))


if __name__ == '__main__':
    main()
