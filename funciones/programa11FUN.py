# Problema 11 - mayor_de_tres
def mayor_de_tres(a, b, c):  # recibe 3 números
    if a >= b and a >= c:  # si a es el mayor
        return a  # regresa a
    if b >= a and b >= c:  # si b es el mayor
        return b  # regresa b
    if c >= a and c >= b:  # si c es el mayor
        return c  # regresa c

# Pruebas problema 11
print(mayor_de_tres(5, 12, 9))  # 12
print(mayor_de_tres(20, 3, 1))  # 20
print(mayor_de_tres(4, 4, 4))  # 4