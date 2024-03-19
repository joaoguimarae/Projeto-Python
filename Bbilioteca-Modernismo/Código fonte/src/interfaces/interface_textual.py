from entidades.obra import Obra, inserir_obra, get_obras
from entidades.estante_biblioteca import get_estantes_biblioteca
from util.gerais import imprimir_objetos, ordenar_objetos_por_um_atributo, ordenar_objetos_por_dois_atributos
from entidades.ficha_catalografica import get_fichas_catalograficas
from entidades.autor import get_autores


def loop_opções(estante_biblioteca, arquivo_saida, fichas_catalográficas):
    print('\n' + str(estante_biblioteca))
    sair_loop = False
    obras_estante_biblioteca = list(estante_biblioteca.obras.values())

    while not sair_loop:
        opções_operações = (
            '\nOpções para Estante da Biblioteca\n'
            '1 - Obras\n'
            '2 - Fichas Catalográficas\n'
            '3 - Obras: ordenação decrescente por páginas\n'
            '4 - Autores das obras\n'
            '5 - Obras: ordenação por dois atributos\n'
            '6 - Obras: ordenação crecente por páginas\n'
            '7- Sair'
        )
        print(opções_operações)
        arquivo_saida.write(opções_operações + '\n')
        questão = 'Número da opção a ser executada'
        opção = ler_int_positivo(questão)
        questão_resposta = questão + ' : ' + str(opção) + '\n'
        arquivo_saida.write(questão_resposta)

        if opção is None:
            break
        elif opção == 1:
            imprimir_objetos('Obras na Biblioteca', objetos=obras_estante_biblioteca, arquivo=arquivo_saida)
        elif opção == 2:
            imprimir_objetos(cabeçalho='Fichas Catalográficas',
                             objetos=fichas_catalográficas, arquivo=arquivo_saida)

        elif opção == 3:
            imprimir_objetos('Obras: ordenação decrescente por páginas',
                             ordenar_objetos_por_um_atributo(objetos=obras_estante_biblioteca,
                                                        comparador=lambda obra1, obra2: obra1.páginas > obra2.páginas))

        elif opção == 4:
            imprimir_objetos('Autores das obras', objetos=get_autores(), arquivo=arquivo_saida)
        elif opção == 5:
            imprimir_objetos('Obras: ordenação por dois atributos',
                             ordenar_objetos_por_dois_atributos(objetos=obras_estante_biblioteca,
                                                                 atributo1=lambda obra: obra.páginas,
                                                                 atributo2=lambda obra: obra.titulo,
                                                                 ordenacao_decrescente=True),
                             arquivo=arquivo_saida)

        elif opção == 6:
            imprimir_objetos('Obras: ordenação crescente por páginas',
                         ordenar_objetos_por_um_atributo(objetos=obras_estante_biblioteca,
                                                         comparador=lambda obra1, obra2: obra1.páginas < obra2.páginas))


        elif opção == 7:
            sair_loop = True
        else:
            print('Opção inválida. Tente novamente.')


def loop_estantes_biblioteca():
    arquivo_saída = open(file='../../dados/estantes_biblioteca_saída.txt', mode='w', encoding='utf-8')
    sair_loop = False
    nomes_estantes_biblioteca = list(get_estantes_biblioteca().keys())

    while not sair_loop:
        imprimir_objetos(cabeçalho='Selecionar a estante da biblioteca', objetos=get_estantes_biblioteca(), arquivo=arquivo_saída)
        questão = 'Número da estante da biblioteca a ser executada'
        índice_estante_biblioteca = ler_int_positivo(questão)
        questão_resposta = questão + ' : ' + str(índice_estante_biblioteca) + '\n'
        arquivo_saída.write(questão_resposta)

        if índice_estante_biblioteca is None:
            break
        elif 1 <= índice_estante_biblioteca <= len(nomes_estantes_biblioteca):
            estante_biblioteca_selecionada = get_estantes_biblioteca()[
                nomes_estantes_biblioteca[índice_estante_biblioteca - 1]]
            fichas_catalográficas = get_fichas_catalograficas(estante_biblioteca_selecionada.id)
            loop_opções(estante_biblioteca_selecionada, arquivo_saída, fichas_catalográficas)

        sair_loop = ler_sair_loop('estantes_biblioteca')

    arquivo_saída.close()


def ler_int_positivo(dado):
    while True:
        try:
            string = input('- ' + dado + ' : ')
            if len(string) == 0:
                return None
            int_positivo = int(string)
            if int_positivo > 0:
                return int_positivo
            else:
                raise ValueError
        except ValueError:
            print('Erro na leitura/conversão do inteiro positivo: ' + dado)


def ler_sair_loop(loop):
    while True:
        try:
            sair = input('\n-- sair do loop de ' + loop + ' [S]: ')
            if sair.upper() == 'S':
                return True
            elif sair.upper() == 'N':
                return False
            else:
                raise ValueError
        except ValueError:
            print('Resposta inválida. Responda S ou N.')

