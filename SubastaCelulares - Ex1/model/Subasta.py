"""
    Clase que representa la subasta.
"""

from model.Celular import Celular

class Subasta:

    def __init__(self):
        """
        Establece los valores iniciales de una nueva subasta
        """
        self.inicializar()

    def inicializar(self):
        """
        Inicializa los 3 celulares de la subasta de la siguiente forma:
        Celular1 - Modelo: Galaxy Note, Precio base: 50000, Marca: Samsung.
        Celular2 - Modelo: LG Z, Precio base: 50000, Marca: LG.
        Celular3 - Modelo: iPhone, Precio base: 50000, Marca: Apple.
        """
        self.__celular1 = Celular()
        self.__celular1.inicializar("Galaxy Note", 50000, "Samsung")

        #TODO: Crear e inicializar los celulares 2 y 3

    @property
    def celular1(self):
        """
        Retorna el primer celular de la subasta
        :return Primer celular de la subasta
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    @property
    def celular2(self):
        """
        Retorna el segundo celular de la subasta
        :return Segundo celular de la subasta
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    @property
    def celular3(self):
        """
        Retorna el tercer celular de la subasta
        :return Tercer celular de la subasta
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_minima_celular_1(self):
        """
        Registra una oferta mínima para el primer celular.
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_minima_celular_2(self):
        """
        Registra una oferta mínima para el segundo celular.
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_minima_celular_3(self):
        """
        Registra una oferta mínima para el tercer celular.
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_moderada_celular_1(self):
        """
        Registra una oferta moderada para el primer celular.
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_moderada_celular_2(self):
        """
        Registra una oferta moderada para el segundo celular.
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_moderada_celular_3(self):
        """
        Registra una oferta moderada para el tercer celular.
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_abierta_celular_1(self, monto):
        """
        Registra una oferta abierta para el primer celular.
        :param monto Valor de la oferta. monto > 0
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_abierta_celular_2(self, monto):
        """
        Registra una oferta abierta para el segundo celular.
        :param monto Valor de la oferta. monto > 0
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def registrar_oferta_abierta_celular_3(self, monto):
        """
        Registra una oferta abierta para el tercer celular.
        :param monto Valor de la oferta. monto > 0
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def calcular_incremento_promedio_costo_base(self):
        """
        Devuelve el incremento promedio del costo base de todos los celulares sobre el valor total recaudado.
        En otras palabras, el método calcula el promedio del incremento del costo base de todos los celulares.
        :return La sumatoria del incremento del costo base de cada uno de los celulares divido por la cantidad de celulares.
        """

        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def calcular_valor_total_recaudado(self):
        """
        Devuelve el valor total recaudado por las ofertas de los tres celulares.
        :return La sumatoria del valor total de las ofertas realizadas por los tres celulares.
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def calcular_numero_total_ofertas(self):
        """
        La sumatoria del valor total de las ofertas realizadas por los tres celulares.
        :return La sumatoria del valor total de las ofertas realizadas por los tres celulares.
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación

    def reiniciar_subasta(self):
        """
        Reinicia la subasta al estado inicial. Todos los celulares reinician el número de ofertas y el valor total
        de sus ofertas.
        """
        pass    #TODO: Reemplazar "pass" y completar el método según la documentación