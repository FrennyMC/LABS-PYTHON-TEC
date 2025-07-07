def traductor():
    lista_español = ["blanco","casa","rojo","zapato","azul","cielo","rosa","ventana","flor","sol"]
    lista_ingles = ["white","house","red","shoe","blue","sky","rose","window","flower","sun"]
    print("Opcion 1 - Español")
    print("Opcion 2 - Ingles")
    print("Respuesta: 1/2")
    Entrada = input("A cual idioma desea traducir: ")
    if Entrada == "1":
        print("lista de palabras en Inglés que puede traducir a Español, elija una y escribala")
        print(lista_ingles)
        Elegida = input("Ingrese la palabra que desea traducir: ")
        Elegida = Elegida.lower()
        if Elegida in lista_ingles:
            pos = lista_ingles.index(Elegida)
        else:
            print("La palabra ingresada no se encuentra dentro de la lista")
        palabra = lista_español[pos]
        print("La traducción de", Elegida , " es ", palabra)
                
    if Entrada == "2":
        print("lista de palabras en Español que puede traducir a Inglés, elija una y escribala")
        print(lista_español)
        Elegida1 = input("Ingrese la palabra que desea traducir: ")
        Elegida1 = Elegida1.lower()
        if Elegida1 in lista_español:
            pos = lista_español.index(Elegida1)
        else:
            print("La palabra ingresada no se encuentra dentro de la lista")
        palabra1 = lista_ingles[pos]
        print("La traducción de", Elegida1,"es", palabra1)

traductor()
