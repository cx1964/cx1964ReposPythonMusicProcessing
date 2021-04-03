# file: my_uilities.copy
# function: miscellaneous utility functions

def roundTo(numberValue, baseValue):
    """
    numberValue: a number to round
    baseValue:   a number multiples
    """
    # Round a numberValue, to multiples of baseValue
    return( numberValue + (baseValue - numberValue) % baseValue )