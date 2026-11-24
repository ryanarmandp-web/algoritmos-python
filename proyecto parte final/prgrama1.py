nomina = 0 #variable para nomina (acumulador)
horas_extras = 0 #acumulador para horas extras
dias = ["lunes","martes","miercoles","jueves","viernes","sabado"]
horas = 0 #acumulador para horas trabajadas normales
sueldo = 20
for i in range(6):#ciclo for para pedir las horas trabajadas
	h = int(input(f"dime las horas trabajadas el dia {dias[i]}: "))
	if h > 8:
		horas_extras += h-8	
	else:
		horas += h
 	

nomina = (sueldo*horas)+(sueldo*horas_extras*2)#calculo para obtener la nomina 
#prints para mostras la horas trabjadas y la nomina
print(F"horas extras trabajadas: {horas_extras}")
print(F"horas trabajadas: {horas}")
print(F"nomina: {nomina}")
