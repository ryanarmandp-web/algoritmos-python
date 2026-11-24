# Acumulador de la suma total
suma = 0

# Ciclo para 5 números
for i in range(5):
    # Pide el número entero actual
    num = int(input(f"Dime el numero entero No{i+1}: "))
    # Suma el número al total
    suma += num

# Muestra la suma total
print(f"suma total: {suma}")