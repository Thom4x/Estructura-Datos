import requests

url = 'https://fantastic-computing-machine-7vprgqq7r5gcxjrj-8000.app.github.dev'

# Ejemplo de solicitud GET
r = requests.get(url)
print(r.text)

# Ejemplo de solicitud POST
r = requests.post(url + 'encolar', json={'nombre': 'Juan', 'productos': ['manzana', 'pera'],"Id":12345})

print(r.text)
