''' A unit testing framework for ECOR1042 '''

def check_equal(description: str, actual, expected) -> None:
    """
    Print a "passed" message if actual and expected have same type and
    are equal (as determined by the == operator); otherwise, print a 
    "fail" message.
    
    Parameter "description" should provide information that will help us
    interpret the test results; e.g., the call expression that yields
    actual.
    
    Parameters "actual" and "expected" are typically the actual value returned
    by a call expression and the value we expect a correct implementation
    of the function to return, respectively. Both parameters must have the same
    type, which must be a type for which == is used to determine if two values
    are equal. Don't use this function to check if floats, lists of floats,
    tuples of floats, etc. are equal. 
    """
    actual_type = type(actual)
    expected_type = type(expected)
    if actual_type != expected_type:
        
        # The format methods is explained on pages 119-122 of 
        # 'Practical Programming', 3rd ed.
        
        print("{0} FAILED: expected ({1}) has type {2}, " \
              "but actual ({3}) has type {4}".
              format(description, expected, str(expected_type).strip('<class> '), 
                      actual, str(actual_type).strip('<class> ')))
    elif actual != expected:
        print("{0} FAILED: expected {1}, got {2}".
              format(description, expected, actual))
    else:
        print("{0} PASSED".format(description))
    print("------")

