import random

number = random.randrange(1,50)
res = int(input("Adivina un numero de 1 a 50 :"))
while res != number:
    if res < number:
        print("Es un numero mas grande, intentalo de nuevo")
        res = int(input("\nAdivina un numero de 1 a 50 : "))
    else:
         print("Es un numero mas pequeño, intentalo de nuevo")
         cres = int(input("\nAdivina un numero de 1 a 50 : "))
        

print("Le atinaste al numero") 