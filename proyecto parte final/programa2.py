# Acumulador del total general de ventas
total = 0
# Acumuladores de totales por categoría
total1 = 0
total2 = 0
total3 = 0
# Contadores de ventas por categoría
men = 0
entre = 0
may = 0
# Pide cuántas ventas se van a ingresar
op = int(input("dime el numero de ventas que vas a ingresar: "))

# Ciclo para cada venta
for i in range(op):
    # Pide el monto de la venta
    a = int(input(f"dime la venta No.{i+1}: "))
    # Ventas menores o iguales a 300
    if a <= 300:
        # Cuenta la venta en esta categoría
        men += 1
        # Suma el monto al total de la categoría
        total1 += a
    # Ventas mayores a 300 y menores o iguales a 800
    elif a > 300 and a <= 800:
        # Cuenta la venta en esta categoría
        entre += 1
        # Suma el monto al total de la categoría
        total2 += a
    # Ventas mayores a 800
    else:
        # Cuenta la venta en esta categoría
        may += 1
        # Suma el monto al total de la categoría
        total3 += a
    # Suma el monto al total general
    total += a

# Muestra la cantidad total de ventas
print(f"Cantidad de ventas: {op}")
# Muestra la cantidad y total de ventas <= 300
print(f"Cantidad de ventas <=300: {men}")
print(f"total de esta categoria: {total1}")
# Muestra la cantidad y total de ventas > 300 y <= 800
print(f"Cantidad de ventas >300 y <=800: {entre}")
print(f"total de esta categoria: {total2}")
# Muestra la cantidad y total de ventas > 800
print(f"Cantidad de ventas >800: {may}")
print(f"total de esta categoria: {total3}")
# Muestra el total general de ventas
print(f"total: {total}")