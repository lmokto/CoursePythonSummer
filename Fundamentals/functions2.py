error = "Mensaje de error: {msg}"

def add(a, b):
	return a+b


def divider_msg():
	print('----------')


def mult(ch,n):
	print(ch*n)


def sum_and_mult(arg):
	result = add(arg, 3)
	divider_msg()
	mult(result, 2)


def handle_error(arg, function):
	try:
		function(arg)
	except Exception as e:
		print(error.format(msg=e))


def use_wrong_case():
	handle_error("1", sum_and_mult)


def use_correct_case():
	handle_error(1, sum_and_mult)


def main():
	use_wrong_case()
	use_correct_case()


if __name__ == '__main__':
	main()
