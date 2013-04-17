sum = 1
s_4 = 1
for n in range(1, 501):
    print 'n', n
    sum += 4 * s_4 + 20 * n
    print 'sum+', sum
    s_4 = s_4 + 8 * n
    print
print sum
