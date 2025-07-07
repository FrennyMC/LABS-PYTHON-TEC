#importación de las expresiones regulares
import re

#funciones
def validarCedula(pcedula):
    """
    Funcionamiento: Valida que la cédula sea de nueve dígitos exactamente, con el primero sin poder ser cero
    Entradas:
    -cedula(str)= cédula(s) ingresada(s) por el usuario
    Salidas:
    - como la función se llamará de manera constante en las funciones independientes su salida es continuar con dichas funciones
    """
    restricciones = r"^[1-9][0-9]{8}$"
    return re.fullmatch(restricciones, pcedula) is not None

def agregarDonadores(precuperados):
    """
    Funcionamiento: Se encarga de agregar los nuevos donadores al programa y verifica que no estén previamente registrados
    Entradas:
    -precuperados(list)= lista con los donantes previamente recuperados
    Salidas:
    -registra a los donadores ingresados por el usuario
    """
    nuevos = []
    cantidad = 4
    print("Debe ingresar 4 cédulas válidas y no repetidas:")
    while len(nuevos) < cantidad:
        cedula = input(f"Ingrese la cédula #{len(nuevos)+1}: ") #le indica al usuario que ingrese el número de cédulas indicado, y luego le indica qúe número de cédula en tiempo de ejecución debe ingresar 
        if not validarCedula(cedula):
            print("Formato de cédula inválido. Debe tener 9 dígitos y no iniciar en 0.")
            continue
        if cedula in precuperados or cedula in nuevos:
            print("La cédula ya está registrada.")
            continue
        nuevos.append(cedula) #agrega las cédulas nuevas a la lista "nuevos"
    precuperados.extend(nuevos) #agrega los donantes nuevos a la lista inicial
    return print("Donantes registrados satisfactoriamente.")

def decodificarDonador(precuperados):
    """
    Funcionamiento: Se encarga de decodificar la cédula ingresada por el usuario para indicarle el tomo y la provincia.
    Entradas:
    -cedula(str)= cédula ingresada por el usuario para decodificar
    Salidas:
    -retorna si la cédula está registrada o no, y se lo iindica a l usuario
    """
    cedula = input("Indique el número de cédula a decodificar: ")
    if not validarCedula(cedula): #llama a la función de validar la cédula
        print("Cédula inválida") #en caso de ser inváilod el formato de cédula se lo indica al usuario
        return
    if cedula in precuperados: #verifica que la cédula esté en la lista de donantes recuperados
        provincia = int(cedula[0])
        tomo = cedula[1:5]
        asiento = cedula[5:]
        print("Usted es de {}\nestá registrado en el tomo {}, y el asiento {}".format(provincias.get(provincia, "Provincia desconocida"), tomo, asiento))
    else:
        return print("El donador no es un donante aún.")#le indica al usuario si la cédula no está ingresada previamente

def listarPorProvincia(precuperados):
    """
    Funcionamiento: lista los donadores según el registro de naturalizaciones indicado en las especificaciones del problema
    Entradas:
    -código=código ingresado por el usuario para determinar cuáles cédulas pertenecen a esa provincia o a los casos especiales(8 y 9)
    Salidas:
    -c(str)= son los datos de las personas filtradas mediante el código ingresado por el usuario y retornados en la variable "c"
    """
    print("Seleccione una provincia por código:")
    for i, j in provincias.items(): #toma los códigos para cada provincia y los muestra al usuario
        print(f"{i}. {j}")
    opcion = input("Código: ")
    if not opcion.isdigit() or int(opcion) not in provincias:
        print("Opción inválida")# valida que la opción escogida por el usuario esté dentro de los valores permitidos
        return
    codigo = int(opcion)
    filtrados = [c for c in precuperados if int(c[0]) == codigo]
    if filtrados:
        print(f"Los donadores de la provincia de {provincias[codigo]}, son {len(filtrados)} con las cédulas:")#muestra los donadores ya filtrados
        for c in filtrados:
            print(c)
    else:
        print("Aún no hay personas donadoras de esa naturalización")#mustra si no hay donadores de dicha provincia o caso especial

def listarTodos(precuperados):
    """
    Funcionamiento: recorre todos los donadores de todas las provincias y casos especiales y los muestra, ya sea qeu hayan o no
    Entradas:
    -al ingresar la opción 4 muestra de manera automática los datos descritos arriba en el funcionamiento
    Salidas:
    -muestra los datos en cuestión
    """
    for codigo in range(1, 10):
        filtrados = [c for c in precuperados if int(c[0]) == codigo]
        if filtrados:
            print(f"Los donadores de la provincia de {provincias[codigo]}, son {len(filtrados)} con las cédulas:") #muestra todos los datos en las provincias o casos donde hay datos que mostrar
            for c in filtrados:
                print(c)
        else:#en caso de no ser así muestra que no hay donadores en dicha provincia o caso
            print(f"Los donadores de la provincia de {provincias[codigo]}:")
            return print("Aún no reporta donadores")

def donadoresNoTipicos(precuperados):
    """
    Funcionamiento: muestra los datos de las cédulas de donadores solamente de alguno de los casos especiales, 8 o 9
    Entradas:
    -al ingresar la opción 5 en el menú principal, muestra directamente lo solicitado
    Salidas:
    -muestra los datos de los donadores no típicos, los naturalizados o nacionalizados u los de la provincia de partida especial de nacimientos
    """
    for codigo in [8, 9]:#busca los datos de acuerdo a los dos códigos de casos especiales
        filtrados = [c for c in precuperados if int(c[0]) == codigo]
        if filtrados:
            print(f"Los donadores de la provincia de {provincias[codigo]}, son {len(filtrados)} con las cédulas:")
            for c in filtrados:
                print(c) #muestra todos los datos de los casos especiales
        else:
            print(f"Los donadores de la provincia de {provincias[codigo]}:")
            print("Aún no reporta donadores")#mustra el mensaje en caso de no existir donadores en dicha categoría

#provincias (diccionario)
provincias = {
    1: "San José",
    2: "Alajuela",
    3: "Cartago",
    4: "Heredia",
    5: "Guanacaste",
    6: "Puntarenas",
    7: "Limón",
    8: "Nacionalizado o naturalizado",
    9: "Partida especial de nacimientos"
}

