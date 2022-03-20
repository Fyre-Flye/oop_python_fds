# Em POO temos o conceito de métodos abstrados, onde são previamente planejados, mas ainda não implementados
# para "planejarmos" esses métodos podemos utilizar o conceito de interfaces que fazem uma ponte entre esses métodos obrigatórios
# mas não implementados ainda

# Orientação objeto em python não "suporta" o conceito de métodos e classes abstratas então devemos usar uma biblioteca especial
# $ pip install ABCMeta

from abc import ABC, abstractmethod, abstractclassmethod

class VeiculoInterface(ABC):
    
    @abstractmethod
    def buzinar():
        pass
    
    @abstractmethod
    def darPartida():
        pass
    
    @abstractmethod
    def darSeta():
        pass

class Moto(VeiculoInterface):
    def buzinar(self):
        print("bi bii")
        
    def darPartida(self):
        print("vreeuu")
        
    def darSeta(self):
        print("click click")
        
class Carro(VeiculoInterface):
    def buzinar(self):
        print("fon fon")
    
    def darPartida(self):
        print("vrumm")
        
    def darSeta(self):
        print("click click")

m1 = Moto()
c1 = Carro()

m1.buzinar()
c1.buzinar()