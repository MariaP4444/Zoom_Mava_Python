from typing import List, Dict

class Animal:
    def __init__(self, nombre, especie, estadoDeSalud, id, edad, tempMaxA, tempMinA,  cantMaxDormir, juguetes,
                 alimentacion):
        self.nombre = nombre
        self.especie = especie
        self.estadoDeSalud = estadoDeSalud
        self.id = id
        self.edad = edad
        self.tempMaxA = tempMaxA
        self.tempMinA = tempMinA
        self.cantHorasDormidas = 0
        self.cantMaxDormir = cantMaxDormir
        self.jugar = False
        self.comer = False
        self.juguetes = juguetes
        self.alimentos = {}
        self.alimentacion = alimentacion