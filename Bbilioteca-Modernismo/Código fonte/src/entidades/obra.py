
obras = {}
def get_obras(): return obras
def inserir_obra(obra):
    titulo_obra = obra.titulo
    if titulo_obra not in obras.keys():
        obras[titulo_obra] = obra
        return True
    else:
        print('Obra ' + titulo_obra + ' já tem cadastro na Biblioteca')
        return False

class Obra:

    def __init__(self, titulo, páginas, publicação):
        self.titulo = titulo
        self.páginas = páginas
        self.publicação = publicação


    def __str__(self):
        formato = '{:<28} {:<10} {:<8}'
        obra_formatada = formato.format(self.titulo, str(self.páginas), str(self.publicação))
        return obra_formatada

def ordenar_objeto(obra1, obra2):
    return obra1.páginas > obra2.páginas
