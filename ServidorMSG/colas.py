from .tipos import Item

class Nodo:
    def __init__(self, valor,item):
        self.valor = valor
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def esta_vacia(self):
        return self.primero is None

    def encolar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.esta_vacia():
            self.primero = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
        self.ultimo = nuevo_nodo
    
    def desencolar(self):
        if self.esta_vacia():
            return None
        valor = self.primero.valor
        self.primero = self.primero.siguiente
        if self.primero is None:
            self.ultimo = None
        return valor
    
    def ver_listado(self):
        elementos = []
        actual = self.primero
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

    def ver_ultimo(self):
        if self.ultimo:
            return self.ultimo.valor
        else:
            return None

    def contar(self):
        count = 0
        actual = self.primero
        while actual:
            count += 1
            actual = actual.siguiente
        return count
