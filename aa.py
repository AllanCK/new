#definindo o inicio do dicionario
alunos = {}
#definindo uma função para imprimir uma linha separando
def separador():
    #imprime a linha
    print("\n ------------------------------- \n")
#definindo a função para a inserção de alunos
def inserirAluno():
    #iniciando o loop
    while True:
        #função separadora
        separador()
        #criando a variavel nome que ira solicitar um input do nome do aluno, o captalize faz a primeira letra virar maiscula
        nome = input("Insira o nome do aluno: ").capitalize()
        #iniciando outro loop 
        while True:
            #coloca pra tentar esse codigo para pegar erros
            try:
                #Cria a variavel e solicita um input da nota do aluno e transforma em inteiro
                nota = round(float(input("Insira a nota do aluno(1 até 10): ")),1)
            #roda isso caso ocorra um erro no try
            except:
                #imprime solicitando apenas um numero
                print("Insira um numero para a nota")
            #roda isso caso não de erro no try    
            else:
                #valida se o nome ja tem no dicionario de alunos
                if nome in alunos:
                    #imprime que foi alterado a noma pois ja possui no dicionario
                    print(f"Foi alterado a nota do aluno {nome} pela nota {nota}")
                #roda se não existe o nome nos alunos
                else:
                    #imprime que foi adicionado o aluno com a nota
                    print(f"Foi adicionado o aluno {nome} com a nota {nota}")
                #insere ou altera o nome com a nota
                alunos[nome] = nota
                #quebra o 2º loop do while
                break
        #solicita uma variavel resposta
        resposta = input("Digite 1 para voltar ao menu inicial ou Pressione Enter para continuar  ")
        #se a resposta foi 1 vai quebrar o loop
        if resposta == "1":
            #quebra o 1ºloop do while
            break
#definindo a função de alterar o aluno        
def alterarAluno():
    #cria um loop de while
    while True:
        #função de imprimir linha pra separar
        separador()
        #solicita o nome ao usuario
        nome = input("Insira o nome do aluno: ").capitalize()
        #verifica se o nome esta no dicionario alunos
        if nome in alunos:
            #cria outro loop
            while True:
                #tenta fazer esse codigo e verificar um erro
                try:
                    #solicita a nota do aluno
                    while True:
                        nota = round(float(input("Insira a nota do aluno(1 até 10): ")),1)
                        
                #se ocorrer um erro roda essa parte do codigo
                except:
                    #solicita ao usuario que coloque apenas numeros
                    print("digite apenas numeros")
                #se não ocorrer erro no try roda esse
                else:
                    #imprime que foi alterado a nota
                    print(f"Foi alterado a nota do aluno {nome} pela nota {nota}")
                    #altera a nota do nome em alunos
                    alunos[nome] = nota
                    #quebra o loop
                    break
        #Roda se não for encontrado aluno com o nome no dicionario
        else:
            #imprime que não achou o nome do aluno
            print(f"Não encontrado o aluno solicitado")
        #Solicita a resposta para quebrar o codigo ou continuar
        resposta = input("Digite 1 para voltar ao menu inicial ou Pressione Enter para continuar  ")
        #verifica se resposta é igual a 1 para quebrar
        if resposta == "1":
            #quebra o loop
            break
#Define uma função para excluir um aluno
def excluirAluno():
    #Loop
    while True:
        #Separador
        separador()
        #Solicita o nome do aluno a ser excluido
        nome = input("Insira o nome do aluno: ").capitalize()
        #Se nome estiver em alunos vai rodar essa parte
        if nome in alunos:
            #exclui o nome do dicionario alunos
            alunos.pop(nome)
            #imprime que foi apagado o nome
            print(f"Apagado o aluno {nome}")
        #se não for encontrado o nome em alunos
        else:
            #imprime que o aluno não foi encontrado
            print("Aluno não encontrado")
        #solicita o numero para quebrar o loop ou continuar apagando
        resposta = input("Digite 1 para voltar ao menu inicial ou Pressione Enter para continuar  ")
        if resposta == "1":
            break
#define uma função para consultar os alunos
def consultarAlunos():
    separador()
    #verifica se o dicionario esta vazio
    if len(alunos) == 0:
        #imprime que esta vazio
        print("Sem registros de alunos")
    #Roda se possuir alunos no dicionario
    else:
        #imprime uma linha, {:<20} fala que vai ocupar 20 espaços pela esquerda e {:>4} 4 espaços começando pela direita
        print('{:<20}      {:>4}'.format("ALUNO", "NOTA"))
        #cria uma copia do alunos mas organizados alfabeticamente
        dicOrganizado = sorted(alunos.items())
        #cria um loop para passar por todos os itens do dicionario organizado
        for aluno, nota in dicOrganizado:
            #imprime usando o .format, usando as mesmas regras do outro
            print('{:<20}      {:>4}'. format(aluno, nota))
    #trava a tela e solicita um input para continuar, pois esta fora de um loop
    input("\nPressione Enter para retornar ao menu principal  ")
#define função para a media dos alunos
def mediaNotas():
    separador()
    #verifica se alunos possuem algum registro
    if len(alunos) == 0:
        print("Sem registros de alunos")
    else:
        #cria variavel media, que é a soma(SUM soma todos os valores de numeros dentro do dicionario) e divide pela quantidade(LEN ve quantos registros possuem o dicionario)
        media = round(sum(alunos.values()) / len(alunos), 1)
        #imprime que a media foi
        print(f"A media de nota dos alunos é: {media}")  
    #trava a tela e solicita um input para continuar, pois esta fora de um loop
    input("\nPressione Enter para retornar ao menu principal  ")      

#Loop do codigo principal
while True:
    separador()
    try:
        #imprime para o usuario e solicita que escreva uma opção para ser salva na variavel opcao
        opcao = int(input("selecione a opção desejada: \n\n  1 - Adicionar aluno\n  2 - Alterar nota\n  3 - Remover aluno\n  4 - Consultar Alunos\n  5 - Consultar Media\n  6 - Encerrar\n\n"))
         #Verifica a variavel opcao e vai rodar a funcao determinada
    except:
        print("\nDigite uma opção valida")
    else:
        match opcao:  
            case 1:
                inserirAluno()
            case 2:
                alterarAluno()
            case 3:
                excluirAluno()
            case 4:
                consultarAlunos()
            case 5:
                mediaNotas()
            case 6:
                #quebra o loop principal.encerrando o programa
                break
            #se não for nenhuma das opções definidas
            case _:
                print("\nDigite uma opção valida")