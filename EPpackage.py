#!user/bin/python
#This package is all the functions that is needed during Euler Project
#File name:EPpackage.py
import math as m


def SumOfTimesN(n, upbound):
    """
    This funciton returns the sum of all number
    that is of mutitples of n under limit.
    For EP No.1
        """
    sum = 0
    i = 1
    if n == upbound or n > upbound:
        print 'Eerro! %d must bigger then the upper bound %d.', n, upbound
    if n == 0:
        print 'Eerro! The sum of mutiples of %d is meaningless.', n
    while i * n < upbound:
        sum += n * i
        i += 1
    return sum


def fiboGenUptoN(n):
    """
    This fouction generate the fabonacci sequence up to n and
    return it as a list
        """
    fibo = []
    a, b = 0, 1
    if n == 0:
        print "Error! n= %d is meaningless", n
    while b < n:
        fibo.append(b)
        a, b = b, a + b
    return fibo


def fiboGenTermsN(n):
    """
    This fouction generate the first n terms of fabonacci sequence and
    return it as a list
        """
    fibo = []
    i = 0
    a, b = 0, 1
    if n == 0:
        print "Error! n= %d is meaningless", n
    while i < n:
        fibo.append(b)
        a, b = b, a + b
        i += 1
    return fibo


def isPrime(n):
    """ This is a founction that check if n is a prime number
        """
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = m.floor(m.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            if n % (f + 2) == 0:
                return False
            f = f + 6
    return True


def Factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * Factorial(n - 1)


# Sum of proper divisors
def SPD(n):
    sum = 0
    i = 0
    if n < 4:
        sum = 1
    else:
        for i in range(1, (n / 2 + 1)):
            if n % i == 0:
                sum += i
    return sum


def GetDigit(n):
    """ This is a founction that return all the
    digits of a number as a list
        """
    diglist = []
    digit = 0
    remain = 0
    num = n
    l = len(str(n))
    for i in range(l - 1, -1, -1):
        digit = num / 10 ** i
        remain = num % 10 ** i
        num = remain
        diglist.append(digit)
    return diglist
