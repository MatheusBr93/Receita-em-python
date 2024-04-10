def Gravar_receita():
    nome_receita = input("Nome da Receita: ")
    ingredientes = input("Ingredientes: ")
    modo_preparo = input("Modo de Preparo da Receita: ")
    receita_txt = open('receita.txt', 'a')
    receita_txt.write(f'\nNome da Receita: {nome_receita} \nIngredientes: {ingredientes} \nModo de Preparo: {modo_preparo}\n//////////////////////////////////////') # uso do f-string para colocar uma variável dentro
    receita_txt.close()


def Consultar_receitas():
    nome_receita = input(f"Digite o nome da receita a ser consultada: ")
    receita_txt = open('receita.txt', 'r')
    tem = False
    for l in receita_txt:
        if l.strip() == f"Nome da Receita: {nome_receita}": # uso do f-string para colocar variavel dentro
            tem = True # comando True, para evitar bugs e  para fazer sentido o uso do for com o if
            print(l, end='') # comando end para finalizar o programa quando ja tiver consultado
            l = receita_txt.readline()
            while l.strip() != '///////////////////////////////////////////': # comando strip remover espaço branco
                if l.strip() != '':
                    print(l, end='')
                l = receita_txt.readline()
            break
    if not tem:
        print("Receita não encontrada")
    receita_txt.close()


def Listar_receitas():
    receita_txt = open('receita.txt', 'r')
    print(receita_txt.read())
    receita_txt.close()


def Limpar_arquivo():
    receita_txt = open('receita.txt', 'w')
    receita_txt.write("")
    receita_txt.close()



while True:
    print("1 - Criar Receita\n2 - Consultar Receita\n3 - Listar Receitas\n4 - Limpar Arquivo\n5 - Sair")
    opcao = input("Escolha uma das opções abaixo: ")
    if opcao == '1':
        Gravar_receita()
    elif opcao == '2':
        Consultar_receitas()
    elif opcao == '3':
        Listar_receitas()
    elif opcao == '4':
        Limpar_arquivo()
        print("Limpo!")
    elif opcao == '5':
        break
    else:
        print("Inválido, Tente novamente.")