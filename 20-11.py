class Animal:
    def __init__ (self,nome,idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"O {self.nome} está falando.")
        print(f"tem {self.idade} de idade")

class Cachorro(Animal):
    def __init__ (self,nome,idade,raca):
        super().__init__(nome,idade)
        self.raca = raca
    
    def latir(self):
        print(f"o {self.nome} esta latindo")
        print(f"a raça do {self.nome} é {self.raca}")

class Gato(Animal):
    def __init__ (self,nome,idade,raca,peso):
        super().__init__(nome,idade)
        self.raca = raca
        self.peso = peso
    
    def miar(self):
        print(f"o {self.nome} esta miando")
        print(f"a raça do {self.nome} é {self.raca}")
        print(f"o peso do {self.nome} é {self.peso}")

a = Animal('Pedro',3)
c = Cachorro("Marley",4,"Yorkshire")
g = Gato("Bichano",2,"siamês","3 kg")
print(a.falar())
print(c.latir())
print(c.falar())
print(g.miar())
'''
Exercicios:
1 imprimir a raça do cachorro
2 criar duas novas classe a saber:
a) gato e leao
b) praticar o polimorfismo de método(comportamento) do objeto
c) fazer com que o caão ao invéz de latir, faça falar
d) fazer a mesma prática de c para leão e gato
3. fazer o meno e capturar os dados or meio do teclado
'''