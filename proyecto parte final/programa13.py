# Acumuladores de piezas por turno, inician en 0
manana = tarde = noche = 0

# Ciclo para los 7 días de la semana
for dia in range(1, 8):
    # Muestra el día actual
    print(f"Día {dia}")
    # Suma las piezas de cada turno al acumulador correspondiente
    manana += int(input("  Mañana: "))
    tarde += int(input("  Tarde: "))
    noche += int(input("  Noche: "))

# Muestra el total de piezas por turno
print(f"Mañana: {manana}, Tarde: {tarde}, Noche: {noche}")

# Compara los totales para encontrar el turno más productivo
if manana >= tarde and manana >= noche:
    # Mañana es mayor o igual que los otros dos
    print("Turno más productivo: Mañana")
elif tarde >= noche:
    # Si no es mañana, compara tarde contra noche
    print("Turno más productivo: Tarde")
else:
    # Si no es ninguno de los anteriores, es noche
    print("Turno más productivo: Noche")