

from abc import ABC, abstractmethod


class Trabajador:
    """
    Clase base que representa a un Trabajador del hospital.

    :param nif: NIF del trabajador.
    :type nif: str
    :param nombre: Nombre del trabajador.
    :type nombre: str
    :param fecha_nac: Fecha de nacimiento del trabajador.
    :type fecha_nac: str
    :param num_colegiado: Número de colegiado del trabajador.
    :type num_colegiado: str
    :param sexo: Sexo del trabajador.
    :type sexo: str
    """
    def __init__(self, nif, nombre, fecha_nac, num_colegiado, sexo):
        self.nif = nif
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.num_colegiado = num_colegiado
        self.sexo = sexo

    def describeme(self):
        """
        Devuelve el nombre de la clase del trabajador.

        :return: Nombre de la clase.
        :rtype: str
        """
        return type(self).__name__
