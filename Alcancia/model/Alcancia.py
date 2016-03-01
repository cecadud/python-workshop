
class Alcancia:

    """
    Clase que representa una alcancía
    """

    def __init__(self):
        self.inicializar()

    def agregar_moneda_50(self):

        """
        Agrega una moneda de 50 pesos a la alcancía. La alcancía no está rota.
        """

        self.__numero_monedas_50 += 1

    def agregar_moneda_100(self):

        """
        Agrega una moneda de 100 pesos a la alcancía. La alcancía no está rota.
        """

        self.__numero_monedas_100 += 1

    def agregar_moneda_200(self):

        """
        Agrega una moneda de 200 pesos a la alcancía. La alcancía no está rota.
        """
        self.__numero_monedas_200 += 1

    def agregar_moneda_500(self):

        """
        Agrega una moneda de 500 pesos a la alcancía. La alcancía no está rota.
        """
        self.__numero_monedas_500 += 1

    def agregar_moneda_1000(self):

        """
        Agrega una moneda de 1000 pesos a la alcancía. La alcancía no está rota.
        """
        self.__numero_monedas_1000 += 1

    def inicializar(self):
        """
        Establece los datos iniciales de una nueva alcancía
        """
        self.__numero_monedas_50 = 0
        self.__numero_monedas_100 = 0
        self.__numero_monedas_200 = 0
        self.__numero_monedas_500 = 0
        self.__numero_monedas_1000 = 0
        self.__esta_rota = False


    def dar_total_dinero(self):
        """
        Retorna el dinero total presente en la alcancia
        :return Dinero total de la alcancia
        """
        total_monedas_50 = self.__numero_monedas_50 * 50
        total_monedas_100 = self.__numero_monedas_100 * 100
        total_monedas_200 = self.__numero_monedas_200 * 200
        total_monedas_500 = self.__numero_monedas_500 * 500
        total_monedas_1000 = self.__numero_monedas_1000 * 1000

        return total_monedas_50 + total_monedas_100 + total_monedas_200 + total_monedas_500 + total_monedas_1000


    @property
    def numero_monedas_50(self):
        """
        Número de monedas de 50 introducidas en la alcancía
        """
        return self.__numero_monedas_50

    @property
    def numero_monedas_100(self):
        """
        Número de monedas de 100 introducidas en la alcancía
        """
        return self.__numero_monedas_100

    @property
    def numero_monedas_200(self):
        """
        Número de monedas de 200 introducidas en la alcancía
        """
        return self.__numero_monedas_200

    @property
    def numero_monedas_500(self):
        """
        Número de monedas de 500 introducidas en la alcancía
        """
        return self.__numero_monedas_500

    @property
    def numero_monedas_1000(self):
        """
        Número de monedas de 1000 introducidas en la alcancía
        """
        return self.__numero_monedas_1000

    @property
    def esta_rota(self):
        """
        Indica si la alcancía está rota
        """
        return self.__esta_rota


    def agregar_monedas_50(self, monedas_50):
        """
        Agrega un número de monedas de 50 establecido por parámetro
        :param: monedas_50 Número de monedas de 50 a agregar
        """
        self.__numero_monedas_50 += monedas_50

    def romper_alcancia(self):
        """
        Rompe la alcancía si esta no se encuentra rota.
        """
        self.__esta_rota = True

    def dar_estado_alcancia(self):
        """
        Devuelve una cadena de texto con el estado de la alcancía
        """

        total_dinero = self.dar_total_dinero()

        return "La alcancía tenía " + str(total_dinero) + "pesos."

