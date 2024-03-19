autores = {}

def get_autores():
    return autores

def inserir_autor(autor):
    nome_autor = autor.nome
    if nome_autor not in autores.keys():
        autores[nome_autor] = autor
        return True
    else:
        print('Autor ' + nome_autor + ' já tem cadastro na Biblioteca')
        return False


class Autor:

    def __init__(self, nome, geração, cidade, UF, sexo):
        self.nome = nome
        self.geração = geração if geração in ['Primeira','Segunda'] else 'Terceira'
        self.cidade = cidade if cidade in ['São Paulo', 'Itabira', 'Cordisburgo', 'Pilar', 'Fortaleza', ' Santa Maria', 'Itabuna', 'Quebrangulo','Patos de Minas', 'Tchetchelnik'] else 'Recife'
        self.UF = UF if UF in ['SP','MG','PB','CE','RS','BA','HR','PE'] else 'AL'
        self.sexo = sexo if sexo in ['masculino'] else 'feminino'

    def __str__(self):
        formato = '{:<25} {:<13} {:<15} {:<15} {:<4}'
        autor_formatado = formato.format(str(self.nome), self.geração, self.sexo,self.cidade,self.UF)
        return autor_formatado





