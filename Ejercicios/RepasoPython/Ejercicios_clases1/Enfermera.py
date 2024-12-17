from Trabajador import Trabajador

class Enfermera(Trabajador):
    def __init__(self,nif, nombre, fecha_nac,numero_colegiado,sexo,area,personas_acargo):
        Enfermera.__init__(self,nif,nombre,fecha_nac,numero_colegiado,sexo)
        self.area = area
        self.personas_acargo = personas_acargo
    
    
    @staticmethod
    def mostrar_personas_acargo(enfermera):
        print(f"El número de personas a cargo por la enfermera {enfermera.nombre} con NIF {enfermera.nif} es {enfermera.personas_acargo}.")
    @staticmethod
    def añadir_personas_acargo(enfermera,cantidad):
        enfermera.personas_acargo += cantidad
    @staticmethod
    def reducir_personas_acargo(enfermera,cantidad):
        enfermera.personas_acargo -= cantidad

