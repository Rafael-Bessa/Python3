class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tipo_lado(self):
        if self.a == self.b == self.c:
            return "equilátero"
        elif self.a == self.b != self.c or self.a == self.c != self.b or self.b == self.c != self.a:
            return "isósceles"
        else:
            return "escaleno"
