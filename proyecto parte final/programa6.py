# Pide la cantidad de paquetes del lote
lote = int(input("dime la cantidad de paquetes: "))
# Acumulador del peso total, total de recargos y contador de sobrepeso
prom = 0
recargos = 0
sobrepeso = 0

# Ciclo para cada paquete del lote
for i in range(lote):
    # Pide el peso del paquete
    paquete = float(input(f"dime el peso del paquete No.{i+1}: "))
    # Si pesa más de 15 kg, tiene sobrepeso
    if paquete > 15:
        # Suma $50 de recargo por sobrepeso
        recargos += 50
        # Cuenta el paquete con sobrepeso
        sobrepeso += 1
    # Acumula el peso para el promedio
    prom += paquete

# Calcula el peso promedio (peso total entre cantidad de paquetes)
prom = prom / lote
# Muestra cuántos paquetes tuvieron sobrepeso
print(f"La cantidad de paquetes con sobrepeso es de: {sobrepeso}")
# Muestra el cobro total de recargos
print(f"el cobro total de recargos es de: ${recargos}")
# Muestra el peso promedio de los paquetes
print(f"El peso promedio de los paquetes es de: {prom}")