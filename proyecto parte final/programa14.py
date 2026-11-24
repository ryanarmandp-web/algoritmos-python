# Pide cuántos productos se van a ajustar
n = int(input("¿Cuántos productos? "))
# Acumulador de la suma total de los ajustes
suma_ajuste = 0

# Ciclo para cada producto
for i in range(n):
    # Pide el precio del producto
    precio = float(input(f"Precio producto {i+1}: $"))

    # Aplica el porcentaje según el rango de precio
    if precio < 100:
        # Menos de $100: aumento del 5%
        nuevo = precio * 1.05
    elif precio <= 500:
        # De $100 a $500: aumento del 8%
        nuevo = precio * 1.08
    else:
        # Más de $500: aumento del 12%
        nuevo = precio * 1.12

    # Calcula cuánto subió el precio
    ajuste = nuevo - precio
    # Acumula el ajuste al total
    suma_ajuste += ajuste
    # Muestra precio anterior, nuevo y diferencia
    print(f"Anterior: ${precio:.2f}, Nuevo: ${nuevo:.2f}, Diferencia: ${ajuste:.2f}")

# Muestra la suma total de todos los ajustes
print(f"Suma total de ajuste: ${suma_ajuste:.2f}")