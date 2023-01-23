# listas
itensMercearia = ['Arroz 5kg', 'Feijao 1kg', 'Cafe 500g', 'Macarrao 2kg']
precoMercearia = [20.0, 8.0, 15.0, 9.0]
itensLaticinios = ['Leite', 'Yogurte', 'Cheddar']
precoLaticinios = [4.0, 2.5, 4.0]
itensCongelados = ['Patinho', 'Coxa de Frango', 'Fraldinha']
precoCongelados = [40.0, 15.0, 13.0]
produtosCarrinho = []
valorCarrinho = []
total = 0


# menu produtos
def produtos():
    print("\n\tSelecione uma das categorias abaixo :"
          "\n\n\t================ Produtos ==============="
          "\n\t|\t1 - Mercearia \t\t\t|"
          "\n\t|\t2 - Laticinios \t\t\t|"
          "\n\t|\t3 - Congelados \t\t\t|"
          "\n\t========================================="
          )


# menu mercearia
def mercearia():
    i = 0
    tamMercearia = len(itensMercearia)
    while i < tamMercearia:
        print(f'Produto {i + 1}: {itensMercearia[i]} - Preço: R${precoMercearia[i]}')
        i += 1
    produto = int(input('\nEscolha um produto: '))
    atualizarLista(itensMercearia[produto - 1], precoMercearia[produto - 1])


# menu laticinios
def laticinios():
    i = 0
    tamLaticinios = len(itensLaticinios)
    while i < tamLaticinios:
        print(f'Produto {i + 1}: {itensLaticinios[i]} - Preço: R${precoLaticinios[i]}')
        i += 1
    produto = int(input('\nEscolha um produto: '))
    atualizarLista(itensLaticinios[produto - 1], precoLaticinios[produto - 1])



# menu congelados
def congelados():
    i = 0
    tamCongelados = len(itensCongelados)
    while i < tamCongelados:
        print(f'Produto {i + 1}: {itensCongelados[i]} - Preço: R${precoCongelados[i]}')
        i += 1
    produto = int(input('\nEscolha um produto: '))
    atualizarLista(itensCongelados[produto - 1], precoCongelados[produto - 1])


# adicionar produto ao carrinho
def atualizarLista(nome, preco):
    global total
    produtosCarrinho.append(nome)
    valorCarrinho.append(preco)
    total += preco
    print('\nProduto adicionado ao carrinho com sucesso!')
    print(f'\nProduto: {nome} - Preço: {preco}')

    
# checar carrinho
def verCarrinho():
    i = 0
    while i < len(produtosCarrinho):
        print(f'Produto {i + 1}: {produtosCarrinho[i]} - Preço: R${valorCarrinho[i]}')
        i += 1
    print(f'\nValor total: R${total}')


while True:
    opcao = int(input(
        "\n\n\t========= Bem-vindo ao SuperMarket ======"
        "\n\t\t1 - Produtos \t\t\t"
        "\n\t\t2 - Ver carrinho \t\t"
        "\n\t\t0 - Sair\t\t\t"
        "\n\t========================================="
        "\n\nEscolha uma opcao: "
    ))

    if opcao == 0:
        print('Obrigado por nos visitar, volte sempre!')
        break
    else:
        match opcao:
            case 1:
                produtos()
                escolha = int(input('Escolha uma opção: '))
                match escolha:
                    case 1:
                        mercearia()
                    case 2:
                        laticinios()
                    case 3:
                        congelados()
                    case _:
                        print('Digite uma escolha válida')
            case 2:
                verCarrinho()
