# Assim como classes podem herdar atributos (características) elas também podem herdar
# métodos (comportamentos)

class Veiculo():
    def __init__(self):
        self.tipo = self.__class__.__name__ # Acessa ao nome da classe em que é chamada
        
    def ligar(self):
        print(f'{self.tipo} está ligando... ')
        
class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    pass

moto1 = Moto()
moto1.ligar()

moto1 = Carro()
moto1.ligar()

moto1 = Caminhao()
moto1.ligar()
