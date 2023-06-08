from __future__ import annotations
import csv
import random
from typing import List

class Pocion:
    # Defino los atributos poniendo el nombre de la variable:tipodedato
    # Recordamos que los atributos son las características de un objeto, así como los parámetros son las características de una función. Por ejemplo: un cuadro tiene un color, un tamaño, un autor, etc. y esos serían sus atributos.
    nombre:str
    ingredientes_conocidos:List[str]
    efecto:str
    caracteristicas:str
    nivel_dificultad:str

    # Defino métodos poniendo el nombre de la función y los parámetros que recibe. En general se escriben como def __str__, por ejemplo porque son métodos especiales que ya están definidos en python. 
    # Para recordar: los métodos son las acciones que puede realizar un objeto. Por ejemplo: un cuadro puede ser colgado, puede ser vendido, etc. y esos serían sus métodos.
    
    def __str__(self)-> str: # Representación como string - se llama __str__ porque es un método especial de python, y se para que se pueda imprimir el objeto. Es una "convención" que se declare así.
        '''
        Devuelve una representación como string de la poción.
        Requiere: nada.
        '''
        return 'Pocion: ' + self.nombre
       
        # OPCION B return f'Poción {self.nombre}' # Devuelve el nombre de la poción. Se usa f para poder poner el nombre de la poción en el string. 
        
    def __lt__ (self, other:Pocion)-> bool: # Comparación por menor de dos pociones en base a su nombre (orden lexicográfico). 
        '''
        Devuelve True si la poción self es menor que la poción other.
        Requiere: nada.
        '''
        return self.nombre < other.nombre # 
    
    def crear_efecto_magico(self):
        """
        Crea un efecto mágico utilizando la poción al estilo de Harry Potter.
        Requiere: nada.
        """
        efectos_magicos = [
            "Transformar el lápiz en un pájaro al tocarlo",
            "Hacer invisible la botella cada vez que tomo agua",
            "Levitar la silla cuando me siento",
            "Ver soluciones de ejercicios de programación en el aire",
            "Transportarme a la playa cuando estoy estudiando",
            "Hacer que el profesor me apruebe el parcial",
        ]

        efecto = random.choice(efectos_magicos)
        print(f"¡La poción {self.nombre} ha creado el efecto mágico: {efecto}!")

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
    

'''
# Versión simplificada
class Pocion:
    nombre: str
    ingredientes_conocidos: List[str]
    efecto: str
    caracteristicas: str
    nivel_dificultad: str

    def __str__(self) -> str:
        return self.nombre

    def __lt__(self, other: Pocion) -> bool:
        return self.nombre < other.nombre

    def __init__(self, n: str, ic: List[str], e: str, c: str, nd: str):
        self.nombre = n
        self.ingredientes_conocidos = ic
        self.efecto = e
        self.caracteristicas = c
        self.nivel_dificultad = nd

#Ejercicio Extra 
 (c) Definir un método crear_efecto_magico: Genera un efecto mágico aleatorio utilizando la poción. 
 El método debe seleccionar al azar un efecto mágico de una lista predefinida y mostrar un mensaje 
 indicando el efecto mágico creado por la poción.

    def crear_efecto_magico(self):
        """
        Crea un efecto mágico utilizando la poción al estilo de Harry Potter.
        Requiere: nada.
        """
        efectos_magicos = [
           "bla bla bla",
        ]

        efecto = random.choice(efectos_magicos)
        print(f"¡La poción {self.nombre} ha creado el efecto mágico: {efecto}!")
        
        # EJEMPLO

        p1 = Pocion('Poción 1', ['a', 'b'], 'e1', 'c1', 'd1')
        p1.crear_efecto_magico()

        OUTPUT: ¡La poción Poción 1 ha creado el efecto mágico: Transformar al bebedor en un animal!


'''



##PRUEBAS

# Ruta del archivo CSV
archivo_csv = 'Potions.csv'

# Lista para almacenar las instancias de Pocion
pociones = []

# Lectura del archivo CSV y creación de las instancias de Pocion
with open(archivo_csv, 'r', encoding='utf-8') as archivo:
    lector_csv = csv.DictReader(archivo, delimiter=';') # Crea un lector de CSV
    for fila in lector_csv: # Recorre las filas del archivo CSV
        nombre = fila['Name']
        ingredientes = fila['Known ingredients'].split(', ') if fila['Known ingredients'] else []
        efecto = fila['Effect']
        caracteristicas = fila['Characteristics']
        nivel_dificultad = fila['Difficulty level']
        
        p = Pocion(nombre, ingredientes, efecto, caracteristicas, nivel_dificultad) # Crea una instancia de Pocion
        pociones.append(p)


# Imprimir las pociones creadas
print("Ahora vamos a imprimir las pociones creadas")
for p in pociones:
    print(p)

#Pruebo la funcion crear efecto magico
n = random.randint(0, len(pociones)-1)
pociones[n].crear_efecto_magico()

#Pruebo comparar por menor con el método especial __lt__
n1 = random.randint(0, len(pociones)-1)
n2 = random.randint(0, len(pociones)-1)
print(pociones[n1])
print(pociones[n2])
print(pociones[n1] < pociones[n2]) 
print(pociones[n1].__lt__(pociones[n2])) 

# Pruebo imprimir con el metodo __str__
print(pociones[n1].__str__())
