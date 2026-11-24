# Capital inicial a invertir
capital = 2000
# Factor de rendimiento anual (8% de interés)
rendimiento = 1.08
# Variable para el acumulado anual (no se usa en el cálculo)
anual_acumulado = 0
# Pide cuántos años se dejará el capital
años = int(input("dime los años a dejar tu capital: "))

# Ciclo para cada año
for i in range(años):
    # Multiplica el capital por el rendimiento (interés compuesto)
    capital = rendimiento * capital

    # Muestra el total acumulado en el año actual
    print(f"total acumulado en el año {i+1}: {capital}")