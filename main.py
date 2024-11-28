import logging
from utils.emi_calculator import calculate_monthly_installment
from utils.exceptions import InvalidRateException, InvalidLoanDurationException
from utils.decorators import retry_on_failure  # Import the decorator

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def validate_loan_input(principal, annual_interest_rate, loan_duration_years):
    """
    Validates the user input for loan principal, interest rate, and duration.
    Raises exceptions if the values are invalid.
    """
    if annual_interest_rate < 0:
        raise InvalidRateException("Rate of interest should be a positive value.")
    if loan_duration_years <= 0 or loan_duration_years > 50:
        raise InvalidLoanDurationException("Loan duration must be between 1 and 50 years.")
    return principal, annual_interest_rate, loan_duration_years

@retry_on_failure(attempts=3)
def get_loan_input():
    """
    Handles user input for loan principal, interest rate, and duration.
    Returns validated input.
    """
    principal = float(input("Enter loan principal amount: "))
    annual_interest_rate = float(input("Enter annual interest rate (in %): "))
    loan_duration_years = int(input("Enter loan duration (in years): "))

    return validate_loan_input(principal, annual_interest_rate, loan_duration_years)

def main():
    """
    Main function that serves as the entry point for the Loan Installment Calculator program.
    It handles user input, validates the input for principal, interest rate, and loan duration, 
    and calculates the monthly installment (EMI) based on the provided information.
    Results are written to a file and logged.
    """
    file_path = "loan_calculator/LoanCalculatorOutput.txt"
    with open(file_path, "w") as writer:
        logger.info("Loan Installment Calculator Started")
        writer.write("User Input Results:\n")

        principal, annual_interest_rate, loan_duration_years = get_loan_input()

        if principal is not None:  # Proceed only if input was valid
            monthly_installment = calculate_monthly_installment(principal, annual_interest_rate, loan_duration_years)
            result = f"Principal: {principal}, Rate: {annual_interest_rate}%, Years: {loan_duration_years} => EMI: {monthly_installment:.2f}"
            logger.info(f"Your monthly installment is: {monthly_installment:.2f}")
            writer.write(result + "\n")
        else:
            writer.write("Invalid input provided after 3 attempts. Program exited.\n")

    logger.info(f"Results saved to {file_path}")

if __name__ == "__main__":
    main()
