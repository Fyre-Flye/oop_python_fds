# No conceito de programação em geral existe um conceito para assinatura de métodos
# O que permite que um método de mesmo nome consiga ter comportamentos diferentes
# As assinaturas de um método são em resumo, sua quantidade de argumentos 

from multipledispatch import dispatch # O python não suporta assinatura de métodos, então para melhor exemplicar a assinatura de métodos usaremos essa biblioteca

# $ pip install multipledispatch

class Carro():

    @dispatch(int, int, int)
    def velocidade_media(self, d_km , t_h, nitro_injetado):
        vm = (d_km/t_h)*nitro_injetado
        print(f"A velocidade média é: {vm} KM/H ")
        
    @dispatch(int, int)
    def velocidade_media(self, d_km, t_h):
        vm = d_km/t_h
        print(f"A velocidade média é: {vm} KM/H ")
        

c1 = Carro()
c1.velocidade_media(100, 10, 10)
c1.velocidade_media(100, 10)