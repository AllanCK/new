alunos = {}
    
def separador():
    print("\n ------------------------------- \n")

def inserirAluno():
    while True:
        separador()
        nome = input("Insira o nome do aluno: ").capitalize()
        while True:
            try:
                nota = int(input("Insira a nota do aluno: "))
            except:
                print("Insira um numero para a nota")
            else:
                if nome in alunos:
                    print(f"Foi alterado a nota do aluno {nome} pela nota {nota}")
                else:
                    print(f"Foi adicionado o aluno {nome} com a nota {nota}")
                alunos[nome] = nota
                break
        resposta = input("Digite 1 para voltar ao menu inicial ou Pressione Enter para continuar  ")
        if resposta == "1":
            break
        
def alterarAluno():
    while True:
        separador()
        nome = input("Insira o nome do aluno: ").capitalize()
        if nome in alunos:
            while True:
                try:
                    nota = int(input("Insira a nota do aluno: "))
                except:
                    print("digite apenas numeros")
                else:
                    print(f"Foi alterado a nota do aluno {nome} pela nota {nota}")
                    alunos[nome] = nota
                    break
        else:
            print(f"Não encontrado o aluno solicitado")
        resposta = input("Digite 1 para voltar ao menu inicial ou Pressione Enter para continuar  ")
        if resposta == "1":
            break

def excluirAluno():
    while True:
        separador()
        nome = input("Insira o nome do aluno: ").capitalize()
        if nome in alunos:
            alunos.pop(nome)
            print(f"Apagado o aluno {nome}")
        else:
            print("Aluno não encontrado")
        resposta = input("Digite 1 para voltar ao menu inicial ou Pressione Enter para continuar  ")
        if resposta == "1":
            break

def consultarAlunos():
    separador()
    if len(alunos) == 0:
        print("Sem registros de alunos")
    else:
        dicOrganizado = sorted(alunos.items())
        print('{:<20}      {:>4}'.format("ALUNO", "NOTA"))
        for aluno, nota in dicOrganizado:
            print('{:<20}      {:>4}'. format(aluno, nota))
    input("\nPressione Enter para retornar ao menu principal  ")

def mediaNotas():
    separador()
    if len(alunos) == 0:
        print("Sem registros de alunos")
    else:
        media = round(sum(alunos.values()) / len(alunos), 1)
        print(f"A media de nota dos alunos é: {media}")  
    input("\nPressione Enter para retornar ao menu principal  ")      

while True:
    separador()
    opcao = int(input("selecione a opção desejada: \n\n  1 - Adicionar aluno\n  2 - Alterar nota\n  3 - Remover aluno\n  4 - Consultar Alunos\n  5 - Consultar Media\n  6 - Encerrar\n\n"))
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
            break
        case _:
            print("\nDigite uma opção valida")