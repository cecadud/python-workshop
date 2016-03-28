class Factura:
    """
    Clase que modela una factura del club
    """

    def __init__(self, nombre, concepto, valor):
        """
        Crea una nueva factura asociada al consumo del socio o de un autorizado
        :param nombre: Nombre de quien hizo el consumo
        :param concepto: Concepto del consumo. not None
        :param valor: Valor del consumo
        :return:
        """
        self.__nombre = nombre
        self.__concepto = concepto
        self.__valor = valor

    @property
    def nombre(self):
        """
        Retorna el nombre de quien hizo el consumo
        :return: Nombre de quien generó el consumo
        """
        return self.__nombre

    @property
    def concepto(self):
        """
        Retorna el concepto de la factura
        :return: Concepto de la factura
        """
        return self.__concepto

    @property
    def valor(self):
        """
        Retorna el valor de la factura
        :return: Valor de la factura
        """
        return self.__valor

    def __str__(self):
        """
        Retorna la representación en cadena de la factura
        :return Cadena de caracteres que representa la factura en formato <concepto>  $<valor>  (<nombre>)
        """
        return self.__concepto + "   $" + self.__valor + "  (" + self.__nombre + ")"