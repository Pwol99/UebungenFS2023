from math import *
class Figur:
    def __init__(self, name):
        self.name = name
        
    def umfang(self):
        return 0
    
    def flaeche(self):
        return 0
    
    def __str__(self):
        return f"{self.name}"

    
class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f"[{self.name}, x={self.x}, y={self.y}]"

    
class Vector2(Figur):
    def __init__(self, x, y):
        super().__init__("Vector2")
        self.x = x
        self.y = y
    
    def cross(self, other):
        return abs(self.x * other.y - self.y * other.x)
    
    
class Dreieck(Figur):
    def __init__(self, Ax, Ay, Bx, By, Cx, Cy):
        super().__init__("Dreieck")
        self.A = Punkt(Ax, Ay)
        self.B = Punkt(Bx, By)
        self.C = Punkt(Cx, Cy)

    def flaeche(self):
        v1 = (self.B - self.A)
        v2 = (self.C - self.A)
        return v1.cross(v2) / 2
        
    def __str__(self):
        return f"[{self.A}, {self.B}, {self.C}]"

    def umfang(self):
        return self.A.dist(self.B) + self.B.dist(self.C) + self.C.dist(self.A)

class Rechteck(Figur):
    def __init__(self,ax,ay,bx,by):
        super().__init__("Rechteck")
        self.A = Punkt(ax,ay)
        self.C = Punkt(bx,by)
        self.D = Punkt(ax,by)
        self.B = Punkt(bx,ay)



    def umfang(self):
        return self.A.dist(self.B)+self.B.dist(self.C)+self.C.dist(self.D)+self.D.dist(self.A)

    def flaeche(self):
        v1 = (self.B - self.A)
        v2 = (self.D - self.A)
        v3 = (self.B - self.C)
        v4 = (self.D - self.C)
        return v1.cross(v2) / 2 + v3.cross(v4)/2

class Kreis (Figur):
    def __init__ (self,mx,my,r):
        super().__init__("Kreis")
        self.m=Punkt(mx,my)
        self.r=r
        
    def flaeche(self):
        return self.r**2*pi
    
    def umfang(self):
        return self.r*2*pi

class Polygon(Figur):
    def __init__(self,*args):
        super().__init__("Polygon")
        self.punkte=[]
        for i in range(0,len(args),2):
            x,y=args[i],args[i+1]
            self.punkte.append(Punkt(x,y))

    def umfang(self):
        umfang = 0
        for i in range(len(self.punkte)):
            x = (i+1)%len(self.punkte)
            seite=self.punkte[i].dist(self.punkte[x])
            umfang += seite
        return umfang
        
    def flaeche(self):
        flaeche= 0
        for i in range(len(self.punkte)):
            x=(i+1)%len(self.punkte)
            flaeche+=self.punkte[i].x*self.punkte[x].y
            flaeche-=self.punkte[i].y*self.punkte[x].x
        return abs(flaeche/2)
            
        

p = Punkt(1, 2)
d = Dreieck(0, 0, 0, 2, 2, 2)
r=Rechteck(0,0,2,2)
k=Kreis(0,0,10)
test=Polygon(0,0,0,2,2,2,2,0,2,-2,0,-2)
print(d.umfang())
print(d.flaeche())
print(r.umfang())
print(r.flaeche())
print(k.flaeche())
print(k.umfang())
print(test.umfang())
print(test.flaeche())