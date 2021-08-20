class Message(object):
    __message = "Esto es un mensaje de ejemplo"

    @classmethod
    def get_message(cls):
        return cls.__message


def main():
    message = Message.get_message()
    print(message)


if __name__ == '__main__':
    main()

