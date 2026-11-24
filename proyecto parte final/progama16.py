# Pide el saldo disponible
saldo = float(input("Saldo disponible: $"))
# Contador de intentos fallidos
intentos = 0
# Bandera para saber si el retiro fue exitoso
exito = False

# Ciclo mientras queden intentos y no haya éxito
while intentos < 3 and not exito:
    # Pide el monto a retirar
    retiro = float(input("Monto a retirar: $"))

    # Si el retiro supera el saldo, cuenta un intento fallido
    if retiro > saldo:
        intentos += 1
        print(f"Saldo insuficiente. Te quedan {3-intentos} intentos")
    else:
        # Si hay saldo suficiente, hace el retiro y marca éxito
        print(f"Retiro exitoso. Nuevo saldo: ${saldo-retiro:.2f}")
        exito = True

# Si después del ciclo no hubo éxito, bloquea la tarjeta
if not exito:
    print("Se agotaron los 3 intentos. Tarjeta bloqueada.")