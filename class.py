class Vehiculo():
 def __init__(self, color,ruedas,puertas): 
  self.color=color
  self.ruedas=ruedas
  self.puertas=puertas
 def mostrar(self):
  print('Color: ', self.color, '\nRuedas: ' , str(self.ruedas),'\nPuertas: ', str(self.puertas))
  
class Coche(Vehiculo):
 def __init__(self, velocidad,cilindrada,color,ruedas,puertas):
  super().__init__(color,ruedas,puertas)
  self.velocidad=velocidad
  self.cilindrada=cilindrada
  
 def mostrar(self):
  super().mostrar()
  print('Velocidad: ' , str(self.velocidad),'\nCilindrada: ', str(self.cilindrada))
  
c1=Coche(200,2.0,'Rojo',4,3)
c1.mostrar()