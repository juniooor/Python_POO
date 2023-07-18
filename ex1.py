""" Crie uma classe chamada "Pessoa" com os atributos "nome" e "idade". 
Em seguida, crie um objeto dessa classe e exiba os valores dos atributos na tela """



class Peaples:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 
        


p = Peaples('junin', '22')

print(p.nome, p.idade )