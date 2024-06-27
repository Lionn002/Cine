import rutt
import entradas
import comida
import cupones
import pago

def generar_boleta(rut):
    print(f"RUT: {rut}")
    print(f"ORD: {len(entradas.compras_entradas) + len(comida.compras_comida):03d}")
    print("--------------------------------------------------")
    print("Detalle de compras:")
    total_entradas = sum([compra[5] for compra in entradas.compras_entradas if compra[0] == rut])
    total_comida = sum([compra[1] for compra in comida.compras_comida if compra[0] == rut])
    subtotal = total_entradas + total_comida
    descuento = 0

    if "descuento" in rutt.usuarios[rut]:
        porcentaje_descuento = rutt.usuarios[rut]["descuento"]
        descuento = (porcentaje_descuento / 100) * subtotal
        print(f"Descuento aplicado: {porcentaje_descuento}%")
        print(f"Descuento: ${descuento:.2f}")

    subtotal_con_descuento = subtotal - descuento
    iva = 0.19 * subtotal_con_descuento
    total = subtotal_con_descuento + iva

    print(f"Total gastado en entradas: ${total_entradas:.2f}")
    print(f"Total gastado en comida: ${total_comida:.2f}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Descuento: ${descuento:.2f}")
    print(f"IVA: ${iva:.2f}")
    print(f"Total: ${total:.2f}")

    pago.seleccionar_metodo_pago(total)

if __name__ == "__main__":
    rut = input("Ingrese su RUT sin puntos ni guion: ")
    rut = rutt.validar_rut(rut)
    if rut and rutt.rut_existe(rut):
        generar_boleta(rut)
    else:
        print("RUT no válido o no registrado.")
