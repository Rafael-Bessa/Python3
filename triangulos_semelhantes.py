class Triangulo:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):

        tri1 = [self.a, self.b, self.c]
        tri2 = [triangulo.a, triangulo.b, triangulo.c]
        sorted(tri1)
        sorted(tri2)

        if tri1[0] >= tri2[0]:
            teste1 = tri1[0] % tri2[0]
        else:
            teste1 = tri2[0] % tri1[0]

        if tri1[1] >= tri2[1]:
            teste2 = tri1[1] % tri2[1]
        else:
            teste2 = tri2[1] % tri1[1]

        if tri1[2] >= tri2[2]:
            teste3 = tri1[2] % tri2[2]
        else:
            teste3 = tri2[2] % tri1[2]

        if teste1 == teste2 == teste3 == 0:
            return True
        else:
            return False
