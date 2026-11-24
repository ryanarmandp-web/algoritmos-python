# Acumulador para el promedio y variables para mayor y menor
prom = 0
may = 0
men = 0

# Ciclo para los 30 días
for i in range(30):
    # Pide la temperatura del día
    temperatura = float(input(f"dime la temperatura del dia {i+1}: "))
    # Acumula la temperatura para el promedio
    prom += temperatura

    if i == 0:
        # El primer día es el mayor y el menor
        may = temperatura
        men = temperatura
    else:
        # Compara con la mayor y menor registradas
        if temperatura > may:
            # Si es mayor, actualiza la mayor
            may = temperatura
        elif temperatura < men:
            # Si es menor, actualiza la menor
            men = temperatura

# Muestra la temperatura más alta
print(f"la temperatura mas alta fue: {may}")
# Muestra la temperatura más baja
print(f"la temperatura mas baja fue: {men}")
# Muestra el promedio (suma entre 30 días)
print(f"la temperatura promedio fue: {prom/30}")