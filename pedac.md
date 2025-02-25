## Problem statement

Build a mortgage calculator that determines the monthly payment assuming that interest is compounded monthly.

You'll need three pieces of information:
* the loan amount
* the Annual Percentage Rate (APR)
* the loan duration
From the above, you'll need to calculate the following two things:
* monthly interest rate (APR / 12)
* loan duration in months

Use the following formula:
m = p * (j / (1 - (1 + j) ** (-n)))
where:
       m = monthly payment
       p = loan amount
       j = monthly interest rate
       n = loan duration in months

## PEDAC

### INPUTS
user inputs:
1. loan amount, 
2. annual percentage rate (APR),
3. loan duration in years

### OUTPUTS

monthly payment

### RULES

1. Monthly interest rate = APR / 12
2. Loan duration in months = loan duration in years * 12 months/yr
3. Interest is compounded monthly
4. Use explicit names for variables in monthly payment formula
5. Print payment amount as dollars & cents
6. Ask user to input interest rate as percent (e.g., for 5%, enter 5)

### MENTAL MODEL

Ask user to input loan amount, annual percentage rate (APR), and loan duration.
Check that entered values are valid and can be converted to float types. Calculate monthly interest rate by dividing APR / 12. Calculate loan duration in months by multiplying years by 12 months/yr. Calculate monthly payment using given formula. Ask if user wants to calculate another monthly payment.

### TEST CASES 

Interest rate of 0

### ALGORITHM

1. Define function `prompt` with parameter `message` (str) that 
   prints f-string combining ==> with interpolated `message`
2. Define function `invalid_num` that returns `True` if input numeric strings cannot be converted to float type. Use try/except block to 
catch `ValueError` & return `True`, otherwise return `False`
3. Define function `monthly_payment` that returns calculated monthly mortgage payment based on above formula
4. Print out header for monthly mortgage payment calculator
5. Wrap rest of code steps in `while True` loop
6. Wrap user input requests in `while True` loops passing input values as arguments to `invalid_num` function
     -- Ask user to input loan amount ($)
     -- Ask user to input APR as a percentage
     -- Ask user to input loan duration in years
7. Ask user if they'd like to do another calculation, if not yes, break