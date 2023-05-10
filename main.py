class DatosMeteorologicos:

    def __init__(self,nombre_archivo: str):

        self.nombre_archivo:str = nombre_archivo

    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        with open (self.nombre_archivo, "r" ) as f:
            datos = f.readlines()

