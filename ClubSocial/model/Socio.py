class Socio:
    """
    Clase que modela un socio del club
    """

    def __init__(self, cedula, nombre):
        """
        Crea un nuevo socio del club
        :param cedula: Cédula del nuevo socio
        :param nombre: Nombre del nuevo socio
        :return:
        """
        self.__cedula = cedula
        self.__nombre = nombre
        self.__facturas = []
        self.__autorizados = []

    @property
    def cedula(self):
        """
        Retorna la cédula del socio
        :return: Cédula del socio
        """
        return self.__cedula

    @property
    def nombre(self):
        """
        Retorna el nombre del socio
        :return: Nombre del socio
        """
        return self.__nombre

    def agregar_autorizado(self,nombre_autorizado):
        """
        Agrega una nueva persona autorizada a un socio.
        :param nombre_autorizado: Nombre de la nueva persona autorizada para un socio
        :raise AutorizadoYaExisteError si el autorizado ya existía en la lista de autorizados del socio
        :raise MismoSocioError si el nombre del autorizado es igual al del socio
        """
        pass

    def eliminar_autorizado(self, nombre_autorizado):
        """
        Elimina el autorizado del socio con el nombre dado
        :param nombre_autorizado: Nombre del autorizado
        :return:
        """
        pass

    def existe_autorizado(self, nombre_autorizado):
        """
        Indica si un nombre dado por parámetro pertenece a la lista de autorizados del socio
        :param nombre_autorizado: Nombre del autorizado
        :return: True si el nombre corresponde a un autorizado de la lista. False en caso contrario.
        """
        pass

    @property
    def autorizados(self):
        """
        Retorna la lista de autorizados por el socio
        :return: Lista con los nombres de los autorizados por el socio
        """
        return self.__autorizados

    @@property
    def facturas(self):
        """
        Retorna la lista de facturas del socio
        :return: Lista de facturas pendientes de pago del socio
        """
        return self.__facturas

    def pagar_factura(self,indice):
        """
        Paga una factura del socio. Cuando una factura se paga, desaparece de la lista de facturas.
        :param indice: Índice de factura que se quiere eliminar
        """

    def registrar_consumo(self, nombre, concepto, valor):
        """
        Registra un nuevo consumo del socio realizado por él o por uno de sus autorizados
        :param nombre: Nombre de quien realiza el consumo
        :param concepto: Descripción del consumo
        :param valor: Valor del consumo
        :return:
        """
        pass

