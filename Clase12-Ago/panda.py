import pandas as pd

class CargarDatos:
    def __init__(self, url, nombre):
        self.url = url
        self.nombre = nombre

    def cargar_datos(self):
        df = pd.read_csv(self.url, sep=";")
        return df.apply(pd.to_numeric, errors='ignore')

    def contar_datos(self, columna):
        df = self.cargar_datos()
        cantidad = df[columna].count()
        return cantidad

def calcular_promedio_cantidad(url):
    cargador = CargarDatos(url, "Encuesta Cultura 2013")

    cantidad_calidad = cargador.contar_datos("acu_cal_cla")
    cantidad_culpabilidad = cargador.contar_datos("acu_id_culp")

    promedio = (cantidad_calidad + cantidad_culpabilidad) / 2

    return cantidad_calidad, cantidad_culpabilidad, promedio

archivo = "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2013.csv"
cantidad_calidad, cantidad_culpabilidad, promedio = calcular_promedio_cantidad(archivo)

print("Cantidad de datos en Calidad:", cantidad_calidad)
print("Cantidad de datos en Culpabilidad:", cantidad_culpabilidad)
print("Promedio entre Calidad y Culpabilidad:", promedio)
