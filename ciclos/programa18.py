import random # Importa la libreria random para generar numeros aleatorios
sueldo=0 # Inicializa la variable sueldo del dia en 0
sueldo1=0 # Inicializa la variable sueldo1 que acumula el total de la semana en 0
dia = ["lunes","martes","miercoles","jueves","viernes","sabado"] # Lista con los nombres de los dias de la semana
for i in range(6): # Inicia un ciclo for que se repetira 6 veces (0 a 5) para cada dia
	horas= random.randint(1,7) # Genera un numero aleatorio de horas entre 1 y 7
	print(f"horas trabajadas: {horas}") # Imprime las horas trabajadas generadas
	sueldo1 += 31*horas # Calcula el pago del dia (31 por hora) y lo suma al total acumulado
	sueldo = 31*horas # Calcula el pago solo del dia actual
	print(f"sueldo dia {dia[i]}: {sueldo}") # Imprime el sueldo del dia segun el nombre de la lista dia[i]

print(f"sueldo total:{sueldo1}") # Imprime el sueldo total acumulado de la semana