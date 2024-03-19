from entidades.obra import Obra, inserir_obra, get_obras
estantes_biblioteca = []

def get_estantes_biblioteca():
    return {f"Estante {i}": estante for i, estante in enumerate(estantes_biblioteca, start=1)}
    return estantes_biblioteca


def inserir_estante_biblioteca(estante_biblioteca):
    estantes_biblioteca.append(estante_biblioteca)

class EstanteBiblioteca:
    def __init__(self, setor, localizacao, id):
        self.setor = setor
        self.localizacao = localizacao
        self.id = id
        self.obras = {}

    def inserir_obra(self, obra):
        titulo_obra = obra.titulo
        if titulo_obra not in self.obras:
            self.obras[titulo_obra] = obra
        else:
            print('Obra ' + titulo_obra + ' já está cadastrada')

    def __str__(self):
        return self.setor + ' '  + ' ' + str(self.localizacao)

