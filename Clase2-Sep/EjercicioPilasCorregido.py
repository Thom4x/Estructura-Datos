class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, dato):
        print(f"Agregando {dato} en la cima de la pila")
        self.items.append(dato)

    def imprimir(self):
        print("Imprimiendo pila:")
        print(self.items)

    def elimnd(self, dato_a_eliminar):
        try:
            self.items.remove(dato_a_eliminar)
        except ValueError:
            print(f" Dato erroneo-no encontrado  {dato_a_eliminar} en la pila.")

pila1 = Pila()
for i in range(11):
    pila1.apilar(i)


print("Pila original:")
pila1.imprimir()


dato_a_eliminar = int(input("Ingresa el dato que desea eliminar : "))
pila1.elimnd(dato_a_eliminar)

print(f"Dato Eliminado {dato_a_eliminar}:")
pila1.imprimir()

