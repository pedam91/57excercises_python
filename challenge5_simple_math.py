def enter_number(order_number):
    while True:
        try:
            ret_val = int(input("What is the %s number? " % order_number))
            if ret_val < 0:
                print("Input must be a positive number!")
                continue
        except ValueError:
            print("Input must be a number!")
            continue
        return ret_val


first = enter_number('first')
second = enter_number('second')

print('%i + %i = %i' % (first, second, first + second) + '\n' +
      '%i - %i = %i' % (first, second, first - second) + '\n' +
      '%i * %i = %i' % (first, second, first * second) + '\n' +
      '%i / %i = %i' % (first, second, first / second))
