i = 998001
while i > 900009:
    d1 = i % 10
    d2 = i % 100 / 10
    d3 = i % 1000 / 100
    d4 = i % 10000 / 1000
    d5 = i % 100000 / 10000
    d6 = i % 1000000 / 100000
    if d1 == d6 and d2 == d5 and d3 == d4:
        for j in range(100, 999):
            if i % j == 0 and i / j > 99 and i / j < 999:
                print "i = :", i
                print "j = :", j
                print i / j
                break
    i = i - 1
