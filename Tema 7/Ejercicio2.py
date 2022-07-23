import time

seconds= time.time()
t=time.localtime(seconds)
print(t)

#print((t.tim_hour))
hora_salida=19
if(int(t.tm_hour)<hora_salida):
    print('Falta ',(hora_salida-t.tm_hour)-1,':',(60-t.tm_min), 'Hs.')
else:
    print('Son más de las 19 hs. debe regresar a su casa.')