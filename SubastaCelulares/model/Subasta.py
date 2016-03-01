from model.Celular import Celular

class Subasta:

    """
    Clase que representa la subasta.
    """

    def __init__(self):
        """
        Establece los valores iniciales de una nuvea subasta
        """
        """
        :return:
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
        self.__celular2 = Celular()
        self.__celular3 = Celular()

        self.__celular1.inicializar("Galaxy Note", 50000, "Samsung")
        self.__celular2.inicializar("LG Z", 50000, "LG")
        self.__celular3.inicializar("iPhone", 50000, "Apple")

    @property
    def celular1(self):
        """
        Retorna el primer celular de la subasta
        :return Primer celular de la subasta
        """
        return self.__celular1

    @property
    def celular2(self):
        """
        Retorna el segundo celular de la subasta
        :return Segundo celular de la subasta
        """
        return self.__celular2

    @property
    def celular3(self):
        """
        Retorna el tercer celular de la subasta
        :return Tercer celular de la subasta
        """
        return self.__celular3

    def registrar_oferta_minima_celular_1(self):
        """
        Registra una oferta mínima para el primer celular.
        """
        self.__celular1.registrar_oferta_minima()

    def registrar_oferta_minima_celular_2(self):
        """
        Registra una oferta mínima para el segundo celular.
        """
        self.__celular2.registrar_oferta_minima()


    def registrar_oferta_minima_celular_3(self):
        """
        Registra una oferta mínima para el tercer celular.
        """
        self.__celular3.registrar_oferta_minima()

    def registrar_oferta_moderada_celular_1(self):
        """
        Registra una oferta moderada para el primer celular.
        """
        self.__celular1.registrar_oferta_moderada()

    def registrar_oferta_moderada_celular_2(self):
        """
        Registra una oferta moderada para el segundo celular.
        """
        self.__celular2.registrar_oferta_moderada()

    def registrar_oferta_moderada_celular_3(self):
        """
        Registra una oferta moderada para el tercer celular.
        """
        self.__celular3.registrar_oferta_moderada()

    def registrar_oferta_abierta_celular_1(self, monto):
        """
        Registra una oferta abierta para el primer celular.
        :param monto Valor de la oferta. monto > 0
        """
        self.__celular1.registrar_oferta_abierta(monto)

    def registrar_oferta_abierta_celular_2(self, monto):
        """
        Registra una oferta abierta para el segundo celular.
        :param monto Valor de la oferta. monto > 0
        """
        self.__celular2.registrar_oferta_abierta(monto)

    def registrar_oferta_abierta_celular_3(self, monto):
        """
        Registra una oferta abierta para el tercer celular.
        :param monto Valor de la oferta. monto > 0
        """
        self.__celular3.registrar_oferta_abierta(monto)

    def calcular_incremento_promedio_costo_base(self):
        """
        Devuelve el incremento promedio del costo base de todos los celulares sobre el valor total recaudado.
        En otras palabras, el método calcula el promedio del incremento del costo base de todos los celulares.
        :return La sumatoria del incremento del costo base de cada uno de los celulares divido por la cantidad de celulares.
        """
        incremento_cel_1 = self.__celular1.calcular_incremento_costo_base()
        incremento_cel_2 = self.__celular2.calcular_incremento_costo_base()
        incremento_cel_3 = self.__celular3.calcular_incremento_costo_base()

        return (incremento_cel_1+incremento_cel_2+incremento_cel_3)/3.0

    def calcular_valor_total_recaudado(self):
        """
        Devuelve el valor total recaudado por las ofertas de los tres celulares.
        :return La sumatoria del valor total de las ofertas realizadas por los tres celulares.
        """
        total_cel_1 = self.__celular1.valor_total_ofertas
        total_cel_2 = self.__celular2.valor_total_ofertas
        total_cel_3 = self.__celular3.valor_total_ofertas

        return total_cel_1 + total_cel_2 + total_cel_3

    def calcular_numero_total_ofertas(self):
        """
        La sumatoria del valor total de las ofertas realizadas por los tres celulares.
        :return La sumatoria del valor total de las ofertas realizadas por los tres celulares.
        """
        total_cel_1 = self.__celular1.numero_ofertas
        total_cel_2 = self.__celular2.numero_ofertas
        total_cel_3 = self.__celular3.numero_ofertas

        return total_cel_1 + total_cel_2 + total_cel_3

    def reiniciar_subasta(self):
        """
        Reinicia la subasta al estado inicial. Todos los celulares reinician el número de ofertas y el valor total
        de sus ofertas.
        """
        self.__celular1.reiniciar_numero_ofertas()
        self.__celular1.reiniciar_valor_total_ofertas()

        self.__celular2.reiniciar_numero_ofertas()
        self.__celular2.reiniciar_valor_total_ofertas()

        self.__celular3.reiniciar_numero_ofertas()
        self.__celular3.reiniciar_valor_total_ofertas()