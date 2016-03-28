from model.Libro import Libro

class ItemCompra:

    """
    Ítem del carrito de compras. El ítem indica el libro y la cantidad que se compra del mismo
    """
    def __init__(self, libro, cantidad=1 ):
        """
        Crea un ítem de compra con el ítem a comprar y la cantidad deseada
        :param libro: Libro que se va a comprar
        :param cantidad: Cantidad de libros a comprar
        """
        self.__cantidad = cantidad
        self.__libro = libro

    @property
    def libro(self):
        """
        Retorna el libro solicitado como ítem de compra
        :return: Libro a comprar
        """
        return self.__libro

    @property
    def cantidad(self):
        """
        Retorna la cantidad solicitada de libros
        :return: Cantidad solicitada
        """
        return self.__cantidad

    def dar_isbn_item(self):
        """
        Retorna el ISBN del libro que es el ítem de compra
        :return: ISBN del libro ítem de compra
        """
        return self.__libro.isbn

    def cambiar_cantidad(self, nueva_cantidad):
        """
        Cambia la cantidad de libros solicitados en la compra
        :param nueva_cantidad: Nueva cantidad de libros a comprar
        """
        self.__cantidad = nueva_cantidad

    def calcular_subtotal(self):
        """
        Retorna el subtotal o valor de compra del ítem.
        :return: Cantidad calculada del valor del ítem de compra
        """
        return self.__cantidad*self.__libro.precio

    def __eq__(self,other):
        """
        Indica si este ítem de compra es igual a otro
        :param other: Otro ítem de compra a comparar
        :return: True si son el mismo ítem de compra. False en caso contrario.
        """
        return self.__cantidad == other.cantidad and self.__libro == other.libro

    def __str__(self):
        """
        Retorna la representación en cadena de caracteres del ítem de compra
        :return: Cadena de caracteres en formato <libro>=>cantidad
        """
        return str(self.__libro) + "=>" + self.__cantidad