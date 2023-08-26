numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

resultado_multiplicacion = 0

for _ in range(numero2):
    resultado_multiplicacion += numero1

print(f"La multiplicación de {numero1} y {numero2} es: {resultado_multiplicacion}")
