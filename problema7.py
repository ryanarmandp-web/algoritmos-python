#problema 7
# Aqui pido que producto quiere, 1 para agua y 2 para pepsi
producto=int(input("dime que quieres comprar (1)agua $18 o (2)pepsi $24: "))

# Si escogio 1, es agua
if producto==1:
    # Aqui le aplico el descuento del 20%, por eso multiplico por 0.8
    precio=18*.8
    # Aqui le sumo el iva del 16%, por eso multiplico por 1.16
    iva=precio*1.16
    print("agua precio 18")
    # Muestro el precio ya con descuento y con iva
    print(f"el pago con iva y descuento es de: {iva}")
    # Muestro el precio solo con el descuento, sin iva
    print(f"el pago con descuento es de: {precio}")

# Si escogio 2, es pepsi
if producto==2:
    # Igual le aplico el 20% de descuento
    precio=24*.8
    # Y le aplico el iva del 16%
    iva=precio*1.16
    print("pepsi precio 24")
    print(f"el pago con iva y descuento es de: {iva}")
    print(f"el pago con descuento es de: {precio}")