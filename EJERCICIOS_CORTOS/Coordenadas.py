from matplotlib import pyplot as plt


def coordenadas():
    # Ingresar Datos
    print("Coordenadas de la Primera recta")
    A = int(input("Ingrese la coordenada en el eje x1: "))
    B = int(input("Ingrese la coordenada en el eje y1: "))
    print("Coordenadas de la Primera recta")
    P = int(input("Ingrese la coordenada en el eje x1: "))
    Q = int(input("Ingrese la coordenada en el eje y1: "))
    
    
    
                        
    rango = list(range(100))
    xdata = [A]
    ydata = [P]
    
    x1data = [P]
    y1data = [Q]
    
    plt.plot(xdata, ydata, 'b')
    plt.plot(x1data, y1data, 'b')

    plt.axhline(y=5, xmin=0.1, xmax=0.9)

    plt.grid()
    plt.show()
      
coordenadas()
