# Acumuladores de kilómetros y litros totales
total_km = 0
total_litros = 0

# Ciclo para las 8 etapas del viaje
for i in range(1, 9):
    # Pide los km recorridos y litros consumidos en la etapa
    km = float(input(f"Etapa {i} - km: "))
    litros = float(input(f"Etapa {i} - litros: "))
    # Muestra el rendimiento de la etapa (km entre litros)
    print(f"Etapa {i}: {km/litros:.2f} km/l")
    # Acumula km y litros al total
    total_km += km
    total_litros += litros

# Muestra el total de km recorridos
print(f"Total km: {total_km}")
# Muestra el rendimiento total (km totales entre litros totales)
print(f"Rendimiento total: {total_km/total_litros:.2f} km/l")