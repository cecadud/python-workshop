"""
    Programa de validación sencilla del ejemplo Subasta de Celulares
"""

from model.Celular import Celular
from model.Subasta import Subasta

sub = Subasta()

sub.registrar_oferta_minima_celular_1()
sub.registrar_oferta_moderada_celular_2()
sub.registrar_oferta_moderada_celular_3()
sub.registrar_oferta_abierta_celular_2(100000)

total_ofertas = sub.calcular_numero_total_ofertas()
total_valor_recaudado = sub.calcular_valor_total_recaudado()
incremento_promedio_costo_base = sub.calcular_incremento_promedio_costo_base()

print("El número total de ofertas es: " + str(total_ofertas))
print("El valor total recaudado es: " + str(total_valor_recaudado))
print("El incremento promedio sobre el costo base es : " + str(incremento_promedio_costo_base))

cel1 = sub.celular1
total_ofertas_cel_1 = cel1.numero_ofertas

print("El total de ofertas del celular 1 es: " + str(total_ofertas_cel_1))

print("-----------------------")
print("Reiniciando subasta...")
print("-----------------------")

sub.reiniciar_subasta()

total_ofertas = sub.calcular_numero_total_ofertas()
total_valor_recaudado = sub.calcular_valor_total_recaudado()
incremento_promedio_costo_base = sub.calcular_incremento_promedio_costo_base()
total_ofertas_cel_1 = cel1.numero_ofertas

print("El número total de ofertas es: " + str(total_ofertas))
print("El valor total recaudado es: " + str(total_valor_recaudado))
print("El incremento promedio sobre el costo base es : " + str(incremento_promedio_costo_base))
print("El total de ofertas del celular 1 es: " + str(total_ofertas_cel_1))

