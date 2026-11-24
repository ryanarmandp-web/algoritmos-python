nven = int(input("dime el numero de ventas este dia")) # Pide el numero total de ventas del dia
may1000 = 0 # Contador para ventas mayores a 1000
ma5o1 = 0 # Contador para ventas mayores a 500 y menores o iguales a 1000
men = 0 # Contador para ventas menores o iguales a 500
n1 = 0 # Acumulador del monto total de ventas mayores a 1000
n2 = 0 # Acumulador del monto total de ventas entre 501 y 1000
n3 = 0 # Acumulador del monto total de ventas menores o iguales a 500
total = 0 # Acumulador del monto total de todas las ventas
ven= 0 # Variable temporal para guardar el valor de cada venta
for i in range(nven): # Inicia ciclo que se repite segun el numero de ventas
	ven = float(input(f"Venta numero {i+1}: ")) # Pide el monto de la venta actual
	if ven>1000: # Si la venta es mayor a 1000
		may1000 += 1 # Incrementa el contador de ventas mayores a 1000
		n1 += ven # Suma el monto al acumulador de esa categoria
	elif ven >500 and ven <=1000: # Si la venta esta entre 501 y 1000
		ma5o1 += 1 # Incrementa el contador de ventas intermedias
		n2 += ven # Suma el monto al acumulador de esa categoria
	else: # Si no se cumple lo anterior, la venta es de 500 o menos
		men +=1 # Incrementa el contador de ventas bajas
		n3 += ven # Suma el monto al acumulador de esa categoria

	total +=ven # Suma cada venta al total general

print(F"Ventas totales mayores a 1000: {may1000}") # Imprime cantidad de ventas mayores a 1000
print(F"total de esta categoria: ${n1}") # Imprime el monto total de ventas mayores a 1000
print(f"ventas totales mayores que 500 y menores a 1001: {ma5o1}") # Imprime cantidad de ventas entre 501 y 1000
print(f"total de esta categoria: ${n2}") # Imprime el monto total de ventas entre 501 y 1000
print(F"ventas totales menores a 501: {men}") # Imprime cantidad de ventas menores o iguales a 500
print(f"total de esta categoria: ${n3}") # Imprime el monto total de ventas menores o iguales a 500