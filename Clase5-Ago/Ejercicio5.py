class Vehiculo:
    def __init__(self, combustible_inicial, nivel_advertencia, consumo_por_km):
        self.combustible = combustible_inicial
        self.nivel_advertencia = nivel_advertencia
        self.consumo_por_km = consumo_por_km
        self.marcha_encendida = False

    def encender_marcha(self):
        self.marcha_encendida = True

    def apagar_marcha(self):
        self.marcha_encendida = False

    def avanzar(self, distancia):
        if self.marcha_encendida:
            consumo = self.consumo_por_km * distancia
            if consumo > self.combustible:
                consumo = self.combustible
            self.combustible -= consumo
            if self.combustible <= 0:
                self.combustible = 0
                self.apagar_marcha()
                print("El vehículo se ha quedado sin combustible y se detuvo.")
            elif self.combustible <= self.nivel_advertencia:
                print("Advertencia: Nivel bajo de combustible.")

    def obtener_combustible(self):
        return self.combustible

# Crear un vehículo con 100 litros de combustible, advertencia a los 20 litros y consumo de 10 km por litro.
vehiculo = Vehiculo(combustible_inicial=100, nivel_advertencia=20, consumo_por_km=10)

# Encender la marcha
vehiculo.encender_marcha()

# Avanzar 300 km
vehiculo.avanzar(distancia=300)
print(f"Combustible restante: {vehiculo.obtener_combustible()} litros")

# Avanzar 150 km más
vehiculo.avanzar(distancia=150)
print(f"Combustible restante: {vehiculo.obtener_combustible()} litros")

# Avanzar 100 km más (esto debería detener el vehículo)
vehiculo.avanzar(distancia=100)
print(f"Combustible restante: {vehiculo.obtener_combustible()} litros")
Este ejemplo crea una clase Vehiculo con métodos para encender/apagar la marcha, avanzar y obtener el nivel de combustible. El vehículo consume combustible según la distancia avanzada y muestra advertencias y mensajes de detención según los niveles de combustible definidos.

Ten en cuenta que este es solo un ejemplo simple y simulado. En un caso real, se necesitarían mediciones más precisas y consideraciones adicionales para reflejar con mayor precisión el comportamiento de un vehículo y su consumo de combustible.





