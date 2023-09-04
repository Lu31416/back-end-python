# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".
class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
    self.nome = nome
    self.telefone = telefone
    self.renda_mensal = renda_mensal


class ClienteMulher(cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.cheque_especial = renda_mensal
     

class Conta:
    def __init_(self):
    self.titulares = []
    self.saldo = 0

    def saque(self):
        for titular in self.titulares:
            if titular.mulher:
                saldo_disponivel = self.saldo + cheque_especial
            else
        if saldo > 0
            saldo -= extracao
            print ('voce extraiu {extracao}, seu novo saldo é{saldo}')
        else print ()



contas devem ter um ou mais clientes
clientes: nome, telefone, renda mensal
conta: saldo, operacoes: saque: dimunie saldo, deposito, aumenta o saldo
cliente mulher pode fazer saque ate -renda mensal
cliente homem nao pode
