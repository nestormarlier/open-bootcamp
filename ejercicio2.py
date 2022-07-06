inicial=int(input("Ingrese un número inicial: "))
final=int(input("Ingrese un número final: "))+1 // Para que en el while tome el numero final

contador=0

while inicial != final:
    if(inicial % 2)!= 0:
        print(inicial)
    inicial = inicial + 1

print("Termino aplicacion")