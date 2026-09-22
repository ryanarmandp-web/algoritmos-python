#problema 10
# Aqui pido cuantos lapices va a comprar el usuario
lap=int(input("dime la cantidad de lapices a comprar: "))

# Si compra 1000 o mas lapices le dejo mas barato
if(lap>=1000):
    # Aqui multiplico por 0.85 porque cada lapiz sale en 85 centavos
    pre=lap*.85
    print(f"el pago final es de:_{pre}")
else:
    # Si compra menos de 1000 sale en 90 centavos cada uno
    pre=lap*.9
    print(f"el pago final es de:_{pre}")