from time import time
start_time = time()
ordin = 365
orlist = [0, 3, 3, 6, 8, 11, 13, 16, 19, 21, 24, 26]
leap = 366
leaplist = [0, 3, 4, 7, 9, 12, 14, 17, 20, 22, 25, 27]
day = 0
firstday = 1  # what day is the first day of the year
lastday = 0
for i in range(1901, 2001):
    oldfirstday = firstday
    ml = []
    if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:  # leap year
        nday = leap
        for j in leaplist:
            if (j + firstday + 1) % 7 == 0:
                day += 1
                ml.append(leaplist.index(j) + 1)
    else:
        nday = ordin
        for j in orlist:
            if (j + firstday + 1) % 7 == 0:
                day += 1
                ml.append(orlist.index(j) + 1)
    firstday = (nday % 7 + oldfirstday) % 7
    if firstday == 0:
        firstday = 7
    print 'The month strated wiht sunday in', i, 'is', ml
print day

print time() - start_time, "seconds"
