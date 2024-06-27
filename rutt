usuarios = {}

def validar_rut(rut):
    if not rut.isdigit() or len(rut) < 8 or len(rut) > 9:
        return False
    rut = rut[:-1] + '-' + rut[-1]
    return rut

def rut_existe(rut):
    return rut in usuarios

def crear_usuario():
    while True:
        rut = input("Ingrese su RUT sin puntos ni guion: ")
        rut = validar_rut(rut)
        if not rut:
            print("RUT inválido. Intente nuevamente.")
            continue
        if rut_existe(rut):
            print("El RUT ya está registrado. Intente iniciar sesión.")
            return None
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        usuarios[rut] = {"nombre": nombre, "apellido": apellido}
        print(f"Usuario {rut} creado exitosamente.")
        return rut

def iniciar_sesion():
    while True:
        rut = input("Ingrese su RUT sin puntos ni guion: ")
        rut = validar_rut(rut)
        if not rut:
            print("RUT inválido. Intente nuevamente.")
            continue
        if not rut_existe(rut):
            print("El RUT no está registrado. Intente crear un usuario.")
            return None
        print(f"Bienvenido {rut}")
        return rut

def main():
    while True:
        print("[1] Iniciar sesión")
        print("[2] Crear usuario")
        print("[3] Salir")
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            rut = iniciar_sesion()
            if rut:
                return rut
        elif opcion == '2':
            rut = crear_usuario()
            if rut:
                return rut
        elif opcion == '3':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
