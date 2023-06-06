# Práctica 11: Más clases
## Nahuel Díaz - Augusto González Omahen - Luz Alba Posse - Catalina Chab

## Introducción
En la página https://www.kaggle.com/gulsahdemiryurek/harry-potter-dataset hay distintos datasets disponibles con datos relativos al universo de Harry Potter sobre personajes, pociones y hechizos, entre otras cosas. Durante la clase de hoy ejercitaremos la manipulación de datos usando los archivos Potions.csv y Potions-mini.csv, que cuentan con información sobre las distintas pociones que aparecen en la saga.

De cada poción p se tiene:
• el nombre;
• la lista de los ingredientes conocidos;
• el efecto que produce;
• sus características; y
• el nivel de dificultad de su preparación.

## Ejercicio 1
Descargar el archivo pocion.py de la página de la materia y completar la clase Pocion para que:

(a) la representación como str de una poción p sea el nombre de p;

(b) dos pociones p1 y p2 puedan compararse por menor de forma tal que p1 < p2 sea verdadero si el nombre de p1 es menor al de p2 de acuerdo al orden lexicográfico.

A continuación puede observarse un ejemplo junto a los resultados esperados:

```python
p1 : Pocion = Pocion ( ' pocion 1 ' , [ 'a ' , 'b '] , ' e1 ' , ' c1 ' , ' d1 ')
p2 : Pocion = Pocion ( ' pocion 2 ' , [ 'c ' , 'd '] , ' e2 ' , ' c2 ' , ' d2 ')
print ( p1 ) # imprime 'pocion 1 '
print ( p2 ) # imprime 'pocion 2 '
print ( p1 < p2 ) # imprime True
print ( p2 < p1 ) # imprime False
```

## Ejercicio 2
Descargar el archivo catalogo-pociones.py de la página de la materia y completar los métodos ```__init__```, ```listar_por_dificultad``` y ```listar_pociones_con_n_ingredientes``` de la clase CatalogoPociones teniendo en cuenta que:

(a) CatalogoPociones debe tener un único atributo de tipo ```Dict[str, Set[Pocion]]```, que vincula niveles de dificultad de preparación de pociones con todas las pociones de tal dificultad. (Las pociones que no tengan definida una dificultad no deben incluirse en el catálogo).

(b) ```listar_por_dificulta``` debe devolver una lista de las Pociones del catalogo que tienen la dificultad indicada por el argumento con el cual el método es invocado. Las pociones deben aparecer ordenadas siguiendo la relación < de la clase Poción. ¿Cuál es la complejidad de este método?

(c) ```listar_pociones_con_n_ingredientes``` debe devolver una lista de tuplas, dónde cada tupla guarda la Poción con n cantidad de ingredientes y su dificultad, dónde n es el argumento con el cual el método es invocado. Las tuplas que conforman la lista deben ser de la froma < difucultad, Pocion >. ¿Cuál es la complejidad de este método?