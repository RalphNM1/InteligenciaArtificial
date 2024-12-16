

from abc import ABC, abstractmethod


class Trabajador:
    def __init__(self,nif, nombre, fecha_nac,numero_colegiado,sexo):
        self.nif = nif
        self.nombre = nombre
        self.fecha = fecha_nac
        self.numero_colegiado = numero_colegiado
        self.sexo = sexo

    def describeme(self):
        print("Soy un Trabajador del tipo", type(self).__name__)





