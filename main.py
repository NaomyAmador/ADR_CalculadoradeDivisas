def exchange_money(dinero_original, tasa_de_cambio):
    moneda_extrangera = dinero_original / tasa_de_cambio
    return moneda_extrangera

#Interacción con el usuario para conseguir datos
input("¡Bienvenido/a Viajero a la Calculadora de Divisas!")

dinero_original = float(input("Ingrese la cantidad de dinero que desea cambiar: "))
tasa_de_cambio = float(input("Ahora, ingrese la tasa de cambio del país: "))

resultado = exchange_money(dinero_original, tasa_de_cambio)
print("El equivalente de la moneda extrajera elegida es: ", resultado)

#Tasa de Cambio de monedas extrangeras para probar el programa
#Colombia: 1 USD = 0.000265
#Mexico: 1 USD = 0.059
#Reino Unido: 1 USD = 0.787

#Forma simple de hacerlo
#print(exchange_money(400, 0.000265))