import rutt
from datetime import datetime, timedelta

cupon_uso = {}

def porcentaje_por_rut(rut):
    ultimo_digito = rut[-1]
    if ultimo_digito.isdigit():
        ultimo_digito = int(ultimo_digito)
        if ultimo_digito == 0:
            return 7
        elif ultimo_digito % 2 == 0:
            return 6
        else:
            return 5
    elif ultimo_digito.lower() == 'k':
        return 7
    return 0

def tiempo_de_cupon(rut):
    ahora = datetime.now()
    if rut in cupon_uso:
        tiempo_desde_ultimo_uso = ahora - cupon_uso[rut]
        if tiempo_desde_ultimo_uso < timedelta(hours=24):
            return False
    cupon_uso[rut] = ahora
    return True


def aplicar_descuentos():
    while True:
        print("1.- Aplicar descuento")
        print("2.- Salir")
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            rut = input("Ingrese el RUT (No ingrese el -) (o escriba 'salir'): ")
            if rut.lower() == 'salir':
                break
            if not rutt.validar_rut(rut):
                print("Error: El RUT ingresado no es válido. Intente nuevamente.")
                continue
            if not rutt.rut_existe(rut):
                print("Error: El RUT ingresado no existe. Debe registrarse primero.")
                continue
            if not tiempo_de_cupon(rut):
                print("No puede usar otro cupón dentro de 24 horas.")
                continue
            descuento = porcentaje_por_rut(rut)
            print(f"Descuento aplicado: {descuento}%")

        elif opcion == 2:
            print("Adios")
            break
