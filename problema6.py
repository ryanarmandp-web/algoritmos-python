#problema6
# Aqui guardo cuanto cuesta el minuto de llamada, 3 pesos
t=3

# Aqui pido cuanto tiempo duro la llamada en minutos
# lo convierto a entero
tiempo= int(input("dime cuanto tiempo dura tu llamada: "))

# Aqui multiplico los minutos por lo que cuesta cada minuto
costo=tiempo*t 

# Aqui muestro cuanto salio la llamada
print(f"el costo de tu llamada es de: {costo}")