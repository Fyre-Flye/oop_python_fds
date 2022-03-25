# Dentro do conceito de polimorfismo para uma mesma característica de um objeto
# Podemos assumi-las de várias formas conforme a necessidade, tanto métodos (comportamento) quanto atributos (características)

class Carro():
    def fases_ignicao(self):
        print("1 - Liberar pistão")
        print("2 - Injetar combustível")
        print("3 - Descarga elétrica\n")

class Carro_Eletrico(Carro):
    def fases_ignicao(self): # Sobrescrevemos a mesma função de ignição do carro para um tipo de carro diferente
        print("1 - Partida eletrônica ")
        print("2 - Energizar rotores ")
        print("3 - Acelerar rotores\n")

c1 = Carro()
c1.fases_ignicao()

ce1 = Carro_Eletrico()
ce1.fases_ignicao()
