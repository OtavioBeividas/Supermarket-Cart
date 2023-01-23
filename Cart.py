# lists
groceryItems = ['Arroz 5kg', 'Feijao 1kg', 'Cafe 500g', 'Macarrao 2kg']
groceryPrice = [20.0, 8.0, 15.0, 9.0]
dairyItems = ['Leite', 'Yogurte', 'Cheddar']
dairyPrice = [4.0, 2.5, 4.0]
frozenFoods = ['Patinho', 'Coxa de Frango', 'Fraldinha']
frozenFoodPrice = [40.0, 15.0, 13.0]
cartProducts = []
cartValue = []
total = 0


# menu produtos // products menu
def products():
    print("\n\tSelect one of the categories below:"
          "\n\n\t================ Products ==============="
          "\n\t|\t1 - Grocery Store \t\t\t|"
          "\n\t|\t2 - Dairy Products \t\t\t|"
          "\n\t|\t3 - Frozen Foods \t\t\t|"
          "\n\t========================================="
          )


# menu mercearia // grocery menu
def groceryStore():
    i = 0
    sizeGrocery = len(groceryItems)
    while i < sizeGrocery:
        print(f'Product {i + 1}: {groceryItems[i]} - Price: R${groceryPrice[i]}')
        i += 1
    product = int(input('\nChoose a product: '))
    updateList(groceryItems[product - 1], groceryPrice[product - 1])


# menu laticinios // dairy menu
def dairyProducts():
    i = 0
    dairySize = len(dairyItems)
    while i < dairySize:
        print(f'Product {i + 1}: {dairyItems[i]} - Price: R${dairyPrice[i]}')
        i += 1
    product = int(input('\nChoose a product: '))
    updateList(dairyItems[product - 1], dairyPrice[product - 1])


# menu congelados // frozen menu
def frozenFood():
    i = 0
    frozenSize = len(frozenFoods)
    while i < frozenSize:
        print(f'Produto {i + 1}: {frozenFoods[i]} - Preço: R${frozenFoodPrice[i]}')
        i += 1
    product = int(input('\nChoose a product: '))
    updateList(frozenFoods[product - 1], frozenFoodPrice[product - 1])


# adicionar produto ao carrinho // add product to cart
def updateList(name, price):
    global total
    cartProducts.append(name)
    cartValue.append(price)
    total += price
    print('\nProduct added to cart successfully!')
    print(f'\nProduct: {name} - Price: {price}')


# checar carrinho // check cart
def viewCart():
    i = 0
    while i < len(cartProducts):
        print(f'Product {i + 1}: {cartProducts[i]} - Price: R${cartValue[i]}')
        i += 1
    print(f'\nValor total: R${total}')


while True:
    option = int(input(
        "\n\n\t========= Welcome to the SuperMarket ======"
        "\n\t\t1 - Products \t\t\t"
        "\n\t\t2 - View Cart \t\t"
        "\n\t\t0 - Exit\t\t\t"
        "\n\t========================================="
        "\n\nChoose an option: "
    ))

    if option == 0:
        print('Thanks for visiting us, come back often!')
        break
    else:
        match option:
            case 1:
                products()
                choice = int(input('Choose an option: '))
                match choice:
                    case 1:
                        groceryStore()
                    case 2:
                        dairyProducts()
                    case 3:
                        frozenFood()
                    case _:
                        print('Enter a valid choice')
            case 2:
                viewCart()
