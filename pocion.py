from __future__ import annotations
from typing import List

class Pocion:
    ''' Representa una poción del universo de Harry Potter.
        Atributos:
            - p.nombre (str)
            - p.ingredientes_conocidos (List[str])
            - p.efecto (str)
            - p.caracteristicas (str)
            - p.nivel_dificultad (str)
        Métodos:
            - representación como string
            -  dos pociones p1 y p2 puedan compararse por menor de forma tal que
                p1 < p2 sea verdadero si el nombre de p1 es menor al de p2 de acuerdo
                al orden lexicográfico
    '''
    # Defino los atributos
    nombre:str
    ingredientes_conocidos:List[str]
    efecto:str
    caracteristicas:str
    nivel_dificultad:str

    #Defino Métodos
    def __str__(self)-> str: # Representación como string
        '''
        Devuelve una representación como string de la poción.
        Requiere: nada.
        '''
        return f'Poción {self.nombre}'
    
    def __lt__ (self, other:Pocion)-> bool: # Comparación por menor de dos pociones en base a su nombre (orden lexicográfico)
        '''
        Devuelve True si la poción self es menor que la poción other.
        Requiere: nada.
        '''
        return self.nombre < other.nombre
    

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
    
