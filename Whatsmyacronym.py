cadena = input("Escriba una frase ")
palabras = cadena.split()
print (palabras)
newCdena = ""
for p in palabras :
    newCdena = newCdena + p[0]
print( newCdena )