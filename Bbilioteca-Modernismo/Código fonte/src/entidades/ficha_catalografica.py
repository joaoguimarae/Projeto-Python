
fichas = []


def get_fichas_catalograficas(id_estante_biblioteca):
    get_fichas_catalograficas = []
    for ficha in fichas:
        if ficha.estante_biblioteca.id == id_estante_biblioteca:
            get_fichas_catalograficas.append(ficha)
    return get_fichas_catalograficas
def inserir_ficha_catalografica(ficha):
    if ficha not in fichas:
        fichas.append(ficha)
    else:
        print('Ficha já cadastrada para a obra: ' + str(ficha))




class FichaCatalografica:
    def __init__(self, estante_biblioteca, obra, conteudo, tematica,):
        self.estante_biblioteca = estante_biblioteca
        self.obra = obra
        self.conteudo = conteudo
        self.tematica = tematica


    def __str__(self):
        formato = '{:<4} {:<28} {:<48} {:<55}'
        ficha_formatado = formato.format(
            self.estante_biblioteca.id,
            self.obra.titulo,
            'Conteudo:' + str(self.conteudo),
            'Temática:' + str(self.tematica))
        return ficha_formatado

