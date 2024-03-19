import json
from entidades.estante_biblioteca import EstanteBiblioteca, inserir_estante_biblioteca
from entidades.autor import Autor, inserir_autor
from entidades.obra import Obra
from entidades.ficha_catalografica import FichaCatalografica, inserir_ficha_catalografica
from interfaces.interface_textual import loop_estantes_biblioteca
def carregar_objetos_arquivo():
    arquivo_entrada = open(file='../../dados/arquivo_entrada.json', mode='r', encoding='utf-8')
    arquivo_dict = json.load(arquivo_entrada)

    autores_list = arquivo_dict['autores']
    for autor_dict in autores_list:
        autor = Autor(
            # (self, nome, geração, cidade, UF, sexo)
            nome = autor_dict['nome'],
            geração = autor_dict['geração'],
            cidade = autor_dict['cidade'],
            UF = autor_dict['UF'],
            sexo = autor_dict['sexo']

        )
        inserir_autor(autor)


    estantes_biblioteca_dict = arquivo_dict['estantes_biblioteca']
    for estante_dict in estantes_biblioteca_dict.values():
        estante_biblioteca = EstanteBiblioteca(
            setor=estante_dict['setor'],
            localizacao=estante_dict['localizacao'],
            id=estante_dict['id']
        )
        inserir_estante_biblioteca(estante_biblioteca)
        obras_list = estante_dict['obras']
        for obra_dict in obras_list:
            obra = Obra(
                titulo=obra_dict['titulo'],
                páginas=obra_dict['páginas'],
                publicação=obra_dict['publicação']
            )
            estante_biblioteca.inserir_obra(obra)

    fichas_catalográficas_dict = arquivo_dict['fichas_catalograficas']
    for categoria, obras_dict in fichas_catalográficas_dict.items():
        for obra, detalhes_dict in obras_dict.items():
            for estante_categoria, estante_info in arquivo_dict['estantes_biblioteca'].items():
                for obra_info in estante_info['obras']:
                    if obra_info['titulo'] == obra:
                        ficha = FichaCatalografica(
                            estante_biblioteca=EstanteBiblioteca(
                                setor=estante_info['setor'],
                                localizacao=estante_info['localizacao'],
                                id=estante_info['id']
                            ),
                            obra=Obra(
                                titulo=obra,
                                páginas=obra_info['páginas'],
                                publicação=obra_info['publicação']
                            ),
                            conteudo=detalhes_dict['conteudo'],
                            tematica=detalhes_dict['tematica']
                        )
                        inserir_ficha_catalografica(ficha)



if __name__ == '__main__':
    carregar_objetos_arquivo()
    loop_estantes_biblioteca()
