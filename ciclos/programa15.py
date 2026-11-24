# Contador de números pares encontrados
pares = 0
# Variable que guarda el par actual (se reutiliza como número par)
par = 0

# Ciclo del 0 al 99
for i in range(0, 100):
    # Si el número es divisible entre 2, es par
    if i % 2 == 0:
        # Guarda el número par actual
        pares = i
        # Muestra el número par
        print(f"Par :{pares}")
        # Aumenta el contador de pares
        par += 1

# Muestra cuántos números pares se encontraron
print(f"Numeros pares encontrados: {par}")