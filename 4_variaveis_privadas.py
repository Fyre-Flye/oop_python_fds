# Do conceito de encapsulamento dentro da Teoria de POO podemos definir a
# visibilidade de certos atributos, o que garante a segurança da aplicação
# e poderá apenas ser acessada por métodos acessores ou modificadores
# Temos 3 tipos de encapsulamento para um atributo, público, protegido e privado onde...

# Público - Qualquer código fora do escopo da classe pode ter acesso
# Protegido - Apenas a classe atual e suas sub-classes (ou classe filhas)
# Privado - Apenas e classe atual

#Exemplo:

class Carro():
    def __init__(self, porta, chave, bateria): 
        
        # Método especial __init__ é um método permite a classe inicializar os atributos do objeto na sua inicialização!
        # também é equivalente a um método construtor! 
        
        self.porta = porta # Publico
        self._chave = chave # Protegido
        self.__bateria = bateria # Privado
        print(self.__bateria)
    
c1 = Carro("Abrindo porta...", "Ligando...", "Levou um choque...")

print(c1.porta)
print(c1._chave)

try:
    print(c1.__bateria)
except AttributeError:
    print("Não toque na bateria sem um mecânico! ")
