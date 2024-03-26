def exibir_menu():
    print("------  [Turmas] Menu de Operações  ------\n")
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(9) Voltar ao menu principal.\n")
     

def menuTurmas():
    while True:
        exibir_menu()
        opcao = input("Informe a opção desejada: ")

        if opcao == '1':
            print("Opção 1 selecionada: Incluir Turmas.")
        elif opcao == '2':
            print("Opção 2 selecionada: Listar Turmas.")
        elif opcao == '3':
            print("Opção 3 selecionada: Atualizar Turmas.")
        elif opcao == '4':
            print("Opção 4 selecionada: Excluir Turmas.")
        elif opcao == '9':
            print("Voltar ao menu principal.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

