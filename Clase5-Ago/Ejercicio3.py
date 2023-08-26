class Vehiculo:

  marca: str
  combustible: str
  tipo: str

  def __init__(self, tipo, marca, combustible):
    self.marca = marca 
    self.combustible = combustible
    self.tipo = tipo

  def encender(self):
    pass

  def arrancar(self):
    pass

  def __str__(self):
    return "El {} de marca {} necesita gasolina {} para operar".format(self.tipo, self.marca, self.combustible)


class Carro(Vehiculo):
  pass

class Moto(Vehiculo):
    pass

carro=Carro('Carro', 'Mazda', 'Corriente')
print(carro)

moto=Moto('Moto', 'Yamaha', 'Corriente')
print(moto)
