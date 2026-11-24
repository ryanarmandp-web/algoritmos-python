# Pide cuántas personas se van a clasificar
n = int(input("¿Cuántas personas? "))
# Contadores para cada grupo de edad, inician en 0
ninos = adolescentes = adultos = mayores = 0

# Ciclo para cada persona
for i in range(n):
    # Pide la edad de la persona
    edad = int(input(f"Edad {i+1}: "))

    # Clasifica según el rango de edad
    if edad <= 12:
        # Hasta 12 años: niño
        ninos += 1
    elif edad <= 17:
        # De 13 a 17 años: adolescente
        adolescentes += 1
    elif edad <= 59:
        # De 18 a 59 años: adulto
        adultos += 1
    else:
        # 60 años o más: adulto mayor
        mayores += 1

# Muestra el total de personas por grupo
print(f"Niños: {ninos}, Adolescentes: {adolescentes}, Adultos: {adultos}, Adultos mayores: {mayores}")