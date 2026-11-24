# Pide cuántos estudiantes se van a registrar
n = int(input("¿Cuántos estudiantes? "))
# Contadores por categoría y acumulador de calificaciones
reprobados = aprobados = excelencia = 0
suma = 0

# Ciclo para cada estudiante
for i in range(n):
    # Pide la calificación del estudiante
    cal = float(input(f"Calificación {i+1}: "))
    # Acumula la calificación para el promedio
    suma += cal

    # Clasifica según la calificación
    if cal < 6.0:
        # Menos de 6.0: reprobado
        reprobados += 1
    elif cal < 9.0:
        # De 6.0 a 8.99: aprobado
        aprobados += 1
    else:
        # 9.0 o más: excelencia
        excelencia += 1

# Muestra el total por categoría
print(f"Reprobados: {reprobados}")
print(f"Aprobados: {aprobados}")
print(f"Excelencia: {excelencia}")
# Muestra el promedio general (suma entre total de estudiantes)
print(f"Promedio general: {suma/n:.2f}")