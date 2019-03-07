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
		idioma = input("Dime un idioma: ").title()
		pais = input("Dime un país: ").title()

# Opción de error de opción		    
	else:
		print()
		print("Error de opción")
		print()