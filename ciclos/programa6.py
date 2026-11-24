# Acumulador de la suma de números pares
suma = 0
# Lista donde se guardarán los números pares
par = []
# Pide cuántos números se van a ingresar
num = int(input("Dime los numeros que vas a ingresar"))
# Referencia a la lista par (sin efecto)
par

# Ciclo para cada número
for i in range(num):
    # Pide el número actual
    n = int(input(f"dime el numero No.{i+1}: "))
    # Si el número es divisible entre 2, es par
    if n % 2 == 0:
        # Agrega el número par a la lista
        par.append(n)
        # Suma el número par al total
        suma += n

# Muestra la lista de números pares
print(f"numero pares:  {par}")
# Muestra la suma de los números pares
print(f"la suma de los numeros pares es de: {suma}")