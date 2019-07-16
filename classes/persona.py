
class Persona:
    edad = 0

    def __init__(self, un_nombre):
        self.mi_nombre = un_nombre
        print("Hola naci, me llamo", self.mi_nombre)
    
    def cumple(self):
        self.edad = self.edad + 1
    
    def apellido(self):
        self.ap = un_ap
        print("Mi apellido es", un_ap)

pepe = Persona("Pepito")
pepa = Persona("Pepita")

print(pepe.edad)
print(pepe.mi_nombre)

pepe.cumple()
print(pepe.edad)