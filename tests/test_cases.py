import logging
from utils.emi_calculator import calculate_monthly_installment
from utils.exceptions import InvalidRateException, InvalidLoanDurationException

logger = logging.getLogger()

def run_test_case(principal, rate, years, writer):
    """
    Runs a single test case for loan EMI calculation.

    This function validates the provided input values (principal, rate, and years), calculates the EMI using the `calculate_monthly_installment` function if valid, and logs and writes the result. If any validation fails (e.g., negative rate or invalid loan duration), an exception is raised and the error message is logged and written.

    Parameters:
    - principal (float): The loan amount.
    - rate (float): The annual interest rate (in percentage).
    - years (int): The loan duration in years.
    - writer (file object): A file object where results or errors are written.

    Returns:
    - None
    """
    try:
        if rate < 0:
            raise InvalidRateException("Rate of interest should be a positive value.")
        if years <= 0 or years > 30:
            raise InvalidLoanDurationException("Loan duration must be between 1 and 30 years.")

        emi = calculate_monthly_installment(principal, rate, years)
        result = f"Principal: {principal}, Rate: {rate}%, Years: {years} => EMI: {emi:.2f}"
        logger.info(result)
        writer.write(result + "\n")
    except (InvalidRateException, InvalidLoanDurationException) as ex:
        error = f"Error - Principal: {principal}, Rate: {rate}%, Years: {years} => {ex}"
        logger.error(error)
        writer.write(error + "\n")

def run_all_test_cases(writer):
     """
    Runs all predefined test cases for loan EMI calculation.

    This function iterates over a list of predefined test cases, calls `run_test_case` for each, and logs and writes the result of each test case. It also handles cases where errors are raised due to invalid inputs (e.g., negative interest rate, invalid loan duration).

    Parameters:
    - writer (file object): A file object where test case results or errors are written.

    Returns:
    - None
    """
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