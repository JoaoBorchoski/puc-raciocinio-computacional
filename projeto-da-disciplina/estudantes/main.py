import json

CAMINHO_ARQUIVO = 'estudantes.json'

def carregar_dados():
    try:
        with open(CAMINHO_ARQUIVO, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
        

def salvar_dados(estudantes):
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(estudantes, arquivo, indent=4)


def adicionar_estudante():
    nome = input("Nome do estudante: ")
    idade = input("Idade do estudante: ")
    estudantes = carregar_dados()
    novo_id = 1 if not estudantes else estudantes[-1]['id'] + 1
    novo_estudante = {'id': novo_id, 'nome': nome, 'idade': idade}
    estudantes.append(novo_estudante)
    salvar_dados(estudantes)
    print("\n Estudante adicionado com sucesso. \n")


def listar_estudantes():
    estudantes = carregar_dados()
    if estudantes:
        print("\n Lista de estudantes: \n")
        for estudante in estudantes:
            print(f"ID: {estudante['id']}, Nome: {estudante['nome']}, Idade: {estudante['idade']}")
        print("\n")
    else:
        print("\n Não há estudantes cadastrados. \n")


def encontrar_estudante_por_id(estudantes, id):
    for estudante in estudantes:
        if estudante['id'] == id:
            return estudante
    return None


def atualizar_estudante():
    estudantes = carregar_dados()
    listar_estudantes()
    if estudantes:
        id = int(input("Digite o ID do estudante que deseja atualizar: "))
        estudante = encontrar_estudante_por_id(estudantes, id)
        if estudante:
            nome = input("Novo nome do estudante: ")
            idade = input("Nova idade do estudante: ")
            estudante['nome'] = nome
            estudante['idade'] = idade
            salvar_dados(estudantes)
            print("\n Estudante atualizado com sucesso. \n")
        else:
            print("ID inválido.")
    else:
        print("\n Não há estudantes cadastrados. \n")


def excluir_estudante():
    estudantes = carregar_dados()
    listar_estudantes()
    if estudantes:
        id = int(input("Digite o ID do estudante que deseja excluir: "))
        estudante = encontrar_estudante_por_id(estudantes, id)
        if estudante:
            estudantes.remove(estudante)
            salvar_dados(estudantes)
            print("\n Estudante excluído com sucesso. \n")
        else:
            print("ID inválido.")
    else:
        print("\n Não há estudantes cadastrados. \n")


def exibir_menu():
    print("------  [Estudantes] Menu de Operações  ------\n")
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(9) Voltar ao menu principal.\n")
     

def menuEstudantes():
    while True:
        exibir_menu()
        opcao = input("Informe a opção desejada: ")

        if opcao == '1':
            print("Opção 1 selecionada: Incluir estudantes.")
            adicionar_estudante()
        elif opcao == '2':
            print("Opção 2 selecionada: Listar estudantes.")
            listar_estudantes()
        elif opcao == '3':
            print("Opção 3 selecionada: Atualizar estudantes.")
            atualizar_estudante()
        elif opcao == '4':
            print("Opção 4 selecionada: Excluir estudantes.")
            excluir_estudante()
        elif opcao == '9':
            print("Voltar ao menu principal.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

