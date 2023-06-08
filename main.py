import csv
from pocion import Pocion
from catalogo_pociones import CatalogoPociones

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

catalogo = CatalogoPociones(pociones)
''' # Crear un catálogo de pociones a partir de un archivo CSV con init 
print("Ahora vamos a crear un catálogo de pociones a partir de un archivo CSV con init")

# Listar las pociones de una determinada dificultad
print("Ahora vamos a listar las pociones de una determinada dificultad")
dificultad = 'Beginner'
pociones_dificultad = catalogo.listar_por_dificultad(dificultad)
for p in pociones_dificultad:
    print(p)

# Listar las pociones con un número específico de ingredientes
print("Ahora vamos a listar las pociones con un número específico de ingredientes e imprimir su dificultad")
n_ingredientes = 2
pociones_ingredientes = catalogo.listar_pociones_con_n_ingredientes(n_ingredientes)
for dificultad, p in pociones_ingredientes:
    print(f"Dificultad: {dificultad}, Poción: {p}")
# Salida:
# Dificultad: Beginner, Poción: Poción Cure for Boils
# Dificultad: Beginner, Poción: Poción Fire Protection Potion

# Exportar las pociones de una dificultad específica a un archivo CSV
catalogo.exportar_csv_dificultad('Beginner')
# Se creará un archivo llamado POCIONES_Beginner.csv
'''
# Crear un efecto mágico utilizando una poción del csv # Blood-Replenishing Potion;;Replenishes lost blood;Dark red in colour;
nombre = "Blood-Replenishing Potion"
efecto_magico = catalogo.crear_efecto_magico(nombre)
print(f"Se creó un efecto mágico usando la poción '{nombre}': {efecto_magico}")
