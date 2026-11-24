# Meta de ahorro a alcanzar
meta = 12000
# Acumulador del total ahorrado
total = 0
# Lista con los nombres de los 12 meses
mes = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

# Ciclo para los 12 meses
for i in range(12):
    # Pide el ahorro del mes actual
    ahorro = float(input(f"Dime lo que vas a ingresar en {mes[i]}: "))
    # Acumula el ahorro al total
    total += ahorro

    # Esta condición nunca se cumple porque i va de 0 a 11
    if(i == 12):
        # Muestra el total ahorrado (nunca se ejecuta)
        print(f"En total ahorraste: {total}")
        break
    else:
        # Muestra el acumulado hasta el mes actual
        print(f" {mes[i]} llevas acumulado: {total}")

# Compara el total ahorrado con la meta
if total > meta:
    # Si superó la meta, muestra por cuánto la superó
    print(f"superate la meta de {meta} por la cantidad de: ${total-meta:.2f} ")
else:
    # Si no llegó, muestra cuánto faltó
    print(f"te falto ${meta-total:.2f} para superar la meta")