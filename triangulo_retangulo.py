class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            maior_lado = self.a
        elif self.b > self.a and self.b > self.c:
            maior_lado = self.b
        else:
            maior_lado = self.c

        if maior_lado == self.a:
            if self.a == (self.b ** 2 + self.c ** 2) ** 0.5:
                return True
            else:
                return False

        elif maior_lado == self.b:
            if self.b == (self.a ** 2 + self.c ** 2) ** 0.5:
                return True
            else:
                return False

        else:
            if self.c == (self.b ** 2 + self.a ** 2) ** 0.5:
                return True
            else:
                return False
