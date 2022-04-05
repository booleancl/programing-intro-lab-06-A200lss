# Ejemplo de una function sin retorno

def volume(radius):
    V = 4/3 * 3.14 * radius ** 3
    print(V)

enigma = volume(7)
print(enigma)

# Ejemplo de una function con valor de retorno
def area(radius):
    a = 3,14 * radius ** 2
    return a

area(7) # Este computo se pierde al no asignarse a ninguna variable

ar = area(7)
print(ar)

# Podemos tener mas de un retorno
def isAdult(age):
    if age < 18:
        return False
    if age >= 18:
        return True

hasBeer = isAdult(18)
print(hasBeer)