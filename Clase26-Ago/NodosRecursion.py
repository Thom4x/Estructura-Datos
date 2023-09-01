import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def crear_lista_enlazada(cantidad_nodos):
    primer_nodo = None
    for _ in range(cantidad_nodos):
        dato = random.randint(1, 100)
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = primer_nodo
        primer_nodo = nuevo_nodo
    return primer_nodo

def mostrar_lista_enlazada(nodo):
    actual = nodo
    i = 1
    while actual:
        print("Nodo", i, ":", actual.dato)
        actual = actual.siguiente
        i += 1

cantidad_nodos = int(input("Ingresa la cantidad de nodos: "))
nodo_inicial = crear_lista_enlazada(cantidad_nodos)
print("Lista enlazada generada:")
mostrar_lista_enlazada(nodo_inicial)
