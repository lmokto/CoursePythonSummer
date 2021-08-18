ERROR = 'Message de error: {msg}'


def add(a, b):
	return a+b


def divider_msg():
	print('----------')


def multiply(ch, n):
	print(ch*n)


def sum_and_multiply(arg):
	result = add(arg, 3)
	divider_msg()
	multiply(result, 2)


def handle_error(arg, function):
	try:
		function(arg)
	except Exception as e:
		print(ERROR.format(msg=e))


def use_wrong_case():
	handle_error("1", sum_and_multiply)


def use_correct_case():
	handle_error(1, sum_and_multiply)


def main():
	use_wrong_case()
	use_correct_case()


if __name__ == '__main__':
	main()
