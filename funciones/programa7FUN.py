# funcion que dice si es mayor de edad

def es_mayor_de_edad(edad):
    # recibe la edad
    if edad >= 18:
        return "Mayor" # si tiene 18 o mas es mayor
    else:
        return "Menor" # si no, es menor

# pruebas
print(es_mayor_de_edad(17)) # deberia dar "Menor"
print(es_mayor_de_edad(18)) # deberia dar "Mayor"
print(es_mayor_de_edad(45)) # deberia dar "Mayor"