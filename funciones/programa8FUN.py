# Problema 8 - area_triangulo
def area_triangulo(base, altura):  # recibe base y altura
    if base > 0 and altura > 0:  # valida que sean mayores a 0
        return (base * altura) / 2  # fórmula del área
    else:  # si no son válidos
        return 0  # regresa 0