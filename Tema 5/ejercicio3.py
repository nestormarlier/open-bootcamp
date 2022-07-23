anios = []
for x in range(1584, 3000, 4):
 anios.append(x)

anio = int(input('Ingrese año: '))

if(anio >= 1582 and anio < 3001):
 for x in anios:
  if(x == anio):
   print(str(anio) + ' es año bisiesto')
   break
else:
 print('Ingrese un año desde 1582 hasta 3000.')
