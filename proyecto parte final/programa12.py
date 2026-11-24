# Pide cuántas ventas se van a registrar
n = int(input("¿Cuántas ventas? "))
# Acumulador de comisiones y registro de la mayor venta
total_comision = 0
mayor_venta = 0

# Ciclo para cada venta
for i in range(n):
    # Pide el monto de la venta
    venta = float(input(f"Venta {i+1}: $"))

    # Si la venta supera a la mayor registrada, la actualiza
    if venta > mayor_venta:
        mayor_venta = venta

    # Calcula comisión según el monto de la venta
    if venta > 1500:
        # Más de $1500: comisión del 10%
        total_comision += venta * 0.10
    elif venta >= 500:
        # De $500 a $1500: comisión del 5%
        total_comision += venta * 0.05
    # Menos de $500: sin comisión

# Muestra el total de comisiones y la mayor venta
print(f"Total comisiones: ${total_comision:.2f}")
print(f"Mayor venta: ${mayor_venta:.2f}")