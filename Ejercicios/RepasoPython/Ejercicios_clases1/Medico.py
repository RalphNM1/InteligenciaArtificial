from Trabajador import Trabajador

class Medico(Trabajador):
    def __init__(self,nif, nombre, fecha_nac,numero_colegiado,sexo,especialidad,fecha_comienzo,):
        Trabajador.__init__(self,nif,nombre,fecha_nac,numero_colegiado,sexo)
        self.especialidad = especialidad
        self.fecha_comienzo = fecha_comienzo


"""En el caso de un Médico se indica la especialidad y la fecha en la que comenzó a
ejercer"""