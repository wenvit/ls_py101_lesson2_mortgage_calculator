# Mortgage Calculator

#######################
# Define functions

# Prompt for messages
def display_prompt(message):
    print(f'==> {message}')

# Check for valid numeric input strings
def invalid_number(number_str):
    try:
        float(number_str)
        if float(number_str) <= 0:
            raise ValueError('Number must be > 0.')
    except ValueError:
        return True
    return False

# Convert numeric strings to float data types
def str_to_num(number_str):
    return float(number_str)

# Calculate monthly payment including interest:
#   -- convert APR to monthly interest
#   -- convert loan duration in years to months
def payment_with_int(amount, annual_int, years):
    monthly_int = (annual_int / 100) / 12
    months = years * 12

    return amount * (monthly_int / (1 - (1 + monthly_int) ** (-months)))

# Calculate monthly payment without interest
def payment_int_free(amount, years):
    months = years * 12

    return amount / months

#######################
display_prompt('This is the Mortgage Calculator!')

while True:

    # Ask user to input loan amount, validate input, convert to float
    display_prompt('Please enter your loan amount ($):')
    loan_amt_str = input()

    while invalid_number(loan_amt_str):
        display_prompt('Must enter a positive number.')
        loan_amt_str = input()

    loan_amt = str_to_num(loan_amt_str)

    # Ask user if paying interest, ask for interest (in %),
    # validate input, convert to float
    display_prompt('Are you paying interest on your loan (y/n)?')
    include_int = input()

    if include_int == 'y':
        display_prompt('Enter the Annual Percentage Rate (APR) '
                       'as a percentage (%).')
        apr_str = input()

        while invalid_number(apr_str):
            display_prompt('Must enter a positive number.')
            apr_str = input()

        apr = str_to_num(apr_str)

    # Ask user for loan duration in years, validate input, convert to float
    display_prompt('Enter the duration of your loan (years):')
    duration_yr_str = input()

    while invalid_number(duration_yr_str):
        display_prompt('Must enter a positive number.')
        duration_yr_str = input()

    duration_yr = str_to_num(duration_yr_str)

    # Calculate payment depending on whether or not interest is included
    if include_int == 'y':
        monthly_payment = payment_with_int(loan_amt, apr, duration_yr)
    else:
        monthly_payment = payment_int_free(loan_amt, duration_yr)

    # Print results
    display_prompt(f'Your monthly payment will be ${monthly_payment:.2f}.')

    # Ask if user would like to calculate another payment
    display_prompt('Would you like to perform another calculation?')

    user_response = input()
    if user_response and user_response[0].lower() != 'y':
        break