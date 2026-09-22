# Importo la libreria math porque voy a ocupar math.ceil para redondear hacia arriba
import math 

# Aqui pido cuantos minutos estuvo en el estacionamiento
# lo paso a entero con int()
mines=int(input("cuanto tiempo tiene de estancia"))

# Aqui guardo el precio, cada hora cuesta 20 pesos
pre=20

# Aqui convierto minutos a horas y con ceil lo redondeo hacia arriba
# osea si son 61 minutos lo cuenta como 2 horas
red=math.ceil(mines/60)

# Aqui saco el total, multiplico el precio por las horas redondeadas
co=pre*red

# Aqui muestro cuanto tiene que pagar
print(f"su pago es de: {co}")