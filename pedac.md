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
Check that entered values are valid and can be converted to float types. 
Calculate monthly interest rate by dividing APR / 12. 
Calculate loan duration in months by multiplying years by 12 months/yr. 
Calculate monthly payment using given formula. 
Ask if user wants to calculate another monthly payment.

### TEST CASES 

Interest rate of 0

### ALGORITHM

1. Define function `prompt` with parameter `message` (str) that 
   prints f-string combining ==> with interpolated `message`
2. Define function `invalid_num` that returns `True` if input numeric strings cannot be converted to float type. Use try/except block to  catch `ValueError` & return `True`, otherwise return `False`
3. Define function `str_to_num` to convert valid numeric strings to floats
4. Define function `payment_with_int` that returns calculated monthly mortgage payment based on above formula
5. Define function `payment_int_free` that returns calculated monthly mortgage payment without interest: loan amount / months
6. Print out header for monthly mortgage payment calculator
7. Wrap rest of code steps in `while True` loop
8. Wrap user input requests in `while True` loops, passing input values as arguments to `invalid_num` function, then passing returned valid strings to `str_to_num` function to convert to floats
  * Ask user to input loan amount ($)
  * Ask user if paying interest. If 'y', ask user to input APR as a percentage
  * Ask user to input loan duration in years
9. If user paying interest, calculate monthly mortgage payment with `payment_with_int`. If no interest, calculate monthly mortgage payment with `payment_int_free`
10. Ask user if they'd like to do another calculation, if not yes, break