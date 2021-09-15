#A simple supermarket shopping list

shopping_list = []

# Sum is the counter to add up the total price at the end of the program
sum = 0

#Lines to enter data (Item name, quantity and Unit price)
print('SHOPPING LIST')
print('Press ENTER to finish the list.')
while True:
    item_name = str(input('Item:'))
    if not item_name:
        break
    try:
        number = int(input('Number of items:'))
    except ValueError:
        print('Oops, something went wrong!')
        continue
    else:
        try:
            unit = float(input('Unit price:'))
        except ValueError:
            print('Oops, something went wrong!')
            continue
        shopping_list.append([item_name, number, unit])

#Lines to format a table for the data input
print()
s_list = 'SHOPPING LIST'
print('-'*64)
print('|{:^62}|' .format(s_list))
print('-'*64)
item_head = 'Item'
quantity_head = 'Quantity'
unit_price_head = 'Unit price'
price_head = 'Item total price'
print('|{:^12}|'.format(item_head), end=' ')
print('{:^13}|'.format(quantity_head), end=' ')
print('{:^14}|'.format(unit_price_head), end=' ')
print('{:^12} |'.format(price_head))
print('-'*64)

#Iterative cicle to organize items, quantity, unit price and total item price in the table
for item in shopping_list:
    print('| {:^10} | {:^12} | R$:{:^10.2f} | R$: {:^12.2f} |' .format(item[0], item[1], item[2], item[1] * item[2]))
    sum += item[1] * item[2]
print('-'*64)

#The final price of the shopping list
print('TOTAL: R${}' .format(sum))

