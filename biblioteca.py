# biblioteca.py
from livro import Livro

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def adicionar_livro(self, titulo, autor, isbn):
        livro = Livro(titulo, autor, isbn)
        self.catalogo.append(livro)

    def listar_livros(self):
        for livro in self.catalogo:
            print(livro)

    def buscar_livro(self, isbn):
        for livro in self.catalogo:
            if livro.isbn == isbn:
                return livro
        return None

    def emprestar_livro(self, isbn):
        livro = self.buscar_livro(isbn)
        if livro and livro.emprestar():
            print(f"Livro '{livro.titulo}' emprestado com sucesso!")
        else:
            print("Livro não disponível ou não encontrado.")

    def devolver_livro(self, isbn):
        livro = self.buscar_livro(isbn)
        if livro:
            livro.devolver()
            print(f"Livro '{livro.titulo}' devolvido com sucesso!")
        else:
            print("Livro não encontrado.")
