

from abc import ABC, abstractmethod


class Trabajador:
    def __init__(self,nif, nombre, fecha_nac,num_colegiado,sexo):
        self.nif = nif
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.num_colegiado = num_colegiado
        self.sexo = sexo

    def describeme(self):
        return type(self).__name__


