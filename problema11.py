#problema 11
# Aqui pido el primer numero
a=float(input("dame el num1 "))
# Aqui pido el segundo numero
b=float(input("dame el num1 "))
# Aqui pido el tercer numero
c=float(input("dame el num1 "))

# Si a es mas grande que b y tambien mas grande que c, entonces a es el mayor
if(a>b and a>c):
    print(f"{a}es mayor")
# Si no, reviso si b es mas grande que a y que c
elif(b>a and b>c):
    print(f"{b}es mayor")
# Si no, reviso si c es mas grande que a y que b
elif(c>a and c>b):
    print(f"{c}es mayor")
# Si ninguno es mas grande que otro, es porque todos son iguales
elif(b==c and a==c):
    print("todos son iguales")