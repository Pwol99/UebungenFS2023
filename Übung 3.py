import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

class Figur:
    def __init__(self):
        self.name = "Figur"

    def Umfang(self):
        return 0

    def __str__(self):
        return self.name

class Dreieck(Figur):
    def __init__(self, a, b, c):
        super().__init__()
        self.name = "Dreieck"
        self.a = a
        self.b = b
        self.c = c

    def Umfang(self):
        return math.dist((self.a.x, self.a.y), (self.b.x, self.b.y)) + \
               math.dist((self.b.x, self.b.y), (self.c.x, self.c.y)) + \
               math.dist((self.c.x, self.c.y), (self.a.x, self.a.y))

    def __str__(self):
        return "Dreieck A={0} B={1} C={2}".format(self.a, self.b, self.c)

class Rechteck(Figur):
    def __init__(self, a, b):
        super().__init__()
        self.name = "Rechteck"
        self.a = a
        self.b = b

    def Umfang(self):
        return 2 * (abs(self.a.x - self.b.x) + abs(self.a.y - self.b.y))

    def __str__(self):
        return "Rechteck A={0} B={1}".format(self.a, self.b)

class Kreis(Figur):
    def __init__(self, m, r):
        super().__init__()
        self.name = "Kreis"
        self.m = m
        self.r = r

    def Umfang(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return "Kreis M={0} r={1}".format(self.m, self.r)

class Polygon(Figur):
    def __init__(self, *points):
        super().__init__()
        self.name = "Polygon"
        self.points = points

    def Umfang(self):
        umfang = 0
        for i in range(len(self.points) - 1):
            umfang += math.dist((self.points[i].x, self.points[i].y), (self.points[i+1].x, self.points[i+1].y))
        umfang += math.dist((self.points[-1].x, self.points[-1].y), (self.points[0].x, self.points[0].y))
        return umfang

    def __str__(self):
        points_str = ""
        for point in self.points:
            points_str += str(point) + " "
        return "Polygon Points=({0})".format(points_str)
