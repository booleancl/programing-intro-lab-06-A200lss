# Estructura de control while ejecuta un conjunto de setencias mienstras l condición sea verdadera

iteractor = 0
while iteractor < 10:
    print(iteractor)
    iteractor +=  1

print("########################################")

iteractor = 10
while iteractor >= 0:
    print(iteractor)
    iteractor -=  1

print("########################################")
#Romper el while con un break

iteractor = 0
while iteractor < 100:
    print(iteractor)
    if iteractor == 42:
        break
    iteractor += 2

print("########################################")
# Saltarnos un paso con continue

iteractor = 1
while iteractor <= 100:
    if iteractor % 3 == 0:
        iteractor += 1
        continue
    print(iteractor)
    iteractor += 1

print("########################################")
iteractor = 0
while iteractor < 100:
    iteractor += 1
    if iteractor % 3 == 0:
        continue
    print(iteractor)
else:
    print("El interactor ya no es menor que 100")

