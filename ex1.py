""" Crie uma classe chamada "Pessoa" com os atributos "nome" e "idade". 
Em seguida, crie um objeto dessa classe e exiba os valores dos atributos na tela """



class Peaples:
    def __init__(self, nome, idade,):
        self.nome = nome 
        self.idade = idade 
        self.falando = False
        self.comendo = False
    def falar(self, falar, ):
        self.falar = falar 
        self.falando = True 
        
        return f' {self.nome}, está falando: {self.falar} '




print(f'#'*90 , '\n ')


p1 = Peaples('junin', '22')

print(p1.falar('oi gente!!'))

