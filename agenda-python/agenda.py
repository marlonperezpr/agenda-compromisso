# AGENDA EM PYTHON
from datetime import datetime

compromissos = []

class Compromisso:
    def __init__(self, descricao, data, hora):
        self.descricao = descricao
        self.data = data
        self.hora = hora

    def __str__(self):
        return f"{self.descricao} - {self.data} {self.hora}"
    
class Agenda():
    def __init__(self):
        self.compromissos = []

    def adicionar_compromisso(self, descricao, data, hora):
        compromisso = Compromisso(descricao, data, hora)
        self.compromissos.append(compromisso)
        print(f"Compromisso adicionado com sucesso!")

    def remover_compromisso(self, indice):
        try:
            del self.compromissos[indice]
            print(f"Compromisso removido com sucesso!")
        except IndexError:
            print("Índice inválido!")
    
    def listar_compromissos(self):
        if not self.listar_compromissos:
            print("Nenhum compromisso foi encontrado")
        else:
            print("Compromissos: ")
            for i, compromisso in enumerate(self.compromissos, start=1):
                print(f"{i}. {compromisso}")

agenda = Agenda

while True:
    print("\nAgenda")
    print("1. Adicionar compromisso")
    print("2. Remover compromisso")
    print("3. Listar compromissos")
    print("4. Sair")