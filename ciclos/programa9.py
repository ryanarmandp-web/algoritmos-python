# Contador de maletas que superan el límite
lim = 0

# Ciclo para 10 maletas
for i in range(10):
    # Pide el peso de la maleta actual
    peso = int(input(f"ingresa el peso de la maleta No.{i+1}:"))
    # Si el peso supera 23, cuenta como maleta que supera el límite
    if peso > 23:
        lim += 1

# Muestra cuántas maletas superan el límite
print(f"maletas que superan el limite:{lim}")