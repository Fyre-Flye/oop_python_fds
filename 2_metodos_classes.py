
# Métodos são tipos de funções associadas à uma classe, também podem ser chamadas de "comportamentos" de uma classe

class Carro():
    def buzinar(self): 
        print("Bii Bii!")

# O argumento especial self indica "ele mesmo (objeto)", o que garante que as intâncias serão associadas exclusivamente ao objeto que foi chamado
# self também equivalente ao método ".this" "esse" em java por exemplo

c1 = Carro()
c1.buzinar()
