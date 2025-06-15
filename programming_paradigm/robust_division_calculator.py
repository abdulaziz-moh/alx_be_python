def safe_divide(numerator, denominator):
    """
    Performs division, handling ZeroDivisionError and ValueError for non-numeric inputs.

    Args:
        numerator (str): The string representation of the numerator.
        denominator (str): The string representation of the denominator.

    Returns:
        str: A message indicating the result of the division or an error.
    """
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        if den == 0:
            # Explicitly check for zero denominator before division
            # to provide a more specific message than a raw ZeroDivisionError
            return "Error: Cannot divide by zero."
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        # This catch is technically redundant due to the explicit check above,
        # but included to demonstrate catching the specific exception.
        return "Error: Cannot divide by zero."