from Trabajador import Trabajador
from datetime import datetime

class Medico(Trabajador):
    """
    Clase que representa a un Médico, hereda de la clase Trabajador.

    :param nif: NIF del médico.
    :type nif: str
    :param nombre: Nombre del médico.
    :type nombre: str
    :param fecha_nac: Fecha de nacimiento del médico.
    :type fecha_nac: str
    :param num_colegiado: Número de colegiado del médico.
    :type num_colegiado: str
    :param sexo: Sexo del médico.
    :type sexo: str
    :param especialidad: Especialidad del médico.
    :type especialidad: str
    :param fecha_comienzo: Fecha de comienzo de la actividad profesional.
    :type fecha_comienzo: str
    """
    def __init__(self, nif, nombre, fecha_nac, num_colegiado, sexo, especialidad, fecha_comienzo):
        super().__init__(nif, nombre, fecha_nac, num_colegiado, sexo)
        self.especialidad = especialidad
        self.fecha_comienzo = fecha_comienzo

    @staticmethod
    def mostrar_años_trabajados(fecha_comienzo):
        """
        Calcula el número de años trabajados a partir de la fecha de comienzo.

        :param fecha_comienzo: Fecha de comienzo del trabajo en formato "DD/MM/AAAA".
        :type fecha_comienzo: str
        :return: Número de años trabajados.
        :rtype: int
        """
        fecha_inicio = datetime.strptime(fecha_comienzo, "%d/%m/%Y")
        fecha_actual = datetime.now()
        return fecha_actual.year - fecha_inicio.year - ((fecha_actual.month, fecha_actual.day) < (fecha_inicio.month, fecha_inicio.day))
