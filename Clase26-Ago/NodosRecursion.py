import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.direccion = None

def crear_nodo_aleatorio(n):
    if n <= 0:
        return None
    else:
        dato_aleatorio = random.randint(1,50)  
        nodo = Nodo(dato_aleatorio)
        nodo.direccion = crear_nodo_aleatorio(n - 1)
        return nodo

def mostrar_nodos(nodo, numero_nodo=1):
    if nodo is None:
        return []
    else:
        resultado_actual = f"Nodo {numero_nodo}: {nodo.dato}"
        return [resultado_actual] + mostrar_nodos(nodo.direccion, numero_nodo + 1)

num_nodos = int(input("Ingrese la cantidad de nodos a crear: "))
print("-"*45)
print(f"La cantidad de nodos creados son: {num_nodos}")
nodo_inicial = crear_nodo_aleatorio(num_nodos)
datos_nodos = mostrar_nodos(nodo_inicial)

for dato in datos_nodos:
    print(dato)
print("-"*45)
