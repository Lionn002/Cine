import rutt
from datetime import datetime, timedelta
import random

cupon_uso = {}

def porcentaje_por_rut(rut):
    return random.randint(10, 25)

def tiempo_de_cupon(rut):
    ahora = datetime.now()
    if rut in cupon_uso:
        tiempo_desde_ultimo_uso = ahora - cupon_uso[rut]
        if tiempo_desde_ultimo_uso < timedelta(hours=24):
            return False
    cupon_uso[rut] = ahora
    return True

def aplicar_descuentos(rut):
    while True:
        print("1.- Aplicar descuento")
        print("2.- Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            if not rutt.rut_existe(rut):
                print("Error: El RUT ingresado no existe. Debe registrarse primero.")
                continue
            if not tiempo_de_cupon(rut):
                print("No puede usar otro cupón dentro de 24 horas.")
                continue
            descuento = porcentaje_por_rut(rut)
            print(f"Descuento aplicado: {descuento}%")
            rutt.usuarios[rut]["descuento"] = descuento
        elif opcion == 2:
            print("Adios")
            break
