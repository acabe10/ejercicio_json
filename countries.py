import json
with open("countries.json") as fichero:
	doc=json.load(fichero)

pais=input("Dime un país: ").title()

fronteras=[]
for paises in doc:
	if paises["name"]["common"] == pais:
		if len(paises["borders"]):
			print(paises["borders"])
		else:
			print("Este país no tiene fronteras, es una isla.")