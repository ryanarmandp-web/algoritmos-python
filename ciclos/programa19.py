# --- Inicialización de variables ---
salario = 1500      # Salario base inicial
a = 2026            # Año inicial (año 0)
total_acumulado = 0 # Variable para sumar lo ganado en los 6 años

print(f"Salario inicial en {a}: {salario}")

# --- Proceso ---
# range(6) repetirá el proceso para 2027, 2028, 2029, 2030, 2031, 2032
for i in range(6):
    a += 1  # Avanza un año
    salario += salario * 0.10  # Aplica el aumento del 10% (salario = salario * 1.10)
    
    total_acumulado += salario # Suma el salario de ese año al total

    print(f"Tu salario el año {a} es: {round(salario, 3)}")

# --- Salida final ---
print(f"\nSalario final después de 6 años: {round(salario, 3)}")
print(f"Total acumulado en los 6 años: {round(total_acumulado, 3)}")