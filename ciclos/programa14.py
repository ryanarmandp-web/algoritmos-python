# Contador de cantidades mayores que 0
may = 0
# Contador de cantidades menores o iguales que 0
men_igual = 0
# Variable que guarda la cantidad actual
cant = 0
# Pide cuántas cantidades se van a ingresar
op = int(input("ingrese el numero de cantitades a ingresar"))

# Ciclo para cada cantidad
for i in range(op):
    # Pide la cantidad actual
    cant = float(input(f"ingrese la cantidad numero {i+1}: "))
    # Si es mayor que 0, cuenta como positiva
    if cant > 0:
        may += 1
    # Si no, cuenta como menor o igual que 0
    else:
        men_igual += 1

# Muestra cuántas cantidades fueron mayores que 0
print(f"Numero de cantidades mayores que 0: {may}")

# Muestra cuántas cantidades fueron menores o iguales que 0
print(f"Numero de cantidades menores o iguales que 0: {men_igual}")