#problema 12
def calificar(nota):#FUncion calificar(variable)

	if nota>=90 and nota<=100:#if para la nota A si la cal es >=90 y <=100
		print("A")#imprime calificacion A
	elif nota>=80 and nota<=89:#if para la nota b si la cal es >=80 y <=89
		print("b")#imprime calificacion b
	elif nota>=70 and nota<=79:#if para la nota c si la cal es >=70 y >=79
		print("c")#imprime calificacion c
	else:#else si no se cumplen las condiciones 
		print("F")#imprime cal F si no se cumplieron las calificaciones 
f=int(input("Dame tu calificacion: "))#aqui pido la calificacion
calificar(f)#aqui llamo la funcion 



