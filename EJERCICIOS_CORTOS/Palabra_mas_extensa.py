def Palabras():
    Palabras_Listas = print("Ingese 5 palabras, Nota por cada palabra presione ENTER: ")
    Palabra1 = input("1-")
    Palabra2 = input("2-")
    Palabra3 = input("3-")
    Palabra4 = input("4-")
    Palabra5 = input("5-")
    
    lista = [Palabra1 ,Palabra2,Palabra3,Palabra4,Palabra5]
    palabra_mayor = len(lista[0])
    palabra_mostrar = lista[0]
    #Calcular palabra mas larga
    for palabra in lista:
	    if palabra_mayor <= len(palabra):
		    palabra_mostrar = palabra
		    palabra_mayor = len(palabra)
	    else:
		    palabra_mostrar = palabra_mostrar

    cadena = palabra_mostrar
    total_caracteres = len(cadena)
    num = total_caracteres + 2
    """Crear Cuadro"""
    #Imprimir
    #Parte arriba
    can_determ = ""
    for i in range(num):
        i = "*"
        can_determ += i 
    print(can_determ)
    #Contar espacios en blanco faltantes
    if Palabra1 == palabra_mostrar:
        linea1 = "*" + Palabra1 +"*"
        print(linea1)
    else:
        espacios1 = " " * total_caracteres 
        Tam1 = total_caracteres - len(Palabra1)
        espacios11 = " " * Tam1
        linea_1 = "*" + Palabra1 + espacios11 + "*"
        print(linea_1)

    if Palabra2 == palabra_mostrar:
        linea2 = "*" + Palabra2 +"*"
        print(linea2)
    else:
        espacios2 = " " * total_caracteres
        Tam2 = total_caracteres - len(Palabra2)
        espacios22 = " " * Tam2 
        linea_2 = "*" + Palabra2 + espacios22 + "*"
        print(linea_2)
        
    if Palabra3 == palabra_mostrar:
        linea3 = "*" + Palabra3 +"*"
        print(linea3)
    else:
        espacios3 = " " * total_caracteres
        Tam3 = total_caracteres - len(Palabra3)
        espacios33 = " " * Tam3 
        linea_3 = "*" + Palabra3 + espacios33 + "*"
        print(linea_3)
        
    if Palabra4 == palabra_mostrar:
        linea4 = "*" + Palabra4 +"*"
        print(linea4)
    else:
        espacios4 = " " * total_caracteres
        Tam4 = total_caracteres - len(Palabra4)
        espacios44 = " " * Tam4 
        linea_4 = "*" + Palabra4 + espacios44 + "*"
        print(linea_4)
        
    if Palabra5 == palabra_mostrar:
        linea5 = "*" + Palabra5 +"*"
        print(linea5)
    else:
        espacios5 = " " * total_caracteres
        Tam5 = total_caracteres - len(Palabra5)
        espacios55 = " " * Tam5 
        linea_5 = "*" + Palabra5 + espacios55 + "*"
        print(linea_5)
    #parte abajo
    can_determ2 = ""
    for i in range(num):
        i = "*"
        can_determ2 += i 
    print(can_determ2)

Palabras()
