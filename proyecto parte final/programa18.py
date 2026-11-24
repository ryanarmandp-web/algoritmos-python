# Contadores iniciales en 0
dentro = infraccion = grave = 0

# Ciclo para 12 vehículos
for i in range(12):
    # Pide la velocidad de cada vehículo
    vel = float(input(f"Vehículo {i+1} - velocidad: "))

    # Si va a 90 o menos, está dentro del límite
    if vel <= 90:
        dentro += 1
    else:
        # Si supera 90, cuenta como infracción
        infraccion += 1

        # Si además supera 110, cuenta como multa grave
        if vel > 110:
            grave += 1

# Muestra los resultados finales
print(f"Dentro del límite: {dentro}")
print(f"Infracción: {infraccion}")
print(f"Multa grave (>110): {grave}")