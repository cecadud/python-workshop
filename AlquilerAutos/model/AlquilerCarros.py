from AlquilerAutos.model.Carro import Carro

class AlquilerCarros:

    def __init__(self):
        """
        Construye un nuevo alquiler de carros. Se crearon los carros de la siguiente manera:
        Carro1 - Modelo: Wrangler - Marca: Jeep - PrecioAlquiler: 200000 - PrecioReparacion: 2000000
        Carro2 - Modelo: Camaro - Marca: Chevrolet - PrecioAlquiler: 400000 - PrecioReparacion: 3000000
        Carro3 - Modelo: Prado - Marca: Toyota - PrecioAlquiler: 300000 - PrecioReparacion: 2500000
        Carro4 - Modelo: Clio - Marca: Renault - PrecioAlquiler: 150000 - PrecioReparacion: 1000000
        """

        self.__carro1 = Carro("Wrangler", "Jeep", 200000, 2000000)
        self.__carro2 = Carro("Camaro", "Chevrolet", 400000, 3000000)

        #TODO: Completar la creación de los carros faltantes de acuerdo a la documentación

    @property
    def ingresos(self):
        """
        Retorna los ingresos totales del alquiler
        :return: Ingresos totales del alquiler
        """
        return self.__ingresos

    @property
    def carro1(self):
        """
        Retorna el primer carro del alquiler
        :return: Primer carro de alquiler
        """
        return self.__carro1

    @property
    def carro2(self):
        """
        Retorna el segundo carro del alquiler
        :return: Segundo carro de alquiler
        """
        return self.__carro2

    @property
    def carro3(self):
        """
        Retorna el tercer carro del alquiler
        :return: Tercer carro de alquiler
        """
        return self.__carro3

    @property
    def carro4(self):
        """
        Retorna el cuarto carro del alquiler
        :return: Cuarto carro de alquiler
        """
        return self.__carro4

    def buscar_carro(self, modelo):
        """
        Retorna el carro con el modelo dado por parámetro. No hay dos carros con el mismo modelo.
        :param modelo: Modelo del carro buscado
        :return: Carro buscado
        """

        car = None
        if( self.__carro1.modelo == modelo):
           car = self.__carro1
        elif( self.__carro2.modelo == modelo ):
            car = self.__carro2

        # TODO: Escribir las condiciones restantes

        return car

    def calcular_total_alquiladas(self):
        """
        Calcula el total de veces que han sido alquilados los carros de la empresa.
        :return:Número total de carros alquilados
        """
        pass  #TODO: Cambiar "pass" por la implementación del método

    def obtener_carro_mas_alquilado(self):
        """
        Busca el carro más alquilado del alquiler. Si existen varios carros con el mismo número de alquileres, se
        escoge el primero.
        Si no hay carros alquilados en la empresa se retorna el mensaje: "Ningún carro ha sido alquilado."
        Si hay carros alquilados, se retorna el mensaje: "El carro más alquilado es: <Marca del carro>-<Modelo del carro>."
        :return: Mensaje con la marca y le modelo del carro más alquilado, o "Ningún carro ha sido alquilado"
        """
        pass #TODO: Cambiar "pass" por la implementación del método

    def alquilar_carro(self, modelo, numero_dias):
        """
        Alquila el carro con el modelo dado por el número de días solicitados.
        Si se cumplen las condiciones para alquilar el carro:
        1. Se alquiló el carro
        2. Se incrementan los ingresos con el precio del carro por el número de días.
        :param modelo: Modelo del carro que se desea alquilar. != None. != ""
        :param numero_dias: Número de días que se quiere alquilar el carro. > 0
        :return: True si se pudo alquilar el carro, False en caso contrario.
        """
        pass #TODO: Cambiar "pass" por la implementación del método

    def devolver_carro(self, modelo, kilometraje):
        """
        Devuelve el carro con el modelo dado. El carro con el modelo dado existe
        :param modelo: Modelo del carro que se quiere devolver. != None. != ""
        :param kilometraje: Kilometraje con el que llego el carro. > 0
        :return: True si el carro se pudo devolver. False en caso contrario.
        """
        pass #TODO: Cambiar "pass" por la implementación del método

    def reparar_carro(self, modelo):
        """
        Repara el carro con el modelo dado si se tienen los ingresos suficientes.
        1. El carro con el modelo dado existe
        2. Si se repara el carro, se actualizaron los ingresos del alquiler si:
          2.1 El carro cumple con las condiciones para la reparación
          2.2. Hay ingresos suficientes para realizar la reparación del carro
        :param modelo: Modelo del carro que se quiere devolver. != None. != ""
        :return: True si se puede reparar el carro. False en caso contrario.
        """
        pass #TODO: Cambiar "pass" por la implementación del método