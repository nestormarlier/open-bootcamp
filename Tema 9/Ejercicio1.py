lista=[]
pais=input('Ingrese paises separados por coma: \n')
lista=pais.split(',')
lista=list(set(lista))
lista=(sorted(lista))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print (','.join(lista))