import pickle 
""" Nos permite serializar y deserializar, convierte la representación de 
un programa a una seceuncia de datos que podemos escribir en un archivo en este caso binarios"""

class Vehiculo():
    def __init__(self, modelo, marca,cilindrada):
        self.modelo=modelo
        self.marca=marca
        self.cilindrada=cilindrada

    def getModelo(self):
        return self.modelo
    
    def __str__(self):
        return (f'Modelo: {self.modelo} \nMarca: {self.marca} \nCilindrada: {self.cilindrada}\n')

    def __repr__(self):
        return (f'{self.modelo} \n {self.marca} \n {self.cilindrada}')


# Vehiculo1 = Vehiculo('Focus', 'Ford', 2.0)

# f= open('datos.bin','wb') # Como quiero crear u archivo binario coloco "wb"

""" Cómo guardo yo mis datos en mis ficheros utilizando Pickle utilizando la funcion Dump,
poniendo lo que quiero serializar y dónde lo quiero hacer """
# pickle.dump(Vehiculo1,f)

# f.close()

""" Como puedo recuperar ese archivo serializado """

f= open('datos.bin', 'rb') #Como es un archivo binario lo leo con "rb"

Vehiculo = pickle.load(f) # Vehiculo es igual a cargar lo del contenido de f
f.close()

print(type(Vehiculo))
print(Vehiculo)
