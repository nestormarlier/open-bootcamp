class Alumno():
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def datos(self):
        print('Nombre:', self.nombre, ' Nota:', self.nota)

    def resultado(self):
        if(self.nota>4):
            print('Aprobó')
        else:
            print('Desaprobó')

alu=Alumno('Nestor', 8)
alu.datos()
alu.resultado()
