#https://meet.google.com/dnw-emhx-gfm

class Biblioteca:  
    def __init__(self):  
        self.livros = []  # Composição: lista de objetos Livro  
  
    def adicionar_livro(self, livro):  
        self.livros.append(livro)  
  
    def remover_livro(self, titulo):  
        for livro in self.livros:  
            if livro.titulo == titulo:  
                self.livros.remove(livro)  
                return  
        print("Livro não encontrado!")  
  
    def listar_livros(self):  
        for livro in self.livros:  
            print(f"{livro.titulo} - {livro.autor}")  

# Exemplo de uso:  
bib = Biblioteca()  
bib.adicionar_livro(Livro("1984", "George Orwell"))  
bib.adicionar_livro(Livro("Dom Quixote", "Cervantes"))  
bib.listar_livros()  