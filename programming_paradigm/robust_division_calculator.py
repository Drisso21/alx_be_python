def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        try:
            result = numerator / denominator
            return "The result of the division is: {result}".format(result=result)
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

    except Exception as e:
        return f"An unexpected error occurred: {e}"
