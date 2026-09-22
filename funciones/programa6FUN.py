# problema6 - cual es mayor

# funcion que compara dos numeros a y b
def mayor(a,b):
    if a>b:
        A=a # si a es mas grande, guardo a en A
    else:
        A=b # si no, guardo b en A (tambien si son iguales)

    return A # regreso el mas grande

print(mayor(15,27)) # deberia dar 27
print(mayor(40,-10)) # deberia dar 40 - este en tu codigo tenia un tab de mas
print(mayor(8,8)) # da 8 porque son iguales