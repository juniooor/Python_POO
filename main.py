from time import sleep
from funcoes import Pessoa

p1= Pessoa('Junior',29)
p1.comer('pizza')
sleep(0.5)
p1.parar_comer()
sleep(0.5)
p1.falar('comidas')
sleep(0.5)
p1.comer('coxinha')
sleep(0.5)
p1.parar_falar()
p1.comer('coxinha')
