input_string = input('What is the input string? ')
length = len(input_string.lstrip())

# if length == 0:
#     output = 'User must enter something into program.'
# else:
#     output = input_string + ' has ' + str(length) + ' characters.'
#
# print(output)

print('User must enter something into program.' if length == 0
      else input_string + ' has ' + str(length) + ' characters.')
