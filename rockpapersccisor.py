import random
aleatorio = random.randrange(0, 3)
Pc = ""
print("1.- Piedra")
print("2.- Papel")
print("3.- Tijera")
opc = int(input("Elije una opc: "))

if opc == 1:
    Usuario = "piedra"
elif opc == 2:
    Usuario = "papel"
elif opc == 3:
    Usuario = "tijera"


if aleatorio == 0:
    Pc = "piedra"
elif aleatorio == 1:
    Pc = "papel"
elif aleatorio == 2:
    Pc = "tijera"
print("PC elijio: ", Pc)
print("...")
if Pc == "piedra" and Usuario == "papel":
    print("Ganaste, papel envulve piedra")
elif Pc == "papel" and Usuario == "tijera":
    print("Ganaste, Tijera corta papel")
elif Pc == "tijera" and Usuario == "piedra":
    print("Ganaste, Piedra pisa tijera")
if Pc == "papel" and Usuario == "piedra":
    print("perdiste, papel envulve piedra")
elif Pc == "tijera" and Usuario == "papel":
    print("perdiste, Tijera corta papel")
elif Pc == "piedra" and Usuario == "tijera":
    print("perdiste, Piedra pisa tijera")
elif Pc == Usuario:
    print("empate")