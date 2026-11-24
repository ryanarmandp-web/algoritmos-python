pena = 0 #acumulador para las penalizaciones
op = int(input("dime la cantidad de facturas a ingresar: ")) #variable para repetir la cantidad de veces que se necesitan
#for para pedir las facturas y separarlas dependiendo la categoria
for i in range(op):
	monto = float(input("dime el monto de la factura: "))
	dias = int(input("dime los dias de atraso: "))
	if dias >30 and dias <61:
		pena += (monto *1.05)-monto 
		monto = monto*1.05
	elif dias > 60:
		pena += (monto *1.12)-monto 
		monto = monto*1.12
#prints para imprimir los montos
	print(f"IMPORTE DE LA factura: {monto:.2f}")

print(F"total de penalizaciones: {pena:.2f}")