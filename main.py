import logging
from utils.emi_calculator import calculate_monthly_installment
from utils.exceptions import InvalidRateException, InvalidLoanDurationException
from tests.test_cases import run_all_test_cases

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def main():
    """
    Main function that serves as the entry point for the Loan Installment Calculator program. 
    It handles user input, validates the input for principal, interest rate, and loan duration, and calculates the monthly installment (EMI) based on the provided information. 
    Results are written to a file and logged. 
    
    The program allows up to three attempts to input valid data. 
    After each invalid input, an error message is logged and the remaining attempts are displayed. 
    If the input is valid, the program writes the result to a file and runs all test cases.
    """
    file_path = "loan_calculator/LoanCalculatorOutput.txt"
    with open(file_path, "w") as writer:
        logger.info("Loan Installment Calculator Started")
        writer.write("User Input Results:\n")

        attempts = 3
        is_valid_input = False

        while attempts > 0 and not is_valid_input:
            try:
                principal = float(input("Enter loan principal amount: "))
                annual_interest_rate = float(input("Enter annual interest rate (in %): "))
                loan_duration_years = int(input("Enter loan duration (in years): "))

                if annual_interest_rate < 0:
                    raise InvalidRateException("Rate of interest should be a positive value.")
                if loan_duration_years <= 0 or loan_duration_years > 50:
                    raise InvalidLoanDurationException("Loan duration must be between 1 and 50 years.")

                monthly_installment = calculate_monthly_installment(principal, annual_interest_rate, loan_duration_years)
                result = f"Principal: {principal}, Rate: {annual_interest_rate}%, Years: {loan_duration_years} => EMI: {monthly_installment:.2f}"
                logger.info(f"Your monthly installment is: {monthly_installment:.2f}")
                writer.write(result + "\n")
                is_valid_input = True
            except (ValueError, InvalidRateException, InvalidLoanDurationException) as ex:
                logger.error(ex)
                writer.write(f"Error: {ex}\n")
                attempts -= 1
                if attempts > 0:
                    logger.warning(f"You have {attempts} attempts left.")
                else:
                    logger.error("All attempts used. Exiting the program.")
                    writer.write("All attempts used. Program exited.\n")

        if is_valid_input:
            run_all_test_cases(writer)

    logger.info(f"Results saved to {file_path}")

if __name__ == "__main__":
    main()