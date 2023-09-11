import requests

url = 'https://refactored-chainsaw-r4prpp99jwc5rvq-8000.app.github.dev/'

# Ejemplo de solicitud GET
r = requests.get(url)
print(r.text)

# Ejemplo de solicitud POST
r = requests.post(url + 'encolar', json={'nombre': 'Juan', 'productos': ['manzana', 'pera']})
print(r.text)
