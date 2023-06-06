from __future__ import annotations
from typing import List

class Pocion:
    ''' Representa una poción del universo de Harry Potter.
        Una poción p tiene atributos:
            - p.nombre (str)
            - p.ingredientes_conocidos (List[str])
            - p.efecto (str)
            - p.caracteristicas (str)
            - p.nivel_dificultad (str)
        y métodos:
            - representación como string
            - menor que: <
    '''
    def __init__(self, n:str, ic:List[str], e:str, c:str, nd:str):
        '''
        Inicializa una poción con nombre n, ingredientes secretos ic,
        efecto e, características c y nivel_dificultad nd.
        Requiere: nada.
        '''
        self.nombre:str = n
        self.ingredientes_conocidos:List[str] = ic
        self.efecto:str = e
        self.caracteristicas:str = c
        self.nivel_dificultad:str = nd


    ############################## COMPLETAR ##############################
