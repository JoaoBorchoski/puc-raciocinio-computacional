def exibir_menu():
    print("------  [Matriculas] Menu de Operações  ------\n")
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(9) Voltar ao menu principal.\n")
     

def menuMatriculas():
    while True:
        exibir_menu()
        opcao = input("Informe a opção desejada: ")

        if opcao == '1':
            print("Opção 1 selecionada: Incluir Matriculas.")
        elif opcao == '2':
            print("Opção 2 selecionada: Listar Matriculas.")
        elif opcao == '3':
            print("Opção 3 selecionada: Atualizar Matriculas.")
        elif opcao == '4':
            print("Opção 4 selecionada: Excluir Matriculas.")
        elif opcao == '9':
            print("Voltar ao menu principal.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

