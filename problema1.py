# Aqui guardo cuanto vale un dolar en pesos, 16.96
dolar=16.96

# Aqui le pido al usuario cuantos pesos quiere convertir
# uso float() porque puede poner decimales
pesos=float(input("dime cuantos pesos quieres convertir a dolares"))

# Aqui hago la conversion, divido los pesos entre lo que vale el dolar
con=pesos/dolar

# Aqui muestro el resultado de la conversion
print(f"De pesos a dolares es  {con}")