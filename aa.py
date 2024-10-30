alunos = {}

def inserirAluno():
    nome = input("Insira o nome do aluno: ")
    nota = int(input("Insira a nota do aluno: "))
    if nome in alunos:
        print(f"Foi alterado o aluno {nome} pela nota {nota}")
    else:
        print(f"Foi adicionado o aluno {nome} com a nota {nota}")
    alunos[nome] = nota

def alterarAluno():
    nome = input("Insira o nome do aluno: ")
    if nome in alunos:
        nota = int(input("Insira a nota do aluno: "))
        print(f"Foi alterado o aluno {nome} pela nota {nota}")
        alunos[nome] = nota
    else:
        print(f"Não encontrado o aluno solicitado")
    
def excluirAluno():
    nome = input("Insira o nome do aluno: ")
    if nome in alunos:
        alunos.pop(nome)
        print(f"Apagado o aluno {nome}")
    else:
        print("Aluno não encontrado")

while True:
    opcao = int(input("selecione a opção desejada: \n 1 - Adicionar aluno\n 2- Remover aluno\n 3 - Alterar nota\n 4 - Consultar Aluno\n 5 - Consultar Media\n 6 - Encerrar\n"))
    match opcao: 
        case 1:
            inserirAluno()
        case 2:
            print("Remover aluno")
            nome = input("Digite o aluno a ser removido")
            if nome in alunos:
                alunos.pop(nome)
            else:
                print("Aluno não encontrado")
        case 3:
            alterarAluno()
        case 4:
            print(alunos)
        case 5:
            notas = alunos.values()
            print("Media de notas:")
            print(f"A media de notas ficou em {notas}")
        

