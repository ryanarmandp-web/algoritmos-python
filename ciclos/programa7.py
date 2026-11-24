# Importa el módulo random para generar números aleatorios
import random

# Contador de menores de edad
men = 0
# Genera una edad aleatoria inicial (se sobrescribe en el ciclo)
edades = random.randint(1, 100)

# Ciclo para 8 personas
for i in range(8):
    # Genera una edad aleatoria entre 1 y 100
    edades = random.randint(1, 100)
    # Muestra la edad generada
    print(f"edad {i+1}:{edades}")
    # Si la edad es menor o igual que 17, cuenta como menor de edad
    if edades <= 17:
        men += 1

# Muestra cuántas personas menores se registraron
print(f"persona menores: {men}")