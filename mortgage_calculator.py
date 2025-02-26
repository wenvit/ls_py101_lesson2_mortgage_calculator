# Mortgage Calculator

#######################
# Define functions

# Prompt for messages
def prompt(message):
    print(f'==> {message}')

# Check that input strings can be converted to float data types
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

# Convert valid numeric strings to float data types
def str_to_num(number_str):
    return float(number_str)

# Calculate monthly payment amount including interest:
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
prompt('This is the Mortgage Calculator!')

while True:

    # Ask user to input loan amount, validate input, convert to float
    prompt('Please enter your loan amount ($):')
    loan_amt_str = input()
    while invalid_number(loan_amt_str):
        prompt('The loan amount must be a valid number.')
        loan_amt_str = input()
    loan_amt = str_to_num(loan_amt_str)

    # Ask user if they're paying interest, ask for interest (in %),
    # validate input, convert to float
    prompt('Are you paying interest on your loan (y/n)?')
    include_int = input()
    if include_int == 'y':
        prompt('Enter the Annual Percentage Rate (APR) as a percentage (%).')
        apr_str = input()
        while invalid_number(apr_str):
            prompt('Please enter a valid number.')
            apr_str = input()
        apr = str_to_num(apr_str)

    # Ask user for loan duration in years, validate input, convert to float
    prompt('Enter the duration of your loan (years):')
    duration_yr_str = input()
    while invalid_number(duration_yr_str):
        prompt('Try again using a valid number.')
        duration_yr_str = input()
    duration_yr = str_to_num(duration_yr_str)

    # Calculate monthly payment depending on whether interest
    # is included or not
    if include_int == 'y':
        monthly_payment = payment_with_int(loan_amt, apr, duration_yr)
    else:
        monthly_payment = payment_int_free(loan_amt, duration_yr)

    # Print results
    prompt(f'Your monthly payment will be ${monthly_payment:.2f}.')

    # Ask if user would like to calculate another payment
    prompt('Would you like to perform another mortgage calculation?')
    user_response = input()
    if user_response and user_response[0].lower() != 'y':
        break