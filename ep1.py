#!user/bin/python
#This is the program implemetation of Euler Project P1
#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


def SumOfTimesN(n, upbound):
    """
    This funciton returns the sum of all number
    that is of mutitples of n under limit.
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

sum = SumOfTimesN(3, 1000) + SumOfTimesN(5, 1000) - SumOfTimesN(15, 1000)
print 'The result sum is', sum
