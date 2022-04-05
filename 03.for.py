# Ejemplo de estructura para iterar utilizando secuencias de cosas
# Listas

drinks = ["Mojito", "Margarita", "Piña Colada"]
for drink in drinks:
    print(drink)

print("##########################################")

#El for tambien funciona con letter 
for letter in "Tio Chalie":
    print(letter)

print("##########################################")

# El for tambien puede ser usado con el break
for drink in drinks:       
    if drink == "Margarita":
        break
    print(drink)


print("##########################################")

# El for tambien puede ser usado con el break
for drink in drinks:       
    if drink == "Margarita":
        continue
    print(drink)
else:
    print("Bertha se termino las Margaritas")

print("##########################################")

# for anidados
sizes = ["Normal", "Large", "Tio Charlie XL"]
for size in sizes:
    for drink in drinks:
        print(drink, size)

