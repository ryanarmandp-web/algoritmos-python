nivel = 0
capacidad = 1000

while True:  # Ciclo infinito, solo se rompe con break
    volumen = float(input("Litros ingresados (0 para terminar): "))
    
    if volumen == 0:  # Condición de salida manual
        break
    
    nivel += volumen  # Acumulador: suma lo ingresado al nivel actual
    print(f"Nivel actual: {nivel} L")
    
    if nivel >= capacidad:  # Tanque lleno o rebasado
        print("¡ALERTA! Tanque lleno")
        break  # Se detiene el llenado
    
    elif nivel >= 900:  # 90% de la capacidad, casi lleno
        print("Alerta: Casi lleno")