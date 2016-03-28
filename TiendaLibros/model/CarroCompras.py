from model.ItemCompra import ItemCompra

class CarroCompras:

    """
    Carrito de compras de libros. Almacena los libros que el cliente quiere comprar.
    """

    def __init__(self):
        """
        Crea un carro de compras vacío
        """
        self.__items_compra = []

    def adicionar_compra(self, libro, cantidad):
        """
        Adiciona un nuevo ítem al carro de compras
        :param libro: Libro a comprar
        :param cantidad: Cantidad de libros a comprar. >0
        """
        item_compra = ItemCompra( libro, cantidad )
        self.__items_compra.append(item_compra)

    def adicionar_compra(self, item):
        """
        Adiciona un nuevo ítem al carro de compras.
        :param item: Ítem a adicionar
        """
        self.__items_compra.append(item)

    def borrar_item_compra(self, item_compra ):
        """
        Borra un ítem del carro de compras
        :param item_compra: Ítem a eliminar
        """
        self.__items_compra.remove( item_compra )

    def buscar_item_compra(self, isbn):
        """
        Determina si existe un item de compra cuyo ISBN sea el dado por parámetro
        :param isbn: ISBN del libro buscado
        :return: Ítem de compra del libro o None si no lo encuentra
        """
        item_buscado = None

        for item in self.__items_compra:
            if( item.libro.isbn == isbn  ):
                item_buscado = item

        return item_buscado

    def calcular_valor_total_compra(self):
        """
        Calcula el total de la compra que lleva el carrito
        :return: Total de la compra
        """
        total = 0.0

        for item in self.__items_compra:
            total += item.calcular_subtotal()

        return total

    @property
    def items_compra(self):
        """
        Retorna la lista de los ítems de compra
        :return: Lista de los ítems de compra
        """
        return self.__items_compra