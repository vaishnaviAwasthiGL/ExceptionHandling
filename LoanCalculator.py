import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

class InvalidRateException(Exception):
    """Custom exception for negative value for rate."""
    def __init__(self, message):
        super().__init__(message)

class InvalidLoanDurationException(Exception):
    """Custom exception for invalid loan durations."""
    def __init__(self, message):
        super().__init__(message)

def calculate_monthly_installment(principal, annual_rate, years):
    """Calculate the monthly EMI for a loan."""
    monthly_rate = annual_rate / 100 / 12
    number_of_payments = years * 12

    if monthly_rate == 0:
        return principal / number_of_payments

    emi = (principal * monthly_rate * (1 + monthly_rate) ** number_of_payments) / \
          ((1 + monthly_rate) ** number_of_payments - 1)
    return emi

def run_test_case(principal, rate, years, writer):
    """Run a single test case and save the result."""
    try:
        if rate < 0:
            raise InvalidRateException("Rate of interest should be a positive value.")
        if years <= 0 or years > 30:
            raise InvalidLoanDurationException("Loan duration must be between 1 and 30 years.")

        emi = calculate_monthly_installment(principal, rate, years)
        result = f"Principal: {principal}, Rate: {rate}%, Years: {years} => EMI: {emi:.2f}"
        logger.info(result)
        writer.write(result + "\n")
    except InvalidRateException as ex:
        error = f"Rate Error - Principal: {principal}, Rate: {rate}%, Years: {years} => {ex}"
        logger.error(error)
        writer.write(error + "\n")
    except InvalidLoanDurationException as ex:
        error = f"Duration Error - Principal: {principal}, Rate: {rate}%, Years: {years} => {ex}"
        logger.error(error)
        writer.write(error + "\n")

def run_all_test_cases(writer):
    """Run all predefined test cases."""
    logger.info("Running Test Cases")
    writer.write("\nTest Cases:\n")

    test_cases = [
        (100000, 5, 10),
        (200000, 0, 20),
        (50000, -7.5, 5),
        (300000, 10, -15),
        (1000000, 3, 25)
    ]

    for i, (principal, rate, years) in enumerate(test_cases, start=1):
        writer.write(f"Test Case {i}:\n")
        run_test_case(principal, rate, years, writer)

def main():
    file_path = "LoanTestCasesOutput.txt"
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

                if loan_duration_years < 0 or loan_duration_years > 50:
                    raise InvalidLoanDurationException("Loan duration must be between 1 and 50 years.")

                monthly_installment = calculate_monthly_installment(principal, annual_interest_rate, loan_duration_years)
                result = f"Principal: {principal}, Rate: {annual_interest_rate}%, Years: {loan_duration_years} => EMI: {monthly_installment:.2f}"
                logger.info(f"Your monthly installment is: {monthly_installment:.2f}")
                writer.write(result + "\n")
                is_valid_input = True
            except ValueError as ex:
                logger.error(f"Error: Please enter numeric values only. {ex}")
                writer.write(f"Error: Invalid input provided. {ex}\n")
            except InvalidRateException as ex:
                logger.error(f"Rate Error: {ex}")
                writer.write(f"Rate Error: {ex}\n")
            except InvalidLoanDurationException as ex:
                logger.error(f"Time Error: {ex}")
                writer.write(f"Time Error: {ex}\n")

            if not is_valid_input:
                attempts -= 1
                if attempts > 0:
                    logger.warning(f"You have {attempts} attempts left.")
                else:
                    logger.error("Sorry, you have used all your attempts. Exiting the program.")
                    writer.write("All attempts used. Program exited.\n")

        if is_valid_input:
            logger.info("Thank you for using the Loan Installment Calculator.")
            run_all_test_cases(writer)

    logger.info(f"Results saved to {file_path}")

if __name__ == "__main__":
    main()
