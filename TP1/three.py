def Primeiro():
    primeiro_nome = input('Digite o primeiro nome: ')
    tamanho = len(primeiro_nome)
    metade = int(tamanho/2)
    primeira_metade = primeiro_nome[0:metade]
    segunda_metade = primeiro_nome[metade:]
    
    return primeira_metade, segunda_metade

def Segundo():
    segundo_nome = input('Digite o segundo nome: ')
    tamanho = len(segundo_nome)
    metade = int(tamanho/2)
    primeira_metade_two = segundo_nome[0:metade]
    segunda_metade_two = segundo_nome[metade:]
    
    return primeira_metade_two, segunda_metade_two

# Chamando as funções
primeira_metade, segunda_metade = Primeiro()
primeira_metade_two, segunda_metade_two = Segundo()

# Concatenando as variáveis
opcao_um = primeira_metade + segunda_metade_two
opcao_dois = primeira_metade_two + segunda_metade
print('Primeira opção:', opcao_um)
print('Segunda opção: ', opcao_dois)
