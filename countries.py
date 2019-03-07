import json
with open("countries.json") as fichero:
	datos=json.load(fichero)

print(datos)