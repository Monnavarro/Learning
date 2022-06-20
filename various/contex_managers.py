# -- coding: utf-8 --
"""

Created on: 20/6/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""


class MiGestor:
    def __enter__(self):
        print - "Entra en __enter__"

    def __exit__(self, exc_type, exec_value, traceback):
        print("Entra en __exit__")


with MiGestor() as f:
    print("Hola")
