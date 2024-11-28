import logging
from utils.emi_calculator import calculate_monthly_installment

logger = logging.getLogger()
file_path = "loan_calculator/TestCaseOutput.txt"

def run_test_case(principal, rate, years, writer):
    """
    Runs a single test case for loan EMI calculation.

    This function validates the provided input values (principal, rate, and years), calculates the EMI using the `calculate_monthly_installment` function if valid, and logs and writes the result. If any validation fails, an AssertionError is raised, and the error message is logged and written.

    Parameters:
    - principal (float): The loan amount.
    - rate (float): The annual interest rate (in percentage).
    - years (int): The loan duration in years.
    - writer (file object): A file object where results or errors are written.

    Returns:
    - None
    """
    try:
        # Validate input using assert statements
        assert rate >= 0, "Rate of interest should be a positive value."
        assert 0 < years <= 30, "Loan duration must be between 1 and 30 years."

        # If validation passes, calculate EMI
        emi = calculate_monthly_installment(principal, rate, years)
        result = f"Principal: {principal}, Rate: {rate}%, Years: {years} => EMI: {emi:.2f}"
        logger.info(result)
        writer.write(result + "\n")

    except AssertionError as ex:
        # Log and write validation errors
        error = f"Error - Principal: {principal}, Rate: {rate}%, Years: {years} => {ex}"
        logger.error(error)
        writer.write(error + "\n")

def run_all_test_cases(writer):
    """
    Runs all user-defined test cases for loan EMI calculation.

    This function prompts the user to input test case values for loan EMI calculation. It also validates the inputs and logs the results.

    Parameters:
    - writer (file object): A file object where test case results or errors are written.

    Returns:
    - None
    """
    logger.info("Running Test Cases")
    writer.write("\nTest Cases:\n")

    # Ask user for the number of test cases
    num_cases = int(input("Enter the number of test cases: "))

    for i in range(num_cases):
        print(f"\nTest Case {i + 1}:")

        # Get input for each test case
        try:
            principal = float(input("Enter the principal amount: "))
            rate = float(input("Enter the annual interest rate (in percentage): "))
            years = int(input("Enter the loan duration in years: "))

            # Run the test case
            writer.write(f"Test Case {i + 1}:\n")
            run_test_case(principal, rate, years, writer)

        except ValueError:
            logger.error(f"Invalid input for Test Case {i + 1}. Please enter valid numerical values.")
            writer.write(f"Invalid input for Test Case {i + 1}. Please enter valid numerical values.\n")

    logger.info(f"Results saved to {file_path}")

if __name__ == "__main__":
    try:
        with open(file_path, "w") as writer:
            run_all_test_cases(writer)
    except Exception as e:
        logger.error(f"Error opening file for writing: {e}")
