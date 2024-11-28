import logging
from utils.emi_calculator import calculate_monthly_installment
from utils.exceptions import InvalidRateException, InvalidLoanDurationException

logger = logging.getLogger()
file_path = "loan_calculator/TestCaseOutput.txt"

def run_test_case(principal, rate, years, writer):
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

    logger.info(f"Results saved to {file_path}")

if __name__ == "__main__":
    try:
        with open(file_path, "w") as writer:
            run_all_test_cases(writer)
    except Exception as e:
        logger.error(f"Error opening file for writing: {e}")
