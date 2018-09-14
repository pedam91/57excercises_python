import math

ONE_GALLON_COVER = 350

length = float(input('Length? '))
width = float(input('Width? '))

ceiling_area = length * width

needed_gallons = math.ceil(ceiling_area / ONE_GALLON_COVER)

print('Needed gallons: %i' % needed_gallons)

# round room
print('Round room: %.2f square feet' % (math.pi * pow(length, 2)))
