# problema 10 - calculadora con opciones

# funcion op que recibe dos numeros A y B y que operacion quiere hacer
def op(A,B,ope):
    if ope==1:
        res=A+B # si ope es 1 suma
    elif ope==2:
        res=A-B # si es 2 resta
    elif ope==3:
        res=A*B # si es 3 multiplica
    elif ope==4:
        if B==0:
            res="no se puede dividir entre 0" # no se puede dividir entre 0
        else:
            res=A/B # si es 4 divide
    else:
        res="no hay resultado operacion no valida"; # si pone otro numero no valido
    
    return res # regreso el resultado

# aqui pruebo todas
print("el res es: ",op(12,2,1))	# 12+2 = 14
print("el res es: ",op(12,2,2))	# 12-2 = 10
print("el res es: ",op(12,2,3))	# 12*2 = 24
print("el res es: ",op(12,2,4))	# 12/2 = 6
print(op(12,2,5)) # operacion no valida