import random as rd

def mapa_butacas(filas, columnas, prob_ocupado=0.25):
    butacas = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if rd.random() < prob_ocupado:
                fila.append('X')
            else:
                fila.append('O')
        butacas.append(fila)
    return butacas

def mostrar_mapa(butacas):
    filas = len(butacas)
    columnas = len(butacas[0])
    
    encabezado = "  " + " ".join([str(i+1) for i in range(columnas)])
    print(encabezado)
    
    for i, fila in enumerate(butacas):
        print(chr(65 + i), " ".join(fila))

def seleccionar_butacas(butacas, cantidad):
    filas = len(butacas)
    columnas = len(butacas[0])
    seleccionadas = 0

    while seleccionadas < cantidad:
        mostrar_mapa(butacas)
        print(f"Seleccione la butaca {seleccionadas + 1} de {cantidad}:")
        
        while True:
            fila = input("Fila (A-G): ").upper()
            columna = input("Columna (1-7): ")
            if len(fila) == 1 and 'A' <= fila <= 'G' and columna.isdigit() and 1 <= int(columna) <= 7:
                columna = int(columna) - 1
                fila_num = ord(fila) - 65
                if butacas[fila_num][columna] == 'O':
                    butacas[fila_num][columna] = 'S'
                    seleccionadas += 1
                    break
                else:
                    print("Butaca ocupada. Seleccione otra.")
            else:
                print("Coordenadas fuera de rango para elegir. Intente nuevamente.")

    return butacas