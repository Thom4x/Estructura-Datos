import networkx as nx
import matplotlib.pyplot as plt
from CRUD_Usuarios import crear_usuarios

lista_usuarios = crear_usuarios(70)

G = nx.DiGraph()

for usuario in lista_usuarios:
  #Nombre del grafo (G)
    G.add_node(usuario.id_aleatorio, nombre=usuario.nombre_aleatorio)

for usuario in lista_usuarios:
    for otro_usuario in lista_usuarios:
        if usuario != otro_usuario:
            if usuario.actividades1_aleatorio == otro_usuario.actividades1_aleatorio or \
               usuario.carreras_aleatorio == otro_usuario.carreras_aleatorio:
                G.add_edge(usuario.id_aleatorio, otro_usuario.id_aleatorio)

# Dibuja el grafo con un largo de arista mayor (incrementando scale)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=230, node_color='skyblue', width=0.4)
plt.show()