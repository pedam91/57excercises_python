import datetime

current_age = int(input('What is your current age? '))
retire_age = int(input('At what age would you like to retire? '))
years_left = retire_age - current_age

# current_year = datetime.datetime.now().year
current_year = datetime.date.today().year
# print('current year: ' + str(current_year))

if years_left < 0:
    print('You can retire now!')
else:
    print('You have %s year left until you can retire.' % years_left)
    print('It\'s %s, so you can retire in %s.' % (current_year, current_year + years_left))
