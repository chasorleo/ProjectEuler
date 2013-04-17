#!/user/bin/python
# Filename: ep7.py
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#we can see that the 6th prime is 13.

#What is the 10 001st prime number?

import EPpackage as e
counter = 0
limit = 10001
i = 1
while counter < limit:
    if e.isPrime(i):
        counter += 1
    i += 1
print "The prime number is ", i - 1
