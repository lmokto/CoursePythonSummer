def get_cantidad_contactos(agenda_telefonos):

	cantidad = len(agenda_telefonos.keys())
	print("Cantidad de contactos: {total}".format(total=cantidad))

	if cantidad < 5:
		print("Agenda de Telefono dispone menos de 5 contactos")
	elif cantidad < 10:
		print("Agenda de Telefono dispone mas de 10 contactos")
	elif cantidad < 15:
		print("Agenda de Telefono dispone mas de 15 contactos")
	elif cantidad < 20:
		print("Agenda de Telefono dispone mas de 20 contactos")
	else:
		print("Agenda de Telefono esta fuera del alcance")


def main():
	agenda_telefonos = {"Jorge": 123123, "Andrea": 123123}
	agenda_telefonos.update({"Luis": 123123})
	get_cantidad_contactos(agenda_telefonos)



if __name__ == '__main__':
	main()
