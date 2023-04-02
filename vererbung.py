import math

class Figur:
    def __init__(self, name):
        self.name = name

    def umfang(self):
        return 0

    def flaeche(self):
        return 0
    
    def __str__(self):
        return self.name

class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt ({self.x}, {self.y})"

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def flaeche(self):
        return self.radius**2 *math.pi
    
    def umfang(self):
        return 2 * self.radius * math.pi
    
    def __str__(self):
        return f"Kreis M={self.mittelpunkt} und Radius = {self.radius}"

class Dreieck(Figur):
    def __init__(self, a, b, c):
        super().__init__("Dreieck")
        self.a = a
        self.b = b
        self.c = c

    def Umfang(self):
        return math.dist((self.a.x, self.a.y), (self.b.x, self.b.y)) + \
               math.dist((self.b.x, self.b.y), (self.c.x, self.c.y)) + \
               math.dist((self.c.x, self.c.y), (self.a.x, self.a.y))

    def __str__(self):
        return f"Dreieck A={self.a} B={self.b} C={self.c}"

A = Punkt(1,2)
B = Punkt(2,3)
C = Punkt(3,4)


D= Dreieck(A,B,C)
print(D)
print(D.Umfang())


M = Punkt(2,3)
k1 = Kreis(M, 10)

print(k1)
print(k1.flaeche())


M.x = 5

print(k1)
k1.mittelpunkt.x = -5
print(M)