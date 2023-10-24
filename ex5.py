# Exercício 3: Sistema de Pedidos

# Crie uma classe chamada "Pedido" com os atributos "id_pedido", "cliente" e "itens".
# Implemente métodos para adicionar e remover itens do pedido, calcular o valor total 
# do pedido e exibir os detalhes do pedido.
# Crie uma classe chamada "SistemaPedidos" que gerencia uma lista de pedidos e permite adicionar,
# remover e exibir os pedidos.



class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.itens = str
        self.valor = float
        self.pedidos = {}
       
    def adcionar(self, itens, valor):
        self.pedidos[itens] = valor
        return True
    
    def remover(self, itens):
        self.pedidos.pop(itens)
        return True
        
    def somar(self):   
        return sum(self.pedidos.values())
      
    def detalhes(self):
        return f"""
                    PEDIDO NUMERO {self.id_pedido}
                        Cliente: {self.cliente}  
                        
                        produto: {self.pedidos.keys()}  || {self.pedidos.values()}
                        
                        
                        total: {sum(self.pedidos.values())}
                        """ 
class SistemaDePedidos(Pedido):
    def exibir(self):
        return Pedido.detalhes()
    
    
     
p = Pedido(1, 'junin')
p2 = Pedido(2, 'letici')

p.adcionar('bolo', 6)
p.adcionar('coxinha', 5)
p2.adcionar('empada', 4)
p2.adcionar('refri', 7)

ps = SistemaDePedidos()

print(SistemaDePedidos.exibir(p))


