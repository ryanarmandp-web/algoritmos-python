#problema 4
# Aqui guardo cuanto cuesta cada kilometro, vale 80 pesos
km=80

# Aqui pido cuantos kilometros quiere recorrer la persona
# lo convierto a entero con int()
kmr=int(input("Dime los kilometros a recorrer: "))

# Aqui saco el total del boleto, multiplico precio por kilometro por los kilometros
bol=km*kmr

# Aqui muestro cuanto le va a costar el boleto
print(f"EL precio del boleto es de: {bol}")