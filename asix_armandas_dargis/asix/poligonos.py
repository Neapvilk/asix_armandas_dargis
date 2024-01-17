# archivo: asix_tuNombre_apellido/geometria.py

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def es_cuadrado(self):
        return self.base == self.altura


class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        import math
        return math.pi * self.radio ** 2

    def calcular_circunferencia(self):
        import math
        return 2 * math.pi * self.radio


def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura


def calcular_perimetro_cuadrado(lado):
    return 4 * lado


def calcular_volumen_cilindro(radio, altura):
    import math
    return math.pi * radio ** 2 * altura


def calcular_area_trapecio(base_menor, base_mayor, altura):
    return 0.5 * (base_menor + base_mayor) * altura
