"""
    Crie uma classe chamada "ContaBancaria" com os atributos "numero" e "saldo". 
    Implemente métodos chamados "depositar" e "sacar" que atualizam o saldo da conta
    de acordo com os valores informados. Em seguida, crie um objeto dessa classe, faça depósitos 
    e saques e exiba o saldo atualizado.
    
    """
    
    
class ContaBancaria:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
    def depositar(self,numero , deposito):
        if numero == self.numero:
            self.saldo += deposito
            return f' you deposited {self.saldo}'
        else:
            return f'numero de conta inexistente'  
    def sacar(self, numero, saca):
        if numero == self.numero:
            self.saldo -= saca
            return f' you cashed: {saca}, your balance is : {self.saldo}' 
        else:
            return 'account number invalid'
        
conta1 = ContaBancaria('1232', 0) 

print(conta1.depositar('1232', 50))
print(conta1.sacar('123', 10))




        