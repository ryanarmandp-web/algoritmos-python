# Aqui le pido al usuario el año en que nacio el trabajador
# lo convierto a entero con int() porque lo necesito para restar
año=int(input("dime el año de nacimiento del trabajador"))

# Aqui guardo el año actual, en este caso 2026
añoac=2026

# Aqui saco la edad, resto el año actual menos el año que nacio
edad=2026-año

# Aqui muestro en pantalla la edad que me dio
print(f"la edad de tu trabajador es {edad}")