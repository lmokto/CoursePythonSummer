msg_help = "Ingrese un numero por favor..."

def function_with_validation(arg):
	if type(arg) == int:
		new_arg = arg*5
		return "Resultado {valor}".format(valor=new_arg)
	else:
		return msg_help


def function_without_validation(arg):
	new_arg = arg+5
	print("Resultado {valor}".format(valor=new_arg))
	return "No se puede mostrar el resultado"


def function_with_exception(arg):
	try:
		new_arg = arg+5
		return "Resultado {valor}".format(valor=new_arg)
	except Exception as exp:
		print("Ocurrio una exception: {msg}".format(msg=exp))
		return msg_help


def function_use_case_ok_int(value):
	print(function_with_exception(value))
	print(function_without_validation(value))
	print(function_with_validation(value))


def function_use_case_fail_string(value):
	function_with_exception(value)
	function_without_validation(value)
	function_with_validation(value)


def main():
	divider = "#"*30
	print(divider)
	print("function_use_case_ok_int")
	function_use_case_ok_int(5)
	# print(divider)
	# print("function_use_case_fail_string")
	# function_use_case_fail_string("5")


if __name__ == '__main__':
	main()
