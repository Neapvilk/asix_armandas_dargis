# asix_armandas_dargis/__init__.py

from .poligonos import Rectangulo, Circulo
from .poligonos import calcular_area_triangulo, calcular_perimetro_cuadrado, calcular_volumen_cilindro, calcular_area_trapecio

__all__ = [
    'Rectangulo', 'Circulo',
    'calcular_area_triangulo', 'calcular_perimetro_cuadrado',
    'calcular_volumen_cilindro', 'calcular_area_trapecio'
]
