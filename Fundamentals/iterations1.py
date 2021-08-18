def testing_while():
	i = 1
	while i<100:
		print(i)
		i += 1
		if i == 30:
			print("breaking ... while")
			break


def testing_color_for():
	colors = ["white", "red", "blue"]
	for color in colors:
		print(color)
		if color == "blue":
			print("for will break whe the its color blue")
			break
		else:
			print("Continue")


def testing_numbers_for():
	seq_number = range(1, 11)
	for number in seq_number:
		print(number)


def testing_string_for():
	characters = "some text"
	for char in characters:
		print(char)


def main():
	testing_string_for()


if __name__ == '__main__':
	main()
