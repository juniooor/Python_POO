a = float(input('Digite a nota 1: '))
b = float(input('Digite a nota 2: '))
c = float(input('Digite a nota 3: '))
d = float(input('Digite a nota 4: '))
media= (a + b + c + d) /4
if a <= 10 and b<=10 and c<=10 and d<=10:
    print('A sua media foi {}'.format(media))
else:
    print('foi digitado algum valor errado, por favor reiniciar')