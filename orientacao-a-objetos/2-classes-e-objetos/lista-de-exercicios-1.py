# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
    def __init__(self,modelo,cor):
        self.ligado = False
        self.velocidade = 0
        self.modelo = modelo 
        self.cor = cor

    def ligar(self):
        self.ligado = True
        print ('o carro esta ligado')
    
    def desligar(self):
        self.ligado = False
        print ('o carro esta desligado')  

    def acelera(self, velocidade):
        if self.ligado == True:
            if velocidade > 0:
                self.velocidade += velocidade
                print(f'o carro acelerou para {self.velocidade}')
            else:
                print(' a velocidade nao pode ser zero ou negativa')
        else:
            print('ligue o carro antes de acelerear')

    def desacelera(self, velocidade):
        if self.ligado == True:
            if velocidade > 0 and self.velocidade >= velocidade:
                self.velocidade -= velocidade
                print(f'o carro desacelerou para {self.velocidade}')
            elif velocidade <=0:
                print('a velocidade nao pode ser menora zero') 
            else:
                print('a velocidade de desaceleracao nao pode ser maior que a atual')

        else:
            print('ligue o carro antes de desacelerar')


    def status(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")

# Crie uma instância da classe carro.

meu_carro = Carro("Corolla", "Prata")

# Faça o carro "andar" utilizando os métodos da sua classe.
meu_carro.acelera(20)
meu_carro.ligar()
meu_carro.acelera(20)
meu_carro.desacelera(10)
meu_carro.desacelera(100)
# Faça o carro "parar" utilizando os métodos da sua classe.
meu_carro.desligar()
meu_carro.desacelera(10)
meu_carro.status()










