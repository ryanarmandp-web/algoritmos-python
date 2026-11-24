# Pide de qué número se quiere la tabla de multiplicar
tabla = int(input("Dime de que numero ocupas la tabla de multiplicar: "))

# Ciclo del 1 al 10
for i in range(10):
    # Muestra la multiplicación actual
    print(f"{tabla}x{i+1}={tabla*(i+1)}")