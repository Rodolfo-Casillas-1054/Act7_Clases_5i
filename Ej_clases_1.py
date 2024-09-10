print("Introduccion a clases")
class Animal:
    edad=3
    raza = "Chihuahua"
    comida ="Croquetas"
    def come(self):
        print(f"El perro come "+self.comida)

print(Animal)
print("Creando el objeto de la clase Animal")
perro = Animal()

print(f"Edad de el perro {perro.edad}")
print(f"Raza de el perro {perro.raza}")
perro.come()