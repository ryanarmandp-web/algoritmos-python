# Aqui pido cuantos minutos duro la llamada
minutos = int(input("Duracion de la llamada en minutos: "))

costo = 0 # aqui voy a guardar lo que va a pagar, empieza en 0

# Si hablo 5 minutos o menos, cada minuto cuesta $1.00
if minutos <= 5:
    costo = minutos * 1.00

# Si hablo entre 6 y 8 minutos, los primeros 5 son a $1 y los que sobran a $0.80
elif minutos <= 8:
    costo = 5 * 1.00 + (minutos - 5) * 0.80

# Si hablo entre 9 y 10 minutos, ya suma 5 a $1, 3 a $0.80 y lo que sobra a $0.70
elif minutos <= 10:
    costo = 5 * 1.00 + 3 * 0.80 + (minutos - 8) * 0.70

# Si se paso de 10 minutos, todo lo demas se cobra a $0.50 el minuto
else:
    costo = 5 * 1.00 + 3 * 0.80 + 2 * 0.70 + (minutos - 10) * 0.50

# Aqui muestro el ticket
print("\n--- CHISMEFON - COBRO POR TIEMPO ---")
print(f"Minutos hablados: {minutos}")
print(f"Total a pagar: ${costo:.2f} MXN")