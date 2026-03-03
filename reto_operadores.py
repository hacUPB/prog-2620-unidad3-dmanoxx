edad_usuario = float(input("Ingresa tu edad: "))
saldo_billetera = float(input("Ingresa el saldo de tu billetera: "))
tiene_subscripcion_premium = True if input("¿Tienes una subscripción activa? (si/no): ").lower() == "si" else False
precio_juego = 60

if tiene_subscripcion_premium:
    precio_final = precio_juego * 0.90
else:
    precio_final = precio_juego

compra_exitosa = (edad_usuario >= 17 and saldo_billetera >= precio_final)

print ("Precio final del juego: $", precio_final)
print ("¿La compra fue exitosa?", compra_exitosa)
