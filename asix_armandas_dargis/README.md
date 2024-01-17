# asix_armandas_dargis

Este es un paquete de Python que proporciona funciones y clases para cálculos geométricos simples, incluyendo áreas y perímetros de figuras geométricas.

## Instalación

Puedes instalar este paquete utilizando pip:

pip install asix_armandas_dargis

## Uso de la clase Rectangulo

from asix_armandas_dargis.poligonos import Rectangulo

rectangulo = Rectangulo(5, 10)
area = rectangulo.calcular_area()
perimetro = rectangulo.calcular_perimetro()

print(f'Área del rectángulo: {area}')
print(f'Perímetro del rectángulo: {perimetro}')

## Uso de la clase Circulo

from asix_armandas_dargis.poligonos import Circulo

circulo = Circulo(7)
area = circulo.calcular_area()
circunferencia = circulo.calcular_circunferencia()

print(f'Área del círculo: {area}')
print(f'Circunferencia del círculo: {circunferencia}')

## Uso de funciones independientes

from asix_tuNombre_apellido.geometria import calcular_area_triangulo

base = 6
altura = 4
area_triangulo = calcular_area_triangulo(base, altura)

print(f'Área del triángulo: {area_triangulo}')
