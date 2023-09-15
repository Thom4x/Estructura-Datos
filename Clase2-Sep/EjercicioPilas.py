class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        print(f"Agregando {dato} en la cima de la pila")  
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def imprimir(self):
        print("Imprimiendo pila:")
        # Recorrer la pila e imprimir valores
        nodo_temporal = (self.superior) 
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")

    def eliminar_nodo(self, dato_a_eliminar):
        if self.superior.dato == dato_a_eliminar:
            self.superior = self.superior.siguiente
            return

        nodo_temporal = self.superior
        while (nodo_temporal.siguiente is not None and nodo_temporal.siguiente.dato != dato_a_eliminar):
            nodo_temporal = nodo_temporal.siguiente

        if nodo_temporal.siguiente is not None:
            nodo_temporal.siguiente = nodo_temporal.siguiente.siguiente
        else:
            print(f"No se encontró el dato {dato_a_eliminar} en la pila.")

pila1 = Pila()
pila1.apilar(0)
pila1.apilar(1)
pila1.apilar(2)
pila1.apilar(3)

print("-"*50)
print("Pila original:")
pila1.imprimir()
print("-"*50)

dato_a_eliminar = int(input("Ingrese el numero de la pila que desea eliminar dentro del rango de 0-10: "))  
pila1.eliminar_nodo(dato_a_eliminar)

print(f"Pila después de eliminar el dato {dato_a_eliminar}:")
pila1.imprimir()
print("-"*50)
