class Vehiculo:

  marca: str
  combustible: str

  def __init__(self, marca, combustible):
    self.marca = marca 
    self.combustible = combustible

  def encender(self):
    pass

  def arrancar(self):
    pass

  def __str__(self):
    return "El vehiculo {} necesita gasolina {} para operar".format(self.marca, self.combustible)


class Auto(Vehiculo):
  pass

class Moto(Vehiculo):
    pass

carra=Auto('Mazda', 'Corriente')
print(carra)

moto=Moto('Yamaha', 'Corriente')
print(moto)
