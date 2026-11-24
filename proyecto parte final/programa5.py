# Pide cuántos artículos hay en el lote
N = int(input("Cuantos articulos hay en el lote? "))

# Diccionario de contadores por código de categoría, inician en 0
conteo = {1: 0, 2: 0, 3: 0}
# Diccionario de nombres por código de categoría
nombres = {1: "Electrónica", 2: "Ropa", 3: "Alimentos"}

# Ciclo para cada artículo del lote
for i in range(N):
    # Ciclo para validar que el código sea 1, 2 o 3
    while True:
        # Pide el código de categoría del artículo
        codigo = int(input(f"Articulo {i+1} - Código (1=Electrónica, 2=Ropa, 3=Alimentos): "))
        # Si el código es válido, sale del ciclo de validación
        if codigo in [1, 2, 3]:
            break
        # Si no es válido, muestra error y vuelve a pedir
        print("Código inválido, usa 1, 2 o 3.")
    # Aumenta el contador de la categoría ingresada
    conteo[codigo] += 1

# Muestra el encabezado del inventario
print("\n--- INVENTARIO ---")
print(f"Total de artículos: {N}")

# Si hay artículos, muestra cantidad y porcentaje por categoría
if N > 0:
    # Recorre cada código de categoría
    for codigo in [1, 2, 3]:
        # Obtiene la cantidad de esa categoría
        cantidad = conteo[codigo]
        # Calcula el porcentaje respecto al total
        porcentaje = (cantidad / N) * 100
        # Muestra nombre, cantidad y porcentaje
        print(f"{nombres[codigo]}: {cantidad} artículos -> {porcentaje:.2f}%")
else:
    # Si no hay artículos, muestra mensaje
    print("No hay artículos.")