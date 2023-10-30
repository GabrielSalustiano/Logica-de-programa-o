from classes import *

def Menu():
  

    while True:
        print("\n--MENU--\n")
        print("1: Inserir e gravar dados")
        print("2: Ler dados")
        print("3: Sair")
        escolha = input("Escolha uma das opções acima: ")
        if escolha == '3':
            break
        if escolha == '1':
            nome = input("\nDigite o Nome: ")
            idade = input("\nDigite a idade: ")
            linguagem = input("\nDigite a linguagem usada pelo analista: ")
            nivel = input("\nDigite o nível do analista (junior, senior, pleno): ")
            tempo = input("\nDigite o tempo de profissão: ")

            # Clear the contents of the files before writing new data
            with open('pessoa.txt', 'w') as pessoa_file:
                pessoa_file.write('')
            with open('analistas.txt', 'w') as analista_file:
                analista_file.write('')
                
            pessoa = Pessoa(nome,idade)
            analista = AnalistaSistemas(nome,idade,linguagem,nivel,tempo)
            pessoa.gravar_pessoa()
            analista.gravar_analista()
        if escolha == '2':
           pessoa = Pessoa(nome,idade)
           analista = AnalistaSistemas(nome,idade,linguagem,nivel,tempo) 
           pessoa.ler_pessoa()
           analista.ler_analista()
        if escolha not in ['1','2','3']:
            print("\nEscolha inválida, tente novamente")
Menu()