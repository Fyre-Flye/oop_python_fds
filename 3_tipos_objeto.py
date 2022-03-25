# Objetos podem ser de vários tipos de dados

# Podem existir vários tipos de objetos associados à uma classe

class Carro():
    pass

# Objeto do tipo string

c1 = Carro()
c1.modelo = "Kwid"

print("C1")
print(f"É uma string? {isinstance(c1.modelo, str)}")
print(f"É um int? {isinstance(c1.modelo, int)}")
print(f"É um booleano? {isinstance(c1.modelo, bool)}\n")

# Objeto do tipo int

c2 = Carro()
c2.ano = 2018

print("C2")
print(f"É uma string? {isinstance(c2.ano, str)}")
print(f"É um int? {isinstance(c2.ano, int)}")
print(f"É um booleano? {isinstance(c2.ano, bool)}\n")

# Objeto do tipo booleano

c3 = Carro()
c3.ligado = False

print("C3")
print(f"É uma string? {isinstance(c3.ligado, str)}")
print(f"É um int? {isinstance(c3.ligado, int)}") # ps: False é o mesmo que 0 inteiro (bibliotecas de C em python)
print(f"É um booleano? {isinstance(c3.ligado, bool)}\n")
