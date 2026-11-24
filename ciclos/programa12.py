# Pide cuántos números se van a introducir
num = int(input("dime la cantida de numeros a introducir: "))
# Contador de números mayores que 0
may = 0
# Contador de números menores o iguales que 0
men_igu = 0

# Ciclo para cada número
for i in range(num):
    # Pide el número actual
    n = float(input(f"Dime el numero No{i+1}: "))
    # Si es menor o igual que 0, cuenta como menor o igual
    if (n <= 0):
        men_igu += 1
    # Si no, es mayor que 0
    else:
        may += 1

# Muestra cuántos números fueron mayores que 0
print(f"numeros mayores a 0: {may}")
# Muestra cuántos números fueron menores o iguales que 0
print(f"numeros menores a 0: {men_igu}")