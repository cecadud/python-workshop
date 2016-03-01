
class Celular:

    """
    Clase que representa un celular de la subasta
    """

    def __init__(self):
        """
        Establece los datos iniciales de un nuevo celular.
        """
        self.reiniciar_numero_ofertas()
        self.reiniciar_valor_total_ofertas()
        self.inicializar("",0,"")

    @property
    def modelo(self):
        """
        Retorna el modelo del celular.
        :return Modelo del celular
        """
        return self.__modelo

    @property
    def costo_base(self):
        """
        Retorna el costo base del celular.
        :return Costo base del celular
        """
        return self.__costo_base

    @property
    def marca(self):
        """
        Retorna la marca del celular.
        :return Marca del celular
        """
        return self.__marca

    @property
    def numero_ofertas(self):
        """
        Retorna el número de ofertas realizadas por el celular.
        :return Número de ofertas realizadas por el  celular
        """
        return self.__numero_ofertas

    @property
    def valor_total_ofertas(self):
        """
        Retorna el valor del total de ofertas por el celular
        :return Valo del total de ofertas por el celular
        """
        return self.__valor_total_ofertas

    def inicializar(self, modelo, costo_base, marca):
        """
        Inicializa la información del celular con lo valores que llegan como parámetro.
        <b>post: </b> Se inicializaron los atributos modelo, costoBase, marca con los valores recibidos como parámetros.
        El número de ofertas y el valor total de las ofertas se inicializaron en cero.
        :param modelo Modelo del celular.
        :param costo_base Costo base del celular
        :param marca Marca del celular
        """
        self.__modelo = modelo
        self.__costo_base = costo_base
        self.__marca = marca
        self.__numero_ofertas = 0
        self.__valor_total_ofertas = 0

    def registrar_oferta_minima(self):
        """
        Registra una oferta mínima por el celular.
        Se adiciona al valor total de las ofertas la suma de $50.000 y se incrementa el número de ofertas en 1
        """
        pass #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_moderada(self):
        """
        Registra una oferta moderada por el celular.
        Se adiciona al valor total de las ofertas la suma de $100.000 y se incrementa el número de ofertas en 1
        """
        pass #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_abierta(self, monto ):
        """
        Registra una oferta abierta por el celular.
        Se adiciona al valor total de las ofertas la suma recibida por parámetro y se incrementa el número de ofertas en 1
        :param monto Monto ofertado por el celular
        """
        pass #TODO: Reemplazar "pass" y completar el método según la documentación

    def calcular_incremento_costo_base(self):
        """
        Calcula la diferencia entre el valor total de las ofertas y el costo base del celular
        :return Incremento del costo base
        """
        pass #TODO: Reemplazar "pass" y completar el método según la documentación

    def reiniciar_numero_ofertas(self):
        """
        Se reinicia el número de ofertas
        """
        self.__numero_ofertas = 0

    def reiniciar_valor_total_ofertas(self):
        """
        Se reinicia el valor total de las ofertas
        """
        self.__valor_total_ofertas = 0
