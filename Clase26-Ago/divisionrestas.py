dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))

cociente = 0

for _ in range(dividendo):
    if dividendo >= divisor:
        dividendo -= divisor
        cociente += 1

print(f"El cociente de la división es: {cociente}")
print(f"El residuo de la división es: {dividendo}")
