import random

def adivina():
    contador = 0
    intentos = []
    número = random.randint(1, 100)
    while int(contador) < 7:
        Num = int(input("Intenta adivinar: "))
        if Num < int(número):
            contador = contador + 1
            print("Tu estimación es muy baja.")
        if Num > int(número):
            contador = contador + 1
            print("Tu estimación es muy alta.")
        if Num == int(número):
            contador = str(contador)
            print("Has adivinado el número en " + contador + " intentos")
        if Num in intentos:
            contador = contador - 1
            print("Este número ", Num ," ya fue ingresado, vuelva a intentar: ")
        intentos.append(Num)
    
    if Num != int(número):
        número = str(número)
        cant = len(intentos)
        cant = str(cant)
        print("Números Intentados",intentos)
        print("En "+ cant + " Intentos")
        print("El número era " + número)

adivina()
