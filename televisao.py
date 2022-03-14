class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def power(self):
        if self.ligada:
            print('Desligando a televisão')
            self.ligada = False
        else:
            print('Ligando a televisão')
            self.ligada=True
    def canal_up(self):
        if self.ligada == True:
            self.canal+=1
            print(f'subiu para o canal {self.canal}')
        else:
            print('A tv está desligada, ligue para mudar de canal')
    
    def canal_down(self):
        if self.ligada == True:
            self.canal-=1
            print(f'Diminuiu para o canal {self.canal}')
        else:
            print('A tv está desligada, ligue para mudar de canal')
