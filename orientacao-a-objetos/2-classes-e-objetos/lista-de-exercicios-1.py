# Crie uma classe que modele o objeto "carro".
class Carro:
    def __init__(self,modelo,cor):
        self.ligado = False
        self.velocidade = 0
        self.modelo = modelo 
        self.cor = cor

    def ligar(self):
        self.ligado = True
        print ('o carro esta ligado')
    
    def desliga(self):
        self.ligado = False
        print ('o carro esta desligado')  

    def status(self):
        print(f"Modelo: {self.modelo}")
        print(f"Cor: {self.cor}")

meu_carro = Carro("Corolla", "Prata")
meu_carro.ligar()
meu_carro.status()

# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.



# Crie uma instância da classe carro.


# Faça o carro "andar" utilizando os métodos da sua classe.


# Faça o carro "parar" utilizando os métodos da sua classe.