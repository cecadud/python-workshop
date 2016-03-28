class Libro:

    """
    Representa un libro en la tienda de libros
    """

    def __init__(self, titulo, isbn, precio):
        """
        Crea un libro con su información básica: título, ISBN y precio
        :param titulo: Título del libro. != None
        :param isbn: ISBN del libro. != None
        :param precio: Precio del libro. >= 0
        :return:
        """
        self.__titulo = titulo
        self.__isbn = isbn
        self.__precio = precio

    @property
    def titulo(self):
        """
        Retorna el título del libro
        :return: Título del libro
        """
        return self.__titulo

    @property
    def isbn(self):
        """
        Retorna el ISBN del libro
        :return: ISBN del libro
        """
        return self.__isbn

    @property
    def precio(self):
        """
        Retorna el precio del libro
        :return: Precio del libro
        """
        return self.__precio

    def __eq__(self, other):
        """
        Determina si este libro es igual a otro
        :param other: Otro libro con el que se compara este
        :return: True si los dos ISBN son iguales. False en caso contrario.
        """
        return self.__isbn == other.isbn

    def __str__(self):
        """
        Retorna la representación en cadena de caracteres del libro
        :return: Representación en formato <titulo>:<ISBN>:<precio>
        """
        return self.__titulo + ":" + self.__isbn + ":" + self.__precio

