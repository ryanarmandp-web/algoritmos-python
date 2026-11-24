# Contador de números pares encontrados
pares = 0
# Contador auxiliar de números pares
par = 0

# Ciclo del 1 al 19
for i in range(1, 20):
    # Si el número es divisible entre 2, es par
    if i % 2 == 0:
        # Guarda el número par actual
        pares = i
        # Muestra el número par
        print(f"Par :{pares}")
        # Incrementa el contador de pares
        par += 1

# Muestra cuántos números pares se encontraron
print(f"Numeros pares encontrados: {par}")