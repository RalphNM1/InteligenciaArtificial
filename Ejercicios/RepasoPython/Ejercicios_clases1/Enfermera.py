from Trabajador import Trabajador

class Enfermera(Trabajador):
    def __init__(self, nif, nombre, fecha_nac, num_colegiado, sexo, area, personas_acargo):
        super().__init__(nif, nombre, fecha_nac, num_colegiado, sexo)
        self.area = area
        self.personas_acargo = personas_acargo

    def mostrar_personas_acargo(self):
        print(f"La enfermera {self.nombre} tiene {self.personas_acargo} personas a su cargo.")

    def añadir_personas_acargo(self, cantidad):
        self.personas_acargo += cantidad
        print(f"Se han añadido {cantidad} personas a cargo. Ahora {self.nombre} tiene {self.personas_acargo} personas a su cargo.")

    def reducir_personas_acargo(self, cantidad):
        if self.personas_acargo - cantidad >= 0:
            self.personas_acargo -= cantidad
            print(f"Se han reducido {cantidad} personas a cargo. Ahora {self.nombre} tiene {self.personas_acargo} personas a su cargo.")
        else:
            print("No se puede reducir más personas a cargo de las que tiene.")

