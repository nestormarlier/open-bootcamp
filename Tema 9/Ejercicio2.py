import functools
import operator

def impar(a):
    if a%2!=0:
        return a

lista = []
lista.append(int(input("Ingrese los números a evaluar 0 para terminar: ")))

i=0
while lista[i] != 0:
    valor=int(input("Ingrese los números a evaluar 0 para terminar: "))
    if valor != 0:
        lista.append(valor)
        i=i+1
        print(lista)
    else:
        break

print(f'Elementos ingresados: {lista}')

impares=list(filter(lambda x: impar(x), lista))

print(f'Elementos impares {impares}')

print(f'Suma de los números impares {functools.reduce(operator.add,impares)}')

