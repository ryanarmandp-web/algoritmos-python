#problema9
# Aqui pido la calificacion del primer examen
ex1=float(input("dime tu primer examen: "))
# Aqui pido la del segundo examen
ex2=float(input("dime tu segundo examen: "))
# Aqui pido la del tercer examen
ex3=float(input("dime tu tercer examen: "))

# Aqui sumo los dos primeros examenes y les saco el 25% de cada uno
# osea el .25 es el porcentaje que vale
prom1=.25*(ex1+ex2)

# El tercer examen vale mas, vale 50% por eso lo multiplico por .50
prom2=ex3*.50

# Aqui sumo todo para sacar el promedio final
prom=prom1+prom2

# Aqui muestro el promedio final y cuanto valio cada parte
print(f"prom final {prom} ponderaciones 50%:{prom2} 25%:{prom1}")