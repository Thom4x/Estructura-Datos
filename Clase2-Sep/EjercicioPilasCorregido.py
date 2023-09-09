class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cabeza = None

    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

    def eliminar(self, dato_a_eliminar):
        if self.cabeza is None:
            return

        if self.cabeza.dato == dato_a_eliminar:
            self.cabeza = self.cabeza.siguiente
            return

        nodo_actual = self.cabeza
        while nodo_actual.siguiente is not None and nodo_actual.siguiente.dato != dato_a_eliminar:
            nodo_actual = nodo_actual.siguiente

        if nodo_actual.siguiente is not None:
            nodo_actual.siguiente = nodo_actual.siguiente.siguiente

pila1 = Pila()
for i in range(11):
    pila1.apilar(i)

print("Pila original (de arriba hacia abajo):")
pila1.imprimir()

dato_a_eliminar = int(input("Ingresa el dato que deseas eliminar: "))
pila1.eliminar(dato_a_eliminar)

print("Pila después de eliminar el dato (de arriba hacia abajo):")
pila1.imprimir()
