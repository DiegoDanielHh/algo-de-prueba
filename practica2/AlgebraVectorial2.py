import math
class AlgebraVectorial:
    def __init__(self, a1, a2, a3=0):
        self.a1 = a1
        self.a2 = a2  
        self.a3 = a3
     
    def __eq__(self, otro):
        return self.a1 == otro.a1 and self.a2 == otro.a2 and self.a3 == otro.a3
    # a)
    def __add__(self, otro):
        return AlgebraVectorial(
            self.a1 + otro.a1,
            self.a2 + otro.a2,
            self.a3 + otro.a3
        )
    def __sub__(self, otro):
        return AlgebraVectorial(
        self.a1 - otro.a1,
        self.a2 - otro.a2,
        self.a3 - otro.a3
    )
    # b)
    def __mul__(self, escalar):
        return AlgebraVectorial(
            self.a1 * escalar,
            self.a2 * escalar,
            self.a3 * escalar
        )
    
    def __rmul__(self, escalar):
        return self.__mul__(escalar)
    # c) 
    def magnitud(self):
        return math.sqrt(self.a1**2 + self.a2**2 + self.a3**2)
    # d) 
    def normalizar(self):
        mag = self.magnitud()
        if mag == 0:
            return AlgebraVectorial(0, 0, 0)
        return AlgebraVectorial(
            self.a1 / mag,
            self.a2 / mag,
            self.a3 / mag
        )
    # e)
    def producto_punto(self, otro):
        return self.a1 * otro.a1 + self.a2 * otro.a2 + self.a3 * otro.a3
    # f)
    def producto_cruz(self, otro):
        return AlgebraVectorial(
            self.a2 * otro.a3 - self.a3 * otro.a2,
            self.a3 * otro.a1 - self.a1 * otro.a3,
            self.a1 * otro.a2 - self.a2 * otro.a1
        )

    def verifica_paralelogramo_rectangulo(self, otro):
        diagonal1 = (self + otro).magnitud()
        diagonal2 = (self - otro).magnitud()
        return diagonal1 == diagonal2
    
    def __str__(self):
        if self.a3 == 0:
            return f"Vector({self.a1}, {self.a2})"
        return f"Vector({self.a1}, {self.a2}, {self.a3})"

a = AlgebraVectorial(3, 4, 0)
b = AlgebraVectorial(4, -3, 0)
    
print("a) Suma de vectores:")
c=a+b
print(f"c=a+b= {c}")
    
print("\nb) Multiplicación por escalar:")
r=2
resultado=r*a
print(f"b={r}*a= {resultado}")
    
print("\nc) Magnitud del vector:")
print(f"|a|= {a.magnitud()}")
    
print("\nd) Vector normal:")
normal = a.normalizar()
print(f"Vector unitario= {normal}")
    
print("\ne) Producto escalar:")
producto_esc = a.producto_punto(b)
print(f"a·b = {producto_esc}")
    
print("\nf) Producto vectorial:")
producto_vec=a.producto_cruz(b)
print(f"a×b={producto_vec}")
    
print("\nParalelogramo:")
esrectangulo = a.verifica_paralelogramo_rectangulo(b)
print(f"¿Las diagonales del paralelogramo son iguales? {esrectangulo}")
if esrectangulo:
    print("Los vectores son perpendiculares")
else:
    print("Los vectores no son perpendiculares")