#!/user/bin/python
# Filename: ep7.py
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#we can see that the 6th prime is 13.

#What is the 10 001st prime number?

import EPpackage as e
import math as m
ans = 0
j = 1
number = 600851475143
i = m.floor(m.sqrt(number))
if e.isPrime(i):
    print "This is a prime", i
else:
    print "The number is not a prime", i
if e.isPrime(number):
    print "This is a prime", number
else:
    print "The number is not a prime", number
while j < i:
    if e.isPrime(j):
        if number % j == 0:
            ans = j
    j += 2
print ans
