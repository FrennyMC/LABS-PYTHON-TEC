def Numeros():

    Entrada = input("Ingrese el número: ")

    
    datos_1 = {"1" : "uno", "2": "dos", "3" : "tres", "4": "cuatro", "5": "cinco", "6":"seis", "7":"siete",
                "8": "ocho", "9": "nueve"}
    
    datos_2 = {"10": "diez", "12": "doce", "13": "trece", "14": "catorce", "15": "quince", "16": "dieciseis",
                 "17": "diecisiete", "18": "dieciocho", "19": "diecinueve","20": "veinte", "30": "treinta", "40": "cuarenta", "50": "cincuenta",
                 "60": "sesenta", "70": "setenta","80": "ochenta", "90": "noventa"}
    
    datos_3 = {"100": "ciento", "200": "doscientos", "300": "trescientos", "400": "cuatroscientos",
                "500": "quinientos", "600": "seiscientos","700": "setescientos",
                "800": "ochoscientos", "900": "Novecientos"}
    
    datos_4 = {"1000": "mil", "2000": "dos mil", "3000": "tres mil", "4000": "cuatro mil",
                "5000": "cinco mil", "6000": "seis mil", "7000": "siete mil"}
    
    if len(Entrada) == 1 :
        print(datos_1[Entrada])
    if len(Entrada) == 2 :
        if Entrada in datos_2 :
            print(datos_2[Entrada])
        elif Entrada not in datos_1 or datos_2:
            cant = []
            for i in Entrada:
                cant.append(i)
            pos1 = cant[0] + "0"
            pos2 = cant[1]
            print(datos_2[pos1],"y",datos_1[pos2])
    if len(Entrada) == 3:
        if Entrada in datos_3:
            print(datos_3[Entrada])
        elif Entrada not in datos_3:
            cant = []
            for i in Entrada:
                cant.append(i)
            pos1 = cant[0] + "00"
            pos2 = cant[1] + "0"
            pos3 = cant[1] + cant[2]
            if pos3 not in datos_2:
                print(datos_3[pos1],datos_2[pos2],"y", datos_1[cant[2]])
            elif pos3 in datos_2 :
                print(datos_3[pos1],datos_2[pos3])
    if len(Entrada) == 4:
        if Entrada in datos_4:
            print(datos_4[Entrada])
        elif Entrada not in datos_4:
            cant = []
            for i in Entrada:
                cant.append(i)
            pos1 = cant[0] + "000"
            pos2 = cant[1] + "00"
            pos3 = cant[2] + "0"
            pos4 = cant[2] + cant[3]
            if pos4 not in datos_2:
                print(datos_4[pos1], datos_3[pos2],datos_2[pos3],"y",datos_1[cant[3]])
            elif pos4 in datos_2:
                print(datos_4[pos1],datos_3[pos2],datos_2[pos4])
Numeros()
