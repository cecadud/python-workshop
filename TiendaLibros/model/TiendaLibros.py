from model.CarroCompras import CarroCompras

class TiendaLibros:
    """
    Tienda de venta de libros
    """

    def __init__(self):
        """
        Crea la tienda con el catálogo de libros vacío
        """
        self.__catalogo = []
        self.__carrito = CarroCompras()

    def buscar_libro(self,isbn):
        """
        Retorna un libro del catálogo de la tienda con el ISBN dado
        :param isbn: ISBN del libro a buscar en el catálogo
        :return: Libro encontrado o None si no existe
        """
        pass

    @property
    def carro_compras(self):
        """
        Retorna el carro de compras
        :return: Carro de compras
        """
        return self.__carrito

    @property
    def catalogo(self):
        """
        Retorna el catálogo de la tienda
        :return: Catálogo de la tienda
        """
        return self.__catalogo

    def crear_nueva_compra(self):
        """
        Crea una nueva compra (un carrito vacío)
        """
        pass

    def adicionar_libro_catalogo(self, nuevoLibro):
        """
        Adiciona un nuevo libro al catálogo de la tienda si el libro no existe ya
        :param nuevoLibro: Nuevo libro del catálogo. not None
        :return:
        """
        pass