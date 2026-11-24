# Acumulador de la suma total
suma = 0
# Pide cuántos números enteros se van a ingresar
ca = int(input("Dime la cantidad de numeros enteros a ingresar"))

# Ciclo para cada número
for i in range(ca):
    # Pide el número entero actual
    num = int(input(f"Dime el numero entero No{i+1}: "))
    # Suma el número al total
    suma += num

# Muestra la suma total
print(f"suma total: {suma}")