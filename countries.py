import json
with open("countries.json") as fichero:
	doc=json.load(fichero)


def fronteras(doc,pais):
	fronteras=[]
	for paises in doc:
		if paises["name"]["common"] == pais:
			if len(paises["borders"]):
				fronteras.append(paises["borders"])
			else:
				print("Este país no tiene fronteras, es una isla.")
	return fronteras

def siglas_pais(doc,siglas):
	name=[]
	for paises in doc:
		if siglas == paises["cca3"]:
			name.append(paises["name"]["common"])
	return name

def continentes(doc,continente):
	paises=[]
	for conti in doc:
		if continente == conti["region"]:
			paises.append(conti["name"]["common"])
	return paises

def moneda(doc,currency):
	paises__=[]
	for paises in doc:
		if currency in paises["currency"]:
			paises__.append(paises["name"]["common"])
	return paises__

def idioma():
	while True:
		print("Dime el idioma:")
		print("1.Checo")
		print("2.Alemán")
		print("3.Francés")
		print("4.Croata")
		print("5.Italiano")
		print("6.Japonés")
		print("7.Holandés")
		print("8.Portugués")
		print("9.Ruso")
		print("10.Esloveno")
		print("11.Español")
		print("12.Finlandés")
		print("13.Estonio")
		print("14.Chino")
		print("15.Polaco")
		print("16.Coreano")
		print()
		opcion=int(input("Elige opción: "))
		print()

		if opcion == 1:
			idioma="ces"
			return idioma
		elif opcion == 2:
			idioma="deu"
			return idioma
		elif opcion == 3:
			idioma="fra"
			return idioma
		elif opcion == 4:
			idioma="hrv"
			return idioma
		elif opcion == 5:
			idioma="ita"
			return idioma
		elif opcion == 6:
			idioma="jpn"
			return idioma
		elif opcion == 7:
			idioma="nld"
			return idioma
		elif opcion == 8:
			idioma="por"
			return idioma
		elif opcion == 9:
			idioma="rus"
			return idioma
		elif opcion == 10:
			idioma="slk"
			return idioma
		elif opcion == 11:
			idioma="spa"
			return idioma
		elif opcion == 12:
			idioma="fin"
			return idioma
		elif opcion == 13:
			idioma="est"
			return idioma
		elif opcion == 14:
			idioma="zho"
			return idioma
		elif opcion == 15:
			idioma="pol"
			return idioma
		elif opcion == 16:
			idioma="kor"
			return idioma
		else:
			print()
			print("Error de opción")
			print()

def idiomas(doc,idioma,pais):
	for i in doc:
		if pais == i["name"]["common"]:
			return i["translations"][idioma]["common"]

def tamapaises(doc,npaises):
	lista = []
	for i in range(npaises):
		pais = input("País: ")
		lista.append(pais)
	return lista

while True:
	print()
	print("1.Pedir país y listar fronteras.")
	print("2.Pedir continente y mostrar cuantos países tiene.")
	print("3.Pedir moneda y que te diga de que país es.")
	print("4.Pedir un idioma y país, y mostrar la traducción de ese país en ese idioma.")
	print("5.Preguntar cuantos países se va a preguntar y mostrar por tamaño ordenados.")
	print("0.Salir")
	print()
	opcion=int(input("Elige opción: "))
	print()

# Opción para despedir el programa
	if opcion == 0:
		print()
		print("Adiós!")
		print()
		break;

# Opción 1: pedir país y listar fronteras.
	elif opcion == 1:
		pais=input("Dime un país: ").title()
		print("%s tiene fronteras con:" % pais)
		for fronte in fronteras(doc,pais):
			for siglas in fronte:
				for name in siglas_pais(doc,siglas):
					print(name)

	elif opcion == 2:
		continente=input("Dime un continente: ").title()
		region = continentes(doc,continente)
		print()
		print("%s tiene %i países" % (continente,len(region)))

	elif opcion == 3:
		currency=input("Dime una moneda: ").upper()
		paises = moneda(doc,currency)
		print()
		print("La moneda %s pertenece a los siguientes países:" % currency)
		for pais in paises:
			print(pais)

	elif opcion == 4:
		idioma = idioma()
		pais = input("Dime un país: ").title()
		idio = idiomas(doc,idioma,pais)
		print("La traducción es: ",idio)

	elif opcion == 5:
		npaises = int(input("¿Cuántos países quiere comparar?: "))
		lista = tamapaises(doc,npaises)
		print(lista)

# Opción de error de opción		    
	else:
		print()
		print("Error de opción")
		print()