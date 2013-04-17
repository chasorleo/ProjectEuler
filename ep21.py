import EPpackage as e
i = 0
sum = 0
for n in range(1, 9999):
    i = e.SPD(n)
    if e.SPD(i) == n and i != n:
        print n
        sum += n
print sum
