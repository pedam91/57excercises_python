import math

def print_pieces(count):
    if count == 1:
        return 'piece'
    return 'pieces'


people_count = int(input('How many people? '))

pizza_count = int(input('How many pizzas do you have? '))
slices_per_pizza = int(input('Slices per pizza? '))

total_slices = pizza_count * slices_per_pizza
slices_per_person = total_slices / people_count
leftovers = total_slices % people_count

print('total slices: %i' % total_slices)

print('%i people with %i pizzas' % (people_count, pizza_count))
print('Each person gets %i %s of pizza.' % (slices_per_person, print_pieces(slices_per_person)))
print('There are %i leftover %s' % (leftovers, print_pieces(slices_per_person)))


# 3rd challenge:
slices_list = []

total_slices2 = 0
for i in range(people_count):
    total_slices2 = total_slices2 + int(input("Insert slices for person no. %i: " % (i+1)))

needed_pizzas = math.ceil(total_slices2 / slices_per_pizza)
print('Needed pizzas: %i' % needed_pizzas)
