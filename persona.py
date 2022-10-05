class Persona:
    def __init__(self, documento=1, apellido='Fernandez', nombre='Anabel'):
        self.documento=documento
        self.apellido=apellido
        self.nombre=nombre
    #return {'documento':3,'apellido':'Trump', 'nombre':'Donald'}) with imputs
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
        

    def input(self):
        self.documento = int(input('Ingrese documento: '))
        self.apellido = input('Ingrese apellido: ')
        self.nombre = input('Ingrese nombre: ')
         
    def __repr__(self):
        return f'Persona: {self.documento} {self.apellido},{self.nombre}'
      

persona=Persona()
print(persona)