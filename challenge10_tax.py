def input_item(total_amount):
    while True:
        item_price = int(input('Enter the item price: '))
        item_quantity = int(input('Enter the item quantity: '))
        total_amount += item_price * item_quantity

        while True:
            response = input('Do you want to add more items?(y/n): ')
            if response == 'y' or response == 'n':
                break
            else:
                print('Wrong value, try again.')
        if response == 'y':
            continue
        else:
            break
    return total_amount


# item1_price = 25
# item1_quantity = 2
# item2_price = 10
# item2_quantity = 1
# item3_price = 4
# item3_quantity = 1
# subtotal = item1_price * item1_quantity + item2_price * item2_quantity + item3_price * item3_quantity

subtotal = input_item(0)

tax = (5.5 * subtotal) / 100
total = subtotal + tax

print('Subtotal: $%.2f' % subtotal)
print('Tax: $%.2f' % tax)
print('Total: $%.2f' % total)
