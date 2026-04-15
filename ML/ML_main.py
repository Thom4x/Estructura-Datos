import random

nombres = ["Juan", "Carlos", "Andrés", "Camila", "María", "Laura", "Lionel", "Santiago", "Valentina", "Daniela",
           "Diego", "Manuel", "Isabella", "Mateo", "Natalia", "Miguel", "Sara", "Javier", "Alejandra", "Julián",
           "Ana", "Felipe", "Paula", "David", "Adriana", "Jorge", "Gigachad", "Bartolo", "Victoria", "Gabriel"]

apellidos = ["Gómez", "Rodríguez", "De Luque", "García", "López", "Hernández", "Pérez", "Díaz", "Sánchez", "Torres",
             "Ramírez", "Rojas", "Moreno", "Jiménez", "Castro", "Ortíz", "Messi", "Vargas", "Reyes", "Mendoza"]

carreras = ["Administración de Empresas", "Ingeniería Industrial", "Contaduría Pública", "Derecho", "Medicina",
            "Ingeniería de Sistemas", "Psicología", "Enfermería", "Comunicación Social y Periodismo", "Economía",
            "Ingeniería Civil", "Arquitectura", "Odontología", "Ingeniería Electrónica", "Ingeniería Mecánica",
            "Pedagogía", "Diseño Gráfico", "Ingeniería Ambiental", "Veterinaria", "Ingeniería Química"]

actividades_colombia = ["Bailar salsa y vallenato", "Disfrutar de la comida típica", "Fútbol", "Ciclismo", "Café",
                        "Explorar la naturaleza", "Visitar pueblos coloniales",  "Celebrar Carnaval de Barranquilla",
                        "Relajarse en las playas", "Visitar museos y galerías de arte", "Practicar deportes acuáticos",
                        "Escuchar música cumbia", "Compartir tiempo con la familia y amigos",
                        "Participar en eventos religiosos y tradicionales"]

otras_actividades_colombia = ["Visitar parques nacionales y reservas naturales", "Hacer senderismo en las montañas",
                              "Explorar cuevas y cavernas", "Participar en actividades de ecoturismo",
                              "Asistir a conciertos y eventos musicales",
                              "Practicar deportes extremos como parapente y rafting",
                              "Bañarse en aguas termales",
                              "Participar en actividades de voluntariado comunitario",
                              "Disfrutar de la vida nocturna en bares y discotecas",
                              "Aprender danzas folklóricas colombianas como el currulao"]
numero_id = []
cantidad_elementos = 100
numero_id = random.sample(range(1, 150), cantidad_elementos)

# Función para generar datos aleatorios
def diferentes_datos():
    id_aleatorio = numero_id.pop()
    nombre_aleatorio = random.choice(nombres)
    apellidos_aleatorio = random.choice(apellidos)
    carreras_aleatorio = random.choice(carreras)
    actividades1_aleatorio = random.choice(actividades_colombia)
    actividades2_aleatorio = random.choice(otras_actividades_colombia)
    return id_aleatorio, nombre_aleatorio, apellidos_aleatorio, carreras_aleatorio, actividades1_aleatorio, actividades2_aleatorio

class Usuario:
    def __init__(self,nombre_aleatorio, apellidos_aleatorio, carreras_aleatorio, actividades1_aleatorio, actividades2_aleatorio, id_aleatorio ):
        self.nombre_aleatorio = nombre_aleatorio
        self.apellidos_aleatorios = apellidos_aleatorio
        self.carreras_aleatorio = carreras_aleatorio
        self.actividades1_aleatorio = actividades1_aleatorio
        self.actividades2_aleatorio = actividades2_aleatorio
        self.id_aleatorio = id_aleatorio

#Funcion recursiva que nos permite crear los usuarios
def crear_usuarios(n):
    if n == 0:
        return []
    else:
        idUsuario, nombre, apellido, carreras, actividades1, actividades2 = diferentes_datos()

        nuevo_usuario = Usuario(nombre, apellido, carreras, actividades1, actividades2, idUsuario)

        usuarios = crear_usuarios(n - 1)
        usuarios.append(nuevo_usuario)

        return usuarios
    
#Ingresar la cantidad de usuarios
cantidad_usuarios = int(input("Ingrese la cantidad de usuarios: "))
lista_usuarios = crear_usuarios(cantidad_usuarios)

# Imprimir los usuarios creados y sus datos
for usuario in lista_usuarios:
    print(f"Nombre: {usuario.nombre_aleatorio}")
    print(f"Apellidos: {usuario.apellidos_aleatorios}")
    print(f"Carrera: {usuario.carreras_aleatorio}")
    print(f"Actividad 1: {usuario.actividades1_aleatorio}")
    print(f"Actividad 2: {usuario.actividades2_aleatorio}")
    print(f"ID: {usuario.id_aleatorio}")
    print("----------------------------------------------")

def eliminar_usuario_por_id(lista_usuarios):
    id_a_eliminar = int(input("Ingrese el ID del usuario que desea eliminar: "))
    usuarios_eliminados = [usuario for usuario in lista_usuarios if usuario.id_aleatorio == id_a_eliminar]

    if usuarios_eliminados:
        lista_usuarios[:] = [usuario for usuario in lista_usuarios if usuario.id_aleatorio != id_a_eliminar]
        print(f"Se eliminaron {len(usuarios_eliminados)} usuarios con el numero del ID {id_a_eliminar}.")
    else:
        print(f"No se encontraron usuarios con el ID {id_a_eliminar}.")

eliminar_usuario_por_id(lista_usuarios)


#Funcion que nos permite crear nuevos datos que se almaceran en lista_usuarios
def agregar_usuarios_extra(lista_usuarios):
    cantidad_a_agregar = int(input("Ingrese la cantidad de usuarios que desea agregar: "))

    for _ in range(cantidad_a_agregar):
        id_usuario, nombre, apellidos, carrera, actividad1, actividad2 = diferentes_datos()
        nuevo_usuario = Usuario(nombre, apellidos, carrera, actividad1, actividad2, id_usuario)
        lista_usuarios.append(nuevo_usuario)
        print(f"Se agregó el usuario con el ID: {id_usuario}")

agregar_usuarios_extra(lista_usuarios)


# Verificar si se desea imprimir nuevamente la lista de usuarios después de eliminar y agregar nuevos usuarios
verificacion = input("¿Desea imprimir de nuevo la lista de usuarios con los cambios? (s/n):")

if verificacion.lower() == 's':
    for usuario in lista_usuarios:
        print(f"Nombre: {usuario.nombre_aleatorio}")
        print(f"Apellidos: {usuario.apellidos_aleatorios}")
        print(f"Carrera: {usuario.carreras_aleatorio}")
        print(f"Actividad 1: {usuario.actividades1_aleatorio}")
        print(f"Actividad 2: {usuario.actividades2_aleatorio}")
        print(f"ID: {usuario.id_aleatorio}")
        print("----------------------------------------------")
elif verificacion.lower() == 'n':
    print("No se imprimirá la lista de usuarios.")
else:
    print("Opción no válida. No se imprimirá la lista de usuarios.")
