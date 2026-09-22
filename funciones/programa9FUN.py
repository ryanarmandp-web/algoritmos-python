#problema 9
def op(a):
	if a<0:
		A="es negativo"
	elif a>0:
		A="es positivo"
	else:
		A="es 0"

	return A

print(op(17))
print(op(0))
print(op(-17)) 