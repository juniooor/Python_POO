""" Crie uma classe chamada "Livro" com os atributos "titulo", "autor" e "ano_publicacao". 
Implemente um método chamado "mostrar_detalhes" que exibe na tela todas as informações do livro.
Em seguida, crie um objeto dessa classe e chame o método "mostrar_detalhes". """



class Livro:
    def __init__(self, autor, titulo, ano_publicacao):
        self.autor = autor
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        
    def mostrar_detalhes(self):
        return f""" 
                    Titulo = {self.titulo}
                    Autor = {self.autor} 
                    Ano de lançamento = {self.ano_publicacao}"""   
                    
                    
livros = Livro("John green", "Cidade de papel", "2008")    

print(livros.mostrar_detalhes())             




