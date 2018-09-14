def calculate_simple_interest(principal, rate_of_interest, number_of_years):
    return principal * (1 + rate_of_interest / 100 * number_of_years)


principal_input = 1500
rate_of_interest_input = 4.3
number_of_years_input = 4

# worth = principal * (1 + rate_of_interest / 100 * number_of_years)
worth = calculate_simple_interest(principal_input, rate_of_interest_input, number_of_years_input)

print('After %i years at %.2f%%, the investment will be worth $%i' % (number_of_years_input, rate_of_interest_input, worth))

print('Amount at the end of each year:')
for x in range(number_of_years_input):
    print('Year %i, amount: %.2f' % (x+1, principal_input * (1 + rate_of_interest_input / 100 * (x+1))))
