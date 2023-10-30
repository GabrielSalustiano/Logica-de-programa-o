class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def gravar_pessoa(self):
        with open("pessoa.txt", "a") as arquivo:
            arquivo.write(f"Nome: {self.nome}\n")
            arquivo.write(f"Idade: {self.idade}\n")       
    def ler_pessoa(self):
        f = open("pessoa.txt",'r')
        print("Leitura de pessoa")
        l = f.read()
        print(f"\n", l)

class AnalistaSistemas(Pessoa):
    def __init__(self, nome, idade, linguagem, nivel,tempo):
        super().__init__(nome, idade)
        self.linguagem = linguagem
        self.nivel = nivel
        self.tempo = tempo
    
    def gravar_analista(self):
        with open("analistas.txt", "a") as arquivo:
            arquivo.write(f"Nome: {self.nome}\n")
            arquivo.write(f"Idade: {self.idade}\n")        
            arquivo.write(f"Linguagem: {self.linguagem}\n")
            arquivo.write(f"Nível: {self.nivel}\n")
    def ler_analista(self):
        f = open("analistas.txt",'r')
        print("Leitura de analista")
        l = f.read()
        print(f"\n", l)

