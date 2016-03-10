class Carro:

    """
    Clase que representa un carro de alquiler
    """

    KILOMETRAJE_REPARACION = 100000  # Constante que representa el kilometraje minimo para reparación
    MAXIMO_KILOMETRAJE = 500000 # Kilometraje máximo del carro para poder ser alquilado
    MINIMO_NUM_ALQUILER = 20 # Mínimo número de veces que se tiene que alquilar un carro para hacer reparación

    def __init__(self, modelo, marca, precio_alquiler, precio_reparacion):

        """

        Constructor de la clase Carro.
        Se inicializaron los atributos modelo, marca, precioAlquiler y precioReparación con los valores recibidos por
        parámetro.
        Los atributos total_alquileres, alquileres_desde_reparacion y kilometraje se inicializaron en cero
        :param modelo: Modelo del carro. != "". != None
        :param marca: Marca del carro. != "". != None
        :param precio_alquiler: Precio de alquiler del carro. > 0
        :param precio_reparacion: Precio de reparación del carro. > 0
        """

        self.__modelo = modelo
        self.__marca = marca
        self.__precio_alquiler = precio_alquiler
        self.__precio_reparacion = precio_reparacion
        self.__alquilado = False
        self.__total_alquileres = 0
        self.__kilometraje = 0
        self.__alquileres_desde_reparacion = 0

    @property
    def modelo(self):
        """
        Retorna el modelo del carro
        :return: Modelo del carro
        """
        return self.__modelo

    @property
    def marca(self):
        """
        Retorna la marca del carro
        :return: Marca del carro
        """
        return self.__marca

    @property
    def kilometraje(self):
        """
        Retorna el kilometraje del carro
        :return: Kilometraje del carro
        """
        return self.__kilometraje

    @property
    def precio_alquiler(self):
        """
        Retorna el precio de alquiler del carro
        :return: Precio de alquiler del carro
        """
        return self.__precio_alquiler

    @property
    def precio_reparacion(self):
        """
        Retorna el precio de reparacion del carro
        :return: Precio de reparacion
        """
        return self.__precio_reparacion

    @property
    def alquileres_desde_reparacion(self):
        """
        Retorna la cantidad de veces que ha sido alquilado el carro desde su última reparación
        :return: Cantidad de alquileres desde última reparacion
        """
        return self.__alquileres_desde_reparacion

    @property
    def total_alquileres(self):
        """
        Retorna la cantidad total de veces que ha sido alquilado el carro
        :return:
        """
        return self.__total_alquileres

    @property
    def alquilado(self):
        """
        Indica si el carro está actualmente alquilado
        :return: True si el carro está alquilado. False de lo contrario.
        """
        return self.__alquilado

    def alquilar(self):

        """
        Alquila el carro cuando se cumplen las siguientes condiciones:
        1. El carro no está alquilado
        2. El kilometraje es menor al máximo kilmoetraje permitido

        Cuando el carro cumple las condiciones para ser alquilado:
        1. El carro pasa a estado alquilado
        2. Se incrementa en 1 el número total de alquileres
        3. Se incrementa en 1 el número de veces que ha sido alquilado desde reparación
        :return: True si se pudo alquilar el carro. False en caso contrario.
        """
        if( not self.__alquilado and self.__kilometraje < Carro.MAXIMO_KILOMETRAJE):
            self.__alquilado = True
            self.__total_alquileres += 1
            self.__alquileres_desde_reparacion += 1

        return self.__alquilado

    def devolver(self, kilometros):
        """
        Devuelve el carro cuando se cumplen las siguientes condiciones:
        1. El kilometraje reportado es mayor al registrado.
        2. El carro está alquilado

        Cuando el carro cumple las condiciones para la devolución del carro
        1. El carro pasa a estado alquilado
        2. El kilometraje se actualiza con el valor pasado por parámetro
        :param kilometros: Cantidad de kilómetros con que se devuelve el carro. >= 0
        :return: True si se pudo devolver el carro. False de lo contrario.
        """

        if( kilometros > self.__kilometraje and self.__alquilado):
            self.__alquilado = False
            self.__kilometraje = kilometros

        return (not self.__alquilado)

    def reparar(self):
        """
        Repara un carro cuando se cumplen las siguientes condiciones:
        1. El carro no está alquilado y se cumple una entre 2 y 3
        2. El kilometraje actual es mayor al kilometraje mínimo de reparación y se ha alquilado
        más de 2 veces después de la última reparación
        3. La cantidad de veces que ha sido alquilado el carro después de la reparación es mayor al mínimo
        número de alquileres

        Cuando el carro cumple con las condiciones para la reparación:
        1. Se reinicia el kilometraje del carro
        2. Se reinicia el total de alquileres desde reparación.
        :return: True si se pudo reparar el carro. False en caso contrario.
        """

        if( not self.__alquilado and ( ( self.__kilometraje > Carro.KILOMETRAJE_REPARACION and
                                self.__alquileres_desde_reparacion > 2 )
                                or ( self.__alquileres_desde_reparacion > Carro.MINIMO_NUM_ALQUILER) ) ):
            self.__kilometraje = 0
            self.__alquileres_desde_reparacion = 0
            return True

        return False

    