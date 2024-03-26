def exibir_menu():
    print("------  [Professores] Menu de Operações  ------\n")
    print("(1) Incluir.")
    print("(2) Listar.")
    print("(3) Atualizar.")
    print("(4) Excluir.")
    print("(9) Voltar ao menu principal.\n")
     

def menuProfessores():
    while True:
        exibir_menu()
        opcao = input("Informe a opção desejada: ")

        if opcao == '1':
            print("Opção 1 selecionada: Incluir Professores.")
        elif opcao == '2':
            print("Opção 2 selecionada: Listar Professores.")
        elif opcao == '3':
            print("Opção 3 selecionada: Atualizar Professores.")
        elif opcao == '4':
            print("Opção 4 selecionada: Excluir Professores.")
        elif opcao == '9':
            print("Voltar ao menu principal.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

