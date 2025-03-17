def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    i = 0
    unique_digits_cnt = 0
    while i < 10:
        if has_digit(n, i):
            unique_digits_cnt += 1
        i += 1
    print(unique_digits_cnt)

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n :
        if k == (n % 10):
            return True
        n = n // 10
    return False
