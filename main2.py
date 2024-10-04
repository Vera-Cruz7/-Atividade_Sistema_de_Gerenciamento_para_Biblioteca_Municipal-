# main2.py
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    while True:
        print("\nSistema de Gerenciamento de Biblioteca")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            biblioteca.adicionar_livro(titulo, autor, isbn)
            print("Livro adicionado com sucesso!")

        elif escolha == "2":
            biblioteca.listar_livros()

        elif escolha == "3":
            isbn = input("ISBN do livro para emprestar: ")
            biblioteca.emprestar_livro(isbn)

        elif escolha == "4":
            isbn = input("ISBN do livro para devolver: ")
            biblioteca.devolver_livro(isbn)

        elif escolha == "5":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
