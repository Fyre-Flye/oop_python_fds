# A herança multipla é o conceito de que uma única classe pode herdar características de mais de uma só classe

class carro():
    rodas = 4

class barco():
    def navegar(self):
        print("Navegando...")

class veiculo_anfibio(carro, barco):
    pass

# Uma herança múltipla pode reunir características de diferentes classes

anfibio1 = veiculo_anfibio()
print(f"Eu tenho {veiculo_anfibio.rodas} rodas! ")
anfibio1.navegar()