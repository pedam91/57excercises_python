CONVERSION_FACTOR = 0.09290304

length_feet = int(input('What is the length of the room in feet? '))
width_feet = int(input('What is the width of the room in feet? '))

print('You entered dimensions of %i feet by %i feet' % (length_feet, width_feet))

area_feet = length_feet * width_feet
area_meters = area_feet * CONVERSION_FACTOR

print('The area is\n%i square feet\n%.3f square meters' % (area_feet, area_meters))
