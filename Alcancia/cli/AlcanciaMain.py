"""
    Programa de validación sencilla del ejemplo Alcancia
"""

from model.Alcancia import Alcancia

alcancia = Alcancia()   # Crear una nueva alcancía

alcancia.agregar_moneda_50()    # Agregar una moneda de 50
alcancia.agregar_moneda_100()   # Agregar una moneda de 100
alcancia.agregar_moneda_100()   # Agregar otra moneda de 100
alcancia.agregar_moneda_1000()  # Agregar una moneda de 1000

alcancia.agregar_monedas_50(10) # Agregar 10 monedas de 50 utilizando método modificador

numero_monedas_50 = alcancia.numero_monedas_50   # Obtener el número de monedas de 50

total = alcancia.dar_total_dinero() # Obtener el total de dinero depositado en la alcancía

print("El total de dinero en la alcancía es: " + str(total) + " y hay " + str(numero_monedas_50) + " monedas de 50.")

alcancia.romper_alcancia()  # Romper la alcancía
total = alcancia.dar_total_dinero() # Obtener el total

msj_esta_rota = " y la alcalcía está rota." # Definir un mensaje para informar si está rota o no

if( not alcancia.esta_rota ):
    msj_esta_rota = " y la alcancía no está rota."

print("El total de dinero en la alcancía es: " + str(total) + msj_esta_rota)

