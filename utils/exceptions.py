class InvalidRateException(Exception):
    """
    Exception raised for invalid interest rates.

    This exception is used when an invalid interest rate is provided, such as a negative interest rate, which is not allowed in the loan calculation.

    Attributes:
        message (str): The error message that describes the exception.
    """
    def __init__(self, message):
        """
        Initialize the exception with a message.

        Parameters:
        - message (str): The error message that describes the exception.
        """
        super().__init__(message)

class InvalidLoanDurationException(Exception):
    """
    Exception raised for invalid loan durations.

    This exception is used when an invalid loan duration is provided, such as a loan duration that is less than or equal to zero, or exceeds the allowed maximum duration (e.g., 50 years).

    Attributes:
        message (str): The error message that describes the exception.
    """
    def __init__(self, message):
        """
        Initialize the exception with a message.

        Parameters:
        - message (str): The error message that describes the exception.
        """
        super().__init__(message)