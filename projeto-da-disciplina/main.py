from disciplinas.main import menuDisciplinas
from estudantes.main import menuEstudantes
from matriculas.main import menuMatriculas
from professores.main import menuProfessores
from turmas.main import menuTurmas


def exibir_menu():
    print("------  MENU PRINCIPAL  ------\n")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar turmas.")
    print("(4) Gerenciar matrículas.")
    print("(9) Sair.\n")



def main():
    while True:
        exibir_menu()
        opcao = input("Informe a opção desejada: ")

        if opcao == '1':
            print("\n Opção 1 selecionada: Gerenciar estudantes.\n")
            menuEstudantes()
        elif opcao == '2':
            print("\n Opção 2 selecionada: Gerenciar professores.\n")
            menuProfessores()
        elif opcao == '3':
            print("\n Opção 3 selecionada: Gerenciar disciplinas.\n")
            menuDisciplinas()
        elif opcao == '4':
            print("\n Opção 3 selecionada: Gerenciar turmas.\n")
            menuTurmas()
        elif opcao == '5':
            print("\n Opção 4 selecionada: Gerenciar matrículas.\n")
            menuMatriculas()
        elif opcao == '9':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
