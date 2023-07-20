"""
    Crie uma classe chamada "ContaBancaria" com os atributos "numero" e "saldo". 
    Implemente métodos chamados "depositar" e "sacar" que atualizam o saldo da conta
    de acordo com os valores informados. Em seguida, crie um objeto dessa classe, faça depósitos 
    e saques e exiba o saldo atualizado.
    
    
    Crie uma classe chamada "ContaBancaria" que possui os atributos "numero", "titular" e "saldo".
    Implemente os métodos "sacar" e "depositar" para atualizar o saldo da conta. Em seguida, crie uma
    classe chamada "Banco" que possui uma lista de contas bancárias e os métodos "adicionar_conta" e 
    "remover_conta" para gerenciar as contas do banco.
    

    """
    
    
class ContaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
    def depositar(self, deposito):
            self.saldo += deposito
            return f' you deposited {self.saldo}'
    def sacar(self, saca):
        if saca <= self.saldo:
            self.saldo -= saca
            return f' you cashed: {saca}, your balance is : {self.saldo}' 
        else:
            return 'Value requested is higher than the available balance.'

    def mostrar_detalhes(self):
        return f""" 
            Numero da conta: {self.numero}
            Nome do titular: {self.titular}
            Saldo da conta:R${self.saldo}
                """
        
        
        
class Banco(ContaBancaria):
    def __init__(self):
        self.contas = []
        
    def adcionar_conta(self, conta):
        self.contas.append(conta)
        return True
    
    def mostrar_contas(self):
        for conta in self.contas:
            print(conta.mostrar_detalhes())
            
    def remover_conta(self, numero_conta):
        for i in self.contas:
            if i.numero == numero_conta:
                self.contas.remove(i)
                return True
        return False
        
            
conta1 = ContaBancaria('1232','junior', 10)
conta2 = ContaBancaria('1233','junior2', 10)
conta3 = ContaBancaria('1222','junior3', 10)

banco = Banco()
banco.adcionar_conta(conta1)
banco.adcionar_conta(conta2)
banco.adcionar_conta(conta3)


banco.mostrar_contas()

print(banco.remover_conta('1222'))

banco.mostrar_contas()



        



        