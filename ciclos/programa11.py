# Importa el módulo random para generar números aleatorios
import random
# Lista donde se guardarán los pesos de las maletas
peso = []
# Contador de maletas que superan el límite
lim = 0

# Ciclo para 10 maletas
for i in range(10):
    # Genera un peso aleatorio entre 1 y 60
    e = random.randint(1, 60)
    # Agrega el peso a la lista
    peso.append(e)
    # Muestra el peso de la maleta actual
    print(f"peso maleta{i+1}: {peso[i]}")
    # Si el peso supera 23, cuenta como maleta que supera el límite
    if peso[i] > 23:
        lim += 1

# Muestra cuántas maletas superan el límite
print(f"maletas que superan el limite: {lim}")