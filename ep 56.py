t = p = 0
a = 0
b = 0
max = 0
for t in range(0, 100):
    for p in range(0, 100):
        sum = 0
        for i in str(t ** p):
            sum += int(i)
            if max < sum:
                max = sum
                a = t
                b = p
print max
