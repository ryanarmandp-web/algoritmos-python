"""
Programa: Conteo de focos por color

Descripción:
Una compañía fabrica focos de colores (verde, blanco y rojo).
Se desea contabilizar de un lote de N focos, cuántos hay de
cada color en existencia.


1. Solicita el tamaño del lote (N).
2. Recorre N veces pidiendo el color de cada foco.
3. Valida que la opción ingresada sea 1, 2 o 3.
4. Incrementa el contador correspondiente.
5. Muestra el total por color.
"""

# --- Inicialización de contadores ---
# Acumuladores para cada tipo de color
verdes = 0
blancos = 0
rojos = 0

# --- Entrada de datos principal ---
# Se pide el número total de focos del lote
focos = int(input("Dime la cantidad de focos de este lote: "))

# --- Proceso de conteo ---
# Ciclo for que recorre desde el foco 1 hasta N
for i in range(focos):
    # Se solicita el color del foco actual
    color = int(input(f"De que color es el foco No.{i+1} (1)verde (2)blanco (3)rojo: "))

    # Validación: Obliga al usuario a ingresar solo 1, 2 o 3
    while color != 1 and color != 2 and color != 3:
        print("Opcion incorrecta, vuelva a ingresar: ")
        color = int(input("Ingrese (1)verde (2)blanco (3)rojo: "))

    # Clasificación y conteo según el color
    if color == 1:
        verdes += 1  # Incrementa contador de verdes
    elif color == 2:
        blancos += 1 # Incrementa contador de blancos
    elif color == 3:
        rojos += 1   # Incrementa contador de rojos

# --- Salida de resultados ---
print(f"\n--- Resultados del lote ---")
print(f"Cantidad de focos verdes: {verdes}")
print(f"Cantidad de focos blancos: {blancos}")
print(f"Cantidad de focos rojos: {rojos}")