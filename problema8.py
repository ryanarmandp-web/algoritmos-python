# Aqui pido el precio del traje, uso float por si tiene decimales
precio_original = float(input("Precio del traje: "))

# Si el traje cuesta mas de 2500 le hago mas descuento
if precio_original > 2500.00:
    porcentaje = 15 # 15% de descuento
else:
    porcentaje = 8 # si cuesta menos, solo 8% de descuento

# Aqui saco cuanto es el descuento, precio * porcentaje entre 100
descuento = (precio_original * porcentaje) / 100

# Aqui le resto el descuento al precio original para sacar el final
precio_final = precio_original - descuento

# Todo esto es para mostrar el ticket bonito
print("\n--- ALMACENES EL HARAPIENTO DISTINGUIDO ---")
print(f"Precio original: ${precio_original:.2f}") # muestro el precio sin descuento
print(f"Descuento aplicado: {porcentaje}%") # muestro que porcentaje le toco
print(f"Monto del descuento: ${descuento:.2f}") # muestro cuanto dinero se le desconto
print(f"Precio final a pagar: ${precio_final:.2f}") # muestro ya lo que va a pagar