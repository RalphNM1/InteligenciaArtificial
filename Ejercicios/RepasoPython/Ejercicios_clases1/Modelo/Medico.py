from Trabajador import Trabajador
from datetime import datetime

class Medico(Trabajador):
    def __init__(self, nif, nombre, fecha_nac, num_colegiado, sexo, especialidad, fecha_comienzo):
        super().__init__(nif, nombre, fecha_nac, num_colegiado, sexo)
        self.especialidad = especialidad
        self.fecha_comienzo = fecha_comienzo

    @staticmethod
    def mostrar_años_trabajados(fecha_comienzo):
        fecha_inicio = datetime.strptime(fecha_comienzo, "%d/%m/%Y")
        fecha_actual = datetime.now()
        return fecha_actual.year - fecha_inicio.year - ((fecha_actual.month, fecha_actual.day) < (fecha_inicio.month, fecha_inicio.day))


# Lista de trabajadores