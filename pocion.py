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
    # Defino los atributos poniendo el nombre de la variable:tipodedato
    # Recordamos que los atributos son las características de un objeto, así como los parámetros son las características de una función. Por ejemplo: un cuadro tiene un color, un tamaño, un autor, etc. y esos serían sus atributos.
    nombre:str
    ingredientes_conocidos:List[str]
    efecto:str
    caracteristicas:str
    nivel_dificultad:str

    # Defino métodos poniendo el nombre de la función y los parámetros que recibe. En general se escriben como def __str__, por ejemplo porque son métodos especiales que ya están definidos en python. 
    # Para recordar: los métodos son las acciones que puede realizar un objeto. Por ejemplo: un cuadro puede ser colgado, puede ser vendido, etc. y esos serían sus métodos.
    
    def __str__(self)-> str: # Representación como string - se llama __str__ porque es un método especial de python, y se para que se pueda imprimir el objeto como string. Es una "convención" que se declare así.
        '''
        Devuelve una representación como string de la poción.
        Requiere: nada.
        '''
        return f'Poción {self.nombre}' # Devuelve el nombre de la poción. Se usa f para poder poner el nombre de la poción en el string. 
    
    def __lt__ (self, other:Pocion)-> bool: # Comparación por menor de dos pociones en base a su nombre (orden lexicográfico). 
        '''
        Devuelve True si la poción self es menor que la poción other.
        Requiere: nada.
        '''
        return self.nombre < other.nombre # 
    
    ## Función para comparar por menor de dos posicones en base a su orden lexicográfico. Esta está hecha sin usar el método especial __lt__.
    def es_menor(self, other:Pocion)-> bool:
        '''
        Devuelve True si la poción self es menor que la poción other.
        Requiere: nada.
        '''
        # Hago a mano la comparación
        if self.nombre < other.nombre: # Si el nombre de la poción self es menor que el nombre de la poción other. Se tiene por "menor" al string que aparece primero en el orden lexicográfico. Es decir, si una palabra es manzana y la otra es xilofono, la primera es menor que la segunda porque aparece antes en el diccionario, ya que la m viene antes que la x.
            return True
        else:
            return False
    

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
    
