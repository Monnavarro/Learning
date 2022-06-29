# -- coding: utf-8 --
"""

Created on: 19/6/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# calculadora.py

# Tipo de operacion: suma/resta/multiplicación
operacion = "suma"

# Parámetros de la operación
a = 4
b = 7

if operacion == "suma":
    print(a+b)
elif operacion == "resta":
    print(a-b)
elif operacion == "multiplicacion":
    print(a*b)