def Cadena_mas_larga():
    Datos = {}
    texto = str(input("Ingrese el texto a procesar: "))

    frase = texto.split()
    Mas_larga= []
    for palabra in frase:
        Mas_larga.append((len(palabra), palabra))
    Mas_larga.sort
    grande = Mas_larga[-1][1]
    lista = []
    for i in grande:
        lista.append(i)
    print("Caracter mas largo del texto")
    Datos[grande] = lista
    print(Datos)
