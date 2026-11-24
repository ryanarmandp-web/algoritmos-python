# Acumulador del ahorro total
ahorro = 0
# Lista con los nombres de los 12 meses
mes = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

# Ciclo para los 12 meses
for i in range(12):
    # Pide el ahorro del mes actual
    ahorro2 = float(input("Dime cuanto vas a ingresar este mes:_ "))
    # Muestra lo que se ingresó en el mes actual
    print(f"en el mes de {mes[i]} ingresaste: {ahorro2}")
    # Acumula el ahorro al total
    ahorro += ahorro2
    # Muestra el total ahorrado hasta este mes
    print(f"llevas ahorrado hasta este mes: {ahorro}")