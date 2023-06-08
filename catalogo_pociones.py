from pocion import Pocion

class CatalogoPociones:
    def __init__(self, ruta_archivo):
        self.pociones = []
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()[1:] # Ignorar la primera línea (encabezado)
            for linea in lineas:
                campos = linea.strip().split(';')
                if len(campos) >= 5: # Verificar que haya al menos 5 campos
                    nombre, ingredientes, efecto, caracteristicas, dificultad = campos
                    p = Pocion(nombre, ingredientes.split(', '), efecto, caracteristicas, dificultad)
                    self.pociones.append(p)

    def listar_por_dificultad(self, dificultad):
        pociones_filtradas = [p for p in self.pociones if p.nivel_dificultad == dificultad]
        return pociones_filtradas

    def listar_pociones_con_n_ingredientes(self, n):
        pociones_filtradas = [(p.nivel_dificultad, p) for p in self.pociones if len(p.ingredientes) == n]
        return pociones_filtradas

    def exportar_csv_dificultad(self, dificultad):
        pociones_filtradas = self.listar_por_dificultad(dificultad)
        nombre_archivo = f"POCIONES_{dificultad}.csv"
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("Name;Known ingredients;Effect;Characteristics;Difficulty level\n")
            for p in pociones_filtradas:
                linea = f"{p.nombre};{', '.join(p.ingredientes)};{p.efecto};{p.caracteristicas};{p.nivel_dificultad}\n"
                archivo.write(linea)

    def crear_efecto_magico(self, nombre_pocion):
        for p in self.pociones:
            if p.nombre == nombre_pocion:
                return f"Se creó un efecto mágico usando la poción '{nombre_pocion}': {p.efecto}"
        return f"No se encontró la poción '{nombre_pocion}' en el catálogo"
