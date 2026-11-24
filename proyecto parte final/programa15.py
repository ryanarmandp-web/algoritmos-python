# Acumulador del gasto total del año
total_anual = 0

# Ciclo para los 6 bimestres del año
for bimestre in range(1, 7):
    # Pide los kWh consumidos en el bimestre
    kwh = float(input(f"Bimestre {bimestre} - kWh: "))

    # Tarifa base: hasta 250 kWh a $1.5
    if kwh <= 250:
        importe = kwh * 1.5
    else:
        # Excedente: primeros 250 kWh a $1.5 y el resto a $2.8
        importe = 250 * 1.5 + (kwh - 250) * 2.8

    # Acumula el importe al total anual
    total_anual += importe
    # Muestra el importe del bimestre
    print(f"Bimestre {bimestre}: ${importe:.2f}")

# Muestra el gasto total del año
print(f"Gasto anual total: ${total_anual:.2f}")