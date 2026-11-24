# Pide el monto del préstamo y el número de meses
P = float(input("Préstamo: $"))
M = int(input("Meses: "))

# Calcula el capital fijo que se pagará cada mes
capital = P / M
# Saldo inicial igual al préstamo
saldo = P

# Ciclo para cada mes, del 1 al total de meses
for mes in range(1, M+1):
    # Calcula el interés del mes sobre el saldo actual (1.5%)
    interes = saldo * 0.015
    # La cuota es capital + interés
    cuota = capital + interes
    # Resta el capital pagado al saldo
    saldo -= capital
    # Muestra el desglose del mes
    print(f"Mes {mes}: Cuota ${cuota:.2f} (Capital ${capital:.2f} + Interés ${interes:.2f}), Saldo ${saldo:.2f}")