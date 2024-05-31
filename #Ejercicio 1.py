#Ejercicio 1

numeros = [1, 2, 3, 4, 5]
def sumar_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma


resultado = sumar_lista(numeros)
print("La suma de los números en la lista es:", resultado)