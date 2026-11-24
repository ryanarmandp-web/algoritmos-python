# Saldo inicial de la deuda
saldo = 10000
# Pago fijo mensual
pago = 1000
# Contador de meses y acumulador de intereses
mes = 0
total_interes = 0

# Ciclo mientras quede saldo por pagar
while saldo > 0:
    # Aumenta el contador de meses
    mes += 1
    # Calcula el interés del mes sobre el saldo actual (2%)
    interes = saldo * 0.02
    # Acumula el interés al total pagado
    total_interes += interes
    # Suma el interés y resta el pago al saldo
    saldo += interes - pago
    # Si el saldo queda negativo, lo ajusta a 0
    if saldo < 0:
        saldo = 0
    # Muestra el interés y saldo del mes
    print(f"Mes {mes}: Interés ${interes:.2f}, Saldo ${saldo:.2f}")

# Muestra en cuántos meses se liquidó y el total de intereses
print(f"Se liquidó en {mes} meses")
print(f"Total pagado en intereses: ${total_interes:.2f}")