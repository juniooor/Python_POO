from audioop import mul
from fcalculadora import Calculadora



calu=Calculadora()
subtrair= calu.subtracao(5,2)
divisao= calu.divisao(10,2)
somar= calu.soma(6,5)
multi= calu.multiplicacao(2,4)

print(f'A soma foi {somar}')
print(f'A subtração foi {subtrair}')
print(f'A multiplicação foi {multi}')
print(f'A divisão foi {divisao}')