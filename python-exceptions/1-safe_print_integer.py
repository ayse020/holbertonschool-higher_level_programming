def safe_print_integer(value):
    """
    Prints an integer using "{:d}".format().
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
