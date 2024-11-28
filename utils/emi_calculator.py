def calculate_monthly_installment(principal, annual_rate, years):
    """ 
    Calculate the monthly installment (EMI) for a loan based on the principal, annual interest rate, and loan duration in years. 
    
    The formula used for calculating the EMI is: EMI = (P * r * (1 + r)^n) / ((1 + r)^n - 1) 
    where: 
    - P is the principal loan amount 
    - r is the monthly interest rate (annual rate divided by 12 months) 
    - n is the total number of payments (loan duration in years multiplied by 12) 
    
    If the annual interest rate is zero, the EMI is simply the principal divided by the total number of payments. 
    
    Parameters: 
    - principal (float): The loan amount. 
    - annual_rate (float): The annual interest rate (in percentage). 
    - years (int): The loan duration in years. 
    
    Returns: 
    - float: The monthly installment (EMI). 
    """
    monthly_rate = annual_rate / 100 / 12
    number_of_payments = years * 12

    if monthly_rate == 0:
        return principal / number_of_payments

    emi = (principal * monthly_rate * (1 + monthly_rate) ** number_of_payments) / \
          ((1 + monthly_rate) ** number_of_payments - 1)
    return emi