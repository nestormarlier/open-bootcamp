class Verdura():
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def __str__(self):
        return f'Mi nombre es {self.nombre} y mi precio {self.precio}'

    def __repr__(self):
        return f'Verdura: {self.nombre} , {self.precio}'

p1 = Verdura('Batata', 95.5)

print(p1)
print(p1.__repr__)
    
    