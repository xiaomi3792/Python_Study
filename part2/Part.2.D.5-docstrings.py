def is_prime(n):
    """
    return a boolean value based upon
    whether the argument n is a prime number.
    """
    if n < 2:
        return false
    if n == 2:
        return True
    for m in range(2,int(n**0.5)+1):
        if (n % m) == 0:
            return False
    else:
        return True

print(help(is_prime))
print(is_prime.__doc__)
