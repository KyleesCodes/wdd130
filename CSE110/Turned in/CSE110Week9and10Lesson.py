shop_items = []
item_prices = []

print("Welcome to Kylee's shopping cart program!")
print('')
action = '0'
while action != '5':
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove item')
    print('4. Compute total')
    print('5. Quit')
    action = input('Please enter an action: ')
    if action == '1':
        shop_item = input('What item would you like to add?: ')
        item_price = float(input(f'What is the price of the item "{shop_item.capitalize()}"? '))
        print(f'"{shop_item.capitalize()}" has been added to the cart.')
        print('')
        shop_items.append(shop_item.capitalize())
        item_prices.append(item_price)
    elif action == '2':
        for i in range(len(shop_items)):
            shop_item = shop_items[i]
            item_price = item_prices[i]
            print(f'{i + 1}. {shop_item} - ${item_price:.2f}')
        print('')
    elif action == '3':
        remove_items = int(input('What item number would you like to remove?: '))
        remove_item = remove_items - 1 
        if remove_item in range(len(shop_items)):
            shop_items.pop(remove_item)
            item_prices.pop(remove_item)
            print(f'You have removed item number {remove_items} from your cart successfully.')
        else:
            print('Sorry, you do not have that item number!')
        print('')
    elif action == '4':
        subtotal = sum(item_prices)   
        print(f'Your current subtotal is: ${subtotal:.2f}')
        print('')
    elif action == '5':
        print('Thank you for shopping!')
    else:
        print('Invalid option')