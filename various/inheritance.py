# -- coding: utf-8 --
"""

Created on: 21/6/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
class Silla:
    def __init__(self, color, tamaño, angulo):
        self.cuolor = color
        self.size = tamaño
        self.angule_respaldo = angulo

    def reclinar(self, angulo_de_reclinacion):
        self.angule_respaldo -= angulo_de_reclinacion


silla_montse = Silla("blanca", "extra-big", 90)
print(silla_montse.angule_respaldo)
silla_montse.reclinar(120)

silla_heber = Silla("blanca", "extra-big")
