from Trabajador import Trabajador

class Enfermera(Trabajador):
    def __init__(self,nif, nombre, fecha_nac,numero_colegiado,sexo,area,personas_acargo):
        Enfermera.__init__(self,nif,nombre,fecha_nac,numero_colegiado,sexo)
        self.area = area
        self.personas_acargo = personas_acargo


mi_enfermera = Enfermera()

