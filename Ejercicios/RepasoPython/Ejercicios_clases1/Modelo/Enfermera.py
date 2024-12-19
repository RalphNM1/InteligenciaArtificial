from Trabajador import Trabajador

class Enfermera(Trabajador):
    """
    Clase que representa a una Enfermera, hereda de la clase Trabajador.

    :param nif: NIF de la enfermera.
    :type nif: str
    :param nombre: Nombre de la enfermera.
    :type nombre: str
    :param fecha_nac: Fecha de nacimiento de la enfermera.
    :type fecha_nac: str
    :param num_colegiado: Número de colegiado de la enfermera.
    :type num_colegiado: str
    :param sexo: Sexo de la enfermera.
    :type sexo: str
    :param area: Área de especialización de la enfermera.
    :type area: str
    :param personas_acargo: Número de personas a cargo de la enfermera.
    :type personas_acargo: int
    """
    def __init__(self, nif, nombre, fecha_nac, num_colegiado, sexo, area, personas_acargo):
        super().__init__(nif, nombre, fecha_nac, num_colegiado, sexo)
        self.area = area
        self.personas_acargo = personas_acargo

    def mostrar_personas_acargo(self):
        """
        Muestra el número de personas a cargo de la enfermera.
        """
        print(f"La enfermera {self.nombre} tiene {self.personas_acargo} personas a su cargo.")

    def añadir_personas_acargo(self, cantidad):
        """
        Añade una cantidad especificada de personas al cargo de la enfermera.

        :param cantidad: Cantidad de personas añadidas al cargo.
        :type cantidad: int
        """
        self.personas_acargo += cantidad
        print(f"Se han añadido {cantidad} personas a cargo. Ahora {self.nombre} tiene {self.personas_acargo} personas a su cargo.")

    def reducir_personas_acargo(self, cantidad):
        """
        Reduce una cantidad especificada de personas al cargo de la enfermera.

        :param cantidad: Cantidad de personas reducidas al cargo.
        :type cantidad: int
        """
        if self.personas_acargo - cantidad >= 0:
            self.personas_acargo -= cantidad
            print(f"Se han reducido {cantidad} personas a cargo. Ahora {self.nombre} tiene {self.personas_acargo} personas a su cargo.")
        else:
            print("No se puede reducir más personas a cargo de las que tiene.")
