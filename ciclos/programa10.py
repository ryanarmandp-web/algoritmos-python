# Importa el módulo random para generar números aleatorios
import random
# Lista donde se guardarán las edades
edad = []
# Contador de menores de edad
men = 0

# Ciclo para 8 personas
for i in range(8):
    # Genera una edad aleatoria entre 1 y 100
    e = random.randint(1, 100)
    # Agrega la edad a la lista
    edad.append(e)
    # Muestra la edad registrada
    print(f"edad registrada No.{i+1}:{edad[i]}")
    # Si la edad es menor que 17, cuenta como menor de edad
    if edad[i] < 17:
        men += 1

# Muestra cuántos menores de edad se registraron
print(f"Menores de edad registrados:{men}")