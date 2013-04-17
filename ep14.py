#The following iterative sequence is defined for the set of positive integers:
#
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.
iterm = 0
num = 0
for j in range(100000, 999999):
    couter = 0
    i = j
    while i != 1:
        if i % 2 == 0:
            i = i / 2
            couter = couter + 1
        else:
            i = 3 * i + 1
            couter = couter + 1
        if couter > iterm:
            iterm = couter
            num = j
print "Length is :", iterm
print "The number is :", num
