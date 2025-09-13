import math
from multimethod import multimethod
class AlgebraVectorial:
    def __init__(self, x, y, z=0):
        self.x = x
        self.y = y
        self.z = z
    
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y and self.z == otro.z
    
    def __add__(self, otro):
        return AlgebraVectorial(self.x + otro.x, self.y + otro.y, self.z + otro.z)
    
    def __sub__(self, otro):
        return AlgebraVectorial(self.x - otro.x, self.y - otro.y, self.z - otro.z)
    
    def __mul__(self, scalar):
        return AlgebraVectorial(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def producto_punto(self, otro):
        return self.x * otro.x + self.y * otro.y + self.z * otro.z
    
    def producto_cruz(self, otro):
        return AlgebraVectorial(
            self.y * otro.z - self.z * otro.y,
            self.z * otro.x - self.x * otro.z,
            self.x * otro.y - self.y * otro.x
        )
    # a)
    @multimethod
    def es_perpendicular(self, otro):
        suma = self + otro
        resta = self - otro
        return suma.magnitud() == resta.magnitud()
    # b),c),d)
    @multimethod
    def es_perpendicular(self, otro, metodo: str):
        if metodo == "b":
            resta1 = self - otro
            resta2 = otro - self
            return resta1.magnitud() == resta2.magnitud()
        elif metodo == "c":
            return self.producto_punto(otro) == 0
        elif metodo == "d":
            suma = self + otro
            return suma.magnitud()**2 == (self.magnitud()**2 + otro.magnitud()**2)
        else:
            raise ValueError("Método debe ser b,c o d")
    # e)
    @multimethod
    def es_paralela(self, otro):
        if otro.magnitud() == 0:
            return self.magnitud() == 0
        r = None
        if otro.x != 0:
            r = self.x / otro.x
        elif otro.y != 0:
            r = self.y / otro.y
        elif otro.z != 0:
            r = self.z / otro.z
        else:
            return False
        esperado = otro * r
        return self == esperado
    # f)
    @multimethod
    def es_paralela(self, otro, metodo: str):
        if metodo == "f":
            return self.producto_cruz(otro) == AlgebraVectorial(0, 0, 0)
        else:
            raise ValueError("Método debe ser 'f'")
    # g)
    def proyeccion_sobre(self, otro):
        if otro.magnitud() == 0:
            return AlgebraVectorial(0, 0, 0)
        escalar = self.producto_punto(otro) / (otro.magnitud()**2)
        return otro * escalar
    # h)
    def componente_en_direccion(self, otro):
        if otro.magnitud() == 0:
            return 0
        return self.producto_punto(otro) / otro.magnitud()
    
    def __str__(self):
        if self.z == 0:
            return f"Vector({self.x}, {self.y})"
        return f"Vector({self.x}, {self.y}, {self.z})"

a = AlgebraVectorial(1, 0)
b = AlgebraVectorial(0, 5)
c = AlgebraVectorial(4, 4)
d = AlgebraVectorial(3, 3)

print("PERPENDICULARIDAD")
print(f"a es perpendicular a b (método a): {a.es_perpendicular(b)}")
print(f"a es perpendicular a b (método b): {a.es_perpendicular(b, 'b')}")
print(f"a es perpendicular a b (método c): {a.es_perpendicular(b, 'c')}")
print(f"a es perpendicular a b (método d): {a.es_perpendicular(b, 'd')}")

print("\nPARALELISMO")
print(f"c es paralela a d (método e): {c.es_paralela(d)}")
print(f"c es paralela a d (método f): {c.es_paralela(d, 'f')}")
