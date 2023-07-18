""" Exercício 2:
Crie uma classe chamada "Círculo" com o atributo "raio". Implemente um método chamado "calcular_area"
que calcula e retorna a área do círculo. Em seguida, crie um objeto dessa classe, informe 
o valor do raio e exiba a área calculada. """
from math import pi

class Circulo:
    def calcular_area(self,raio):
        area = pi * (raio ** 2)
        return area
    
    

cir = Circulo()
areacir = cir.calcular_area(10)

print(areacir)
