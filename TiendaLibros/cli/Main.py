from model.Libro import  Libro
from model.ItemCompra import ItemCompra
from model.CarroCompras import CarroCompras

libro1 = Libro("50 sombras de Grey","1020100", 99.99)

print( "El titulo del libro 1 es: "  + libro1.titulo )
print( "El ISBN del libro 1 es: " + libro1.isbn )
print( "El precio del libro 1 es: " + str(libro1.precio) )

libro2 = Libro("Calculus","1020100", 49.99)

print( "El titulo del libro 2 es: "  + libro2.titulo )
print( "El ISBN del libro 2 es: " + libro2.isbn )
print( "El precio del libro 2 es: " + str(libro2.precio) )

if( libro1 == libro2 ):
    print("Los libros son iguales.")
else:
    print("Los libros no son iguales.")


item_compra_1 = ItemCompra( libro2, 10 )

print("El item de compra 1 tiene subtotal: "  + str( item_compra_1.calcular_subtotal() ) )

item_compra_2 = ItemCompra( libro2, 20 )

print("El item de compra 2 tiene subtotal: "  + str( item_compra_2.calcular_subtotal() ) )

if( item_compra_1 == item_compra_2 ):
    print("Los item son iguales.")
else:
    print("Los item no son iguales.")

carrito = CarroCompras()

carrito.adicionar_compra( item_compra_1 )
carrito.adicionar_compra( item_compra_2 )

total_carrito = carrito.calcular_valor_total_compra()

print( "El valor del carrito es: " + str(total_carrito) )

carrito.borrar_item_compra( item_compra_2 )

total_carrito = carrito.calcular_valor_total_compra()

print( "El valor del carrito es: " + str(total_carrito) )


