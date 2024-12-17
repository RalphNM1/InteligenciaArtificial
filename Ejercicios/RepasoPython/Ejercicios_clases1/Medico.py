from Trabajador import Trabajador
import datetime as dt
class Medico(Trabajador):
    def __init__(self,nif, nombre, fecha_nac, num_colegiado,sexo,especialidad,fecha_comienzo,):
        Trabajador.__init__(self,nif,nombre,fecha_nac,num_colegiado,sexo)
        self.especialidad = especialidad
        self.fecha_comienzo = fecha_comienzo


    @staticmethod
    def mostrar_años_trabajados(fecha_comienzo):
        actualidad = dt.datetime.now()
        inicio = dt.datetime.strptime(fecha_comienzo, '%d/%m/%Y')
        diferencia = actualidad - inicio
        return diferencia.days // 365
