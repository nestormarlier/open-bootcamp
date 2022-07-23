
texto=input('Ingrese texto: ')

f = open('fichero.txt', 'a') # a Append agrega, w Write escribe pero borra lo escrito antes

if f != '\n':
    f.write(texto + '\n')
else:
    f.write(texto)
f.close()
