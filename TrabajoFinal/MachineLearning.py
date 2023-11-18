import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Datos de ejemplo
etiquetas = ["Administración de Empresas", "Ingeniería Industrial", "Contaduría Pública", "Derecho", "Medicina",
            "Ingeniería de Sistemas", "Psicología", "Enfermería", "Comunicación Social y Periodismo", "Economía",
            "Ingeniería Civil", "Arquitectura", "Odontología", "Ingeniería Electrónica", "Ingeniería Mecánica",
            "Pedagogía", "Diseño Gráfico", "Ingeniería Ambiental", "Veterinaria", "Ingeniería Química"]

etiquetas2 = ["Bailar salsa y vallenato", "Disfrutar de la comida típica", "Fútbol", "Ciclismo", "Café",
                        "Explorar la naturaleza", "Visitar pueblos coloniales",  "Celebrar Carnaval de Barranquilla",
                        "Relajarse en las playas", "Visitar museos y galerías de arte", "Practicar deportes acuáticos",
                        "Escuchar música cumbia", "Compartir tiempo con la familia y amigos",
                        "Participar en eventos religiosos y tradicionales"]

# Creamos una matriz TF-IDF de los datos de etiquetas
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(etiquetas + etiquetas2)  # Concatenamos ambas listas

# Utilizamos K-Means para agrupar las etiquetas en clústeres
num_clusters = 3  # Número de clústeres a crear
kmeans = KMeans(n_clusters=num_clusters, random_state=42)  # Añadimos random_state para reproducibilidad
kmeans.fit(tfidf_matrix)

# Asignamos cada etiqueta a un clúster
etiquetas_clusters = pd.DataFrame({'Etiqueta': etiquetas + etiquetas2, 'Cluster': kmeans.labels_})

print(etiquetas_clusters)
# Imprimimos los resultados
"""for cluster_id in range(num_clusters):
    cluster = etiquetas_clusters[etiquetas_clusters['Cluster'] == cluster_id]
    print(f"Clúster {cluster_id}:")
    print(cluster['Etiqueta'].tolist())
    print()"""
