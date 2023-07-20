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
        
    def mostra(self):
        return self.pedidos
    
    
p = Pedido(1, 'junin')

p.adcionar('bolo', 6)
p.adcionar('coxinha', 5)

print(p.mostra())
p.remover('coxinha')
print(p.mostra())

