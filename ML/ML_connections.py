import pandas as pd
from CRUD_Usuarios import crear_usuarios

lista_usuarios = crear_usuarios(70)

motivos = ['Actividades 1', 'Actividades 2', 'Carreras']

'''
Esta funcion recorre los motivos predefinidos en la lista motivos y para cada motivo, examina la lista de usuarios para encontrar
conexiones entre ellos según el motivo específico
'''

for motivo in motivos:
    conexiones = []
    for usuario in lista_usuarios:
        for otro_usuario in lista_usuarios:
            if usuario != otro_usuario:
                if motivo == 'Actividades 1' and usuario.actividades1_aleatorio == otro_usuario.actividades1_aleatorio:
                    conexiones.append([usuario.id_aleatorio, otro_usuario.id_aleatorio, 'Actividades 1'])
                elif motivo == 'Actividades 2' and usuario.actividades2_aleatorio == otro_usuario.actividades2_aleatorio:
                    conexiones.append([usuario.id_aleatorio, otro_usuario.id_aleatorio, 'Actividades 2'])
                elif motivo == 'Carreras' and usuario.carreras_aleatorio == otro_usuario.carreras_aleatorio:
                    conexiones.append([usuario.id_aleatorio, otro_usuario.id_aleatorio, 'Carreras'])

# Crear DataFrame de Pandas para mostrar las conexiones con sus motivos
    if conexiones:
        df = pd.DataFrame(conexiones, columns=['ID Perfil 1', 'ID Perfil 2', 'Motivo'])
        print(f"DataFrame para {motivo}:")
        with pd.option_context('display.max_rows', 100):
            print(df)
            print("\n")
