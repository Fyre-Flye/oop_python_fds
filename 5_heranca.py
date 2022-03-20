# O conceito de herança no paradigma de POO basicamente é que uma sub-classe pode herdar
# Atributos de uma super-classe, evitando que se repita muitas linhas de código

class Veiculo():
    def __init__(self, qtd_rodas, qtd_farois, qtd_portas):
        self.rodas = qtd_rodas
        self.farois = qtd_farois
        self.portas = qtd_portas
        
# Com base na classe veiculo podemos criar várias outras classes que tem como base o próprio veiculo
# Por exemplo:
        
class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass
    
moto1 = Moto(2, 1, 0)
print(f"Esse veiculo possui: {moto1.farois} faróis! ")

carro1 = Carro(4, 2, 4)
print(f"Esse veiculo possui: {carro1.farois} faróis! ")

caminhao1 = Caminhao(6, 4, 2)
print(f"Esse veiculo possui: {caminhao1.farois} faróis! ")
