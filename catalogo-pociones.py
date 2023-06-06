from __future__ import annotations
from pocion import Pocion
from typing import Dict, List, TextIO

class CatalogoPociones:
    def __init__(self, archivo_csv:str):
        '''
       Requiere: archivo_csv es un string que representa el nombre de un archivo csv con el siguiente formato:
       Devuelve: un objeto de la clase CatalogoPociones con un único atributo de tipo Dict[str, Set[Pocion]], que vincula niveles de dificultad de preparación de pociones con todas las pociones de tal dificultad
        '''
        self._pociones_dificultad:Dict[str, List[Pocion]] = dict()
        with open(archivo_csv, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea = linea.rstrip('\n')
                nombre, ingredientes, efecto, caracteristicas, dificultad = linea.split(';')
                ingredientes = ingredientes.split(',')
                p = Pocion(nombre, ingredientes, efecto, caracteristicas, dificultad)
                if dificultad not in self._pociones_dificultad:
                    self._pociones_dificultad[dificultad] = []
                self._pociones_dificultad[dificultad].append(p)

    def listar_por_dificultad(self, dificultad:str)-> List[Pocion]:
            '''
            Requiere: dificultad es un string que representa una dificultad de pociones
            Devuelve: una lista de las Pociones del catalogo que tienen la dificultad indicada por el argumento con el cual el método es invocado. Las pociones deben aparecer ordenadas siguiendo la relación < de la clase Poción.
            Orden de Complejidad: O(1) porque accede a un elemento del diccionario y devuelve una lista de pociones ordenadas por dificultad. Lo que implica que no depende de la cantidad de pociones que tenga el catalogo, ya que siempre va a devolver una lista de pociones ordenadas por dificultad.
            '''
            return self._pociones_dificultad[dificultad] # Devuelve una lista de pociones ordenadas por dificultad
        
    def listar_pociones_con_n_ingredientes(self, n:int)-> List[tuple]:
            '''
           Requiere: n es un número entero positivo.
           Devuelve: una lista de tuplas, dónde cada tupla guarda la Poción con n cantidad de ingredientes y su dificultad, dónde n es el argumento con el cual el método es invocado. Las tuplas que conforman la lista deben ser de la froma < difucultad, Pocion >.
           Orden de Complejidad: O(n) porque recorre todas las pociones del catalogo y depende de la cantidad de ingredientes de cada poción. 
            '''
            # defino una lista vacía
            lista = []
            # recorro el diccionario
            for dificultad, pociones in self._pociones_dificultad.items():
                # recorro las pociones de cada dificultad
                for p in pociones:
                    # si la poción tiene n ingredientes
                    if len(p.ingredientes_conocidos) == n:
                        # agrego una tupla con la dificultad y la poción
                        lista.append((dificultad, p))
            # devuelvo la lista ordenada
            return sorted(lista)
    


    def exportar_csv_dificultad(self, dif:str):
        '''
        Requiere: dif es un string que representa una dificultad de pociones
        Devuelve: un archivo csv con las pociones de la dificultad indicada
        '''
        # Abro el archivo
        with open(f'POCIONES_{dif}.csv', 'w', encoding='utf-8') as archivo:
            # Escribo los títulos de las columnas
            archivo.write('NOMBRE;INGREDIENTES CONOCIDOS;EFECTO;CARACTERISTICAS\n')
            # Recorro las pociones de la dificultad indicada
            for p in self._pociones_dificultad[dif]:
                # Escribo los atributos de cada poción
                archivo.write(f'{p.nombre};{",".join(p.ingredientes_conocidos)};{p.efecto};{p.caracteristicas}\n')
        

