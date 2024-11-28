# utils/decorators.py
import logging
from utils.exceptions import InvalidRateException, InvalidLoanDurationException

# Configure logging
logger = logging.getLogger()

def retry_on_failure(attempts=3):
    """
    Decorator to retry the decorated function a specified number of times
    in case of invalid input.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            remaining_attempts = attempts
            while remaining_attempts > 0:
                try:
                    return func(*args, **kwargs)
                except (ValueError, InvalidRateException, InvalidLoanDurationException) as ex:
                    logger.error(f"Error: {ex}")
                    remaining_attempts -= 1
                    if remaining_attempts > 0:
                        logger.warning(f"You have {remaining_attempts} attempts left.")
                    else:
                        logger.error("All attempts used. Exiting the program.")
            return None  # If all attempts are used up, return None
        return wrapper
    return decorator
