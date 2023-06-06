from __future__ import annotations
from pocion import Pocion
from typing import Dict, List, TextIO

class CatalogoPociones:
    def __init__(self, archivo_csv:str):
        '''
        Inicializa el catálogo de pociones, cargando las pociones
        contenidas en el archivo archivo_csv que tienen el nivel de
        dificultad definido (el resto las ignora).
        Requiere: archivo_csv es el nombre de un archivo en formato
                  CSV (valores separados por punto y coma), con cinco columnas:
                  'Name' (str), 'Known ingredients' (lista de
                  strings separados por comas), 'Effect' (str),
                  'Characteristics' (str), 'Difficulty level' (str).
        '''
        self._pociones_dificultad:Dict[str, List[Pocion]] = dict()

        ############################## COMPLETAR ##############################

    def exportar_csv_dificultad(self, dif:str):
        '''
        Escribe un archivo CSV llamado POCIONES_[dif].csv, donde dif
        correposnde a una cierta dificultad recibida como argumento.
        Por ejemplo, si el método se invoca con el argumento 'Advanced', el
        archivo se llamará POCIONES_Advanced.csv.
        Los títulos de las columnas son 'NOMBRE', 'INGREDIENTES CONOCIDOS',
        'EFECTO' y 'CARACTERISTICAS' y los valores están separados con ;.
        El archivo incluye una entrada por cada poción del catálogo cuya
        dificultad sea dif. Además, en el archivo las pociones aparecen
        ordenadas de acuerdo al orden definido en la clase Pocion.
        '''
        ############################## COMPLETAR ##############################
