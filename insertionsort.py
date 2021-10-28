# Carregando os valores na lista
# Definindo a quantidade de elementos da lista
quantidade = 10
lista = []

# Rodando o loop para inserir os elementos na lista via input
for cont in range(quantidade):
    lista.append(int(input(f'Valor {cont+1}: ')))

# Exibindo os valores carregados na lista
print(f'\nValores carregados na lista.\n{lista}')

# Ordenando os elementos da lista
# Realizando as iterações a partir do segundo elemento até o tamanho da lista
for i in range(1, quantidade):
    # Elemento que será usado para comparação
    chave = lista[i] # 1ª iteração a partir do segundo elemento
    j = i - 1 # Primeiro elemento da lista
    # Ponto de parada para comparar os elementos
    while j >= 0 and lista[j] > chave:
        # Avançando o elemento até o ponto de parada
        lista[j + 1] = lista[j]
        # J precisa ser decrementado para não ficar preso no loop
        j -= 1
    # Encontrando a posição em que a chave pode ser inserida
    lista[j + 1] = chave

# Exibindo a lista ordenada
print(f'\nLista ordenada.\n{lista}')
