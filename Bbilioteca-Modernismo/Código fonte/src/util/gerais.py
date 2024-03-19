
def compacta_nome(nome):
    partes_nome = nome.split(' ')
    nome_compactado = ''
    for parte_nome in partes_nome:
        nome_compactado += parte_nome + '' if parte_nome not in ('de', 'da', 'das', 'do', 'dos') else ' '
    return nome_compactado.strip()


def imprimir_objetos(cabeçalho, objetos, arquivo=None):
    print('\n' + cabeçalho)
    for indice, objeto in enumerate(objetos):
        formato = '{:<5} {}'
        string = formato.format(str(indice + 1) + ' - ', str(objeto))
        print(string)
        string += '\n'
        if arquivo is not None: arquivo.write(string)
def ordenar_objetos_por_um_atributo(objetos, comparador):
    objetos_ordenados = []
    for objeto_desordenado in objetos:
        ordenou_objeto = False
        for índice, objeto_ordenado in enumerate(objetos_ordenados):
            if comparador(objeto_desordenado, objeto_ordenado):
                objetos_ordenados.insert(índice, objeto_desordenado)
                ordenou_objeto = True
                break
        if not ordenou_objeto: objetos_ordenados.append(objeto_desordenado)
    return objetos_ordenados

def ordenar_objetos_por_dois_atributos(objetos, atributo1, atributo2, ordenacao_decrescente):
    objetos_ordenados_atributo1 = list(objetos)
    objetos_ordenados_atributo1.sort(key=atributo1, reverse=ordenacao_decrescente)
    objetos_ordenados_atributo1_atributo2 = []
    ultimo_atributo1 = None
    objetos_mesmo_atributo1 = []

    for objeto in objetos_ordenados_atributo1:
        if atributo1(objeto) == ultimo_atributo1:
            objetos_mesmo_atributo1.append(objeto)
        else:
            objetos_mesmo_atributo1.sort(key=atributo2, reverse=ordenacao_decrescente)
            objetos_ordenados_atributo1_atributo2.extend(objetos_mesmo_atributo1)
            objetos_mesmo_atributo1 = [objeto]
            ultimo_atributo1 = atributo1(objeto)

    objetos_mesmo_atributo1.sort(key=atributo2, reverse=ordenacao_decrescente)
    objetos_ordenados_atributo1_atributo2.extend(objetos_mesmo_atributo1)
    return objetos_ordenados_atributo1_atributo2