alunos = {"allan": 5, "Ana": 5}
    
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
                continue
            else:
                if nome in alunos:
                    print(f"Foi alterado a nota do aluno {nome} pela nota {nota}")
                else:
                    print(f"Foi adicionado o aluno {nome} com a nota {nota}")
                alunos[nome] = nota
                break
        resposta = input("Digite 1 para voltar ao menu inicial ou qualquer tecla para continuar  ")
        if resposta == "1":
            break
        
def alterarAluno():
    while True:
        separador()
        nome = input("Insira o nome do aluno: ")
        if nome in alunos:
            while True:
                try:
                    nota = int(input("Insira a nota do aluno: "))
                except:
                    print("digite apenas numeros")
                    continue
                else:
                    print(f"Foi alterado a nota do aluno {nome} pela nota {nota}")
                    alunos[nome] = nota
                    break
        else:
            print(f"Não encontrado o aluno solicitado")
        resposta = input("Digite 1 para voltar ao menu inicial ou qualquer tecla para continuar  ")
        if resposta == "1":
            break

def excluirAluno():
    while True:
        separador()
        nome = input("Insira o nome do aluno: ")
        if nome in alunos:
            alunos.pop(nome)
            print(f"Apagado o aluno {nome}")
        else:
            print("Aluno não encontrado")
        resposta = input("Digite 1 para voltar ao menu inicial ou qualquer tecla para continuar  ")
        if resposta == "1":
            break

def consultarAlunos():
    separador()
    print("NOME      NOTA")
    for aluno, nota in alunos.items():
        print(f"{aluno}      {nota}")
    input("\nDigite qualquer tecla para retornar ao menu principal  ")

def mediaNotas():
    separador()
    media = sum(alunos.values()) / len(alunos)
    print(media)  
    input("\nDigite qualquer tecla para retornar ao menu principal  ")      

while True:
    separador()
    opcao = int(input("selecione a opção desejada: \n\n  1 - Adicionar aluno\n  2- Remover aluno\n  3 - Alterar nota\n  4 - Consultar Aluno\n  5 - Consultar Media\n  6 - Encerrar\n\n"))
    match opcao:  
        case 1:
            inserirAluno()
        case 2:
            excluirAluno()
        case 3:
            alterarAluno()
        case 4:
            consultarAlunos()
        case 5:
            mediaNotas()
        case 6:
            break
        case _:
            print("\nDigite uma opção valida")