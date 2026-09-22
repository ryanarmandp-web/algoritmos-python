# Aqui pido minutos, que dia fue y en que turno si no es domingo
minutos = int(input("Duracion de la llamada en minutos: "))
dia = input("Dia de la llamada (domingo / habil): ").lower()
turno = ""
# Solo si no es domingo pregunto el turno, porque domingo no importa
if dia != "domingo":
    turno = input("Turno (matutino / vespertino): ").lower()

# Aqui saco el costo base igual que el ejercicio anterior por bloques
if minutos <= 5:
    costo_base = minutos * 1.00 # 1-5 a $1
elif minutos <= 8:
    costo_base = 5 * 1.00 + (minutos - 5) * 0.80 # 6-8 a $0.80
elif minutos <= 10:
    costo_base = 5 * 1.00 + 3 * 0.80 + (minutos - 8) * 0.70 # 9-10 a $0.70
else:
    costo_base = 5 * 1.00 + 3 * 0.80 + 2 * 0.70 + (minutos - 10) * 0.50 # 11+ a $0.50

# Aqui veo cuanto impuesto toca segun el dia y turno
if dia == "domingo":
    porcentaje_impuesto = 3 # domingo 3%
elif turno == "matutino":
    porcentaje_impuesto = 15 # dia habil en la mañana 15%
else:
    porcentaje_impuesto = 10 # dia habil en la tarde 10%

# Aqui saco cuanto es de impuesto
impuesto = costo_base * (porcentaje_impuesto / 100)
# Y aqui le sumo el impuesto al costo base
total = costo_base + impuesto

# Muestro el ticket con todo
print("\n--- CHISMEFON - CON IMPUESTO ---")
print(f"Costo base de la llamada: ${costo_base:.2f}")
print(f"Impuesto aplicado: {porcentaje_impuesto}%")
print(f"Monto del impuesto: ${impuesto:.2f}")
print(f"Total a pagar: ${total:.2f} MXN")