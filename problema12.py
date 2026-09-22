# Aqui pido cuantas personas van a ir al evento
# y lo convierto a numero entero con int() porque input siempre regresa texto
personas = int(input("Numero de personas para el evento: "))

# Si son 200 o menos, el platillo sale mas caro porque son poquitos
if personas <= 200:
    costo_platillo = 95.00
# Si no son 200 pero son 300 o menos, baja un poco el precio
elif personas <= 300:
    costo_platillo = 85.00
# Si ya son mas de 300, es el precio mas barato por mayoreo
else:
    costo_platillo = 75.00

# Aqui saco el total, multiplico personas por lo que cuesta cada platillo
presupuesto = personas * costo_platillo

# Esto ya es nomas para mostrar bonito el ticket en pantalla
print("\n--- LA LANGOSTA AHUMADA ---")
print(f"Numero de personas: {personas}") # muestro cuantas personas puso el usuario
print(f"Costo por platillo: ${costo_platillo:.2f}") # muestro cuanto cuesta cada uno con 2 decimales
print(f"Presupuesto total: ${presupuesto:.2f}") # muestro el total ya calculado