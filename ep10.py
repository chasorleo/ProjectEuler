#!/user/bin/python
# Filename: ep7.py
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#we can see that the 6th prime is 13.

#What is the 10 001st prime number?

import EPpackage as e
limit = 2000001
sum = 0
i = 2
while i < limit:
    if e.isPrime(i):
        sum = i + sum
    i += 1
print "The number is ", sum
