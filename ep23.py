import EPpackage as e
abnd = []  # list of abandunt numbers
for n in range(1, 28123):
    if e.SPD(n) > n:
        abnd.append(n)
l = len(abnd)
print l
S_Of_2_Aband = []
last = 0  # last number of S_OF_2_Aband
for i in range(0, l):
    for j in range(0, l):
        sum = abnd[i] + abnd[j]
        if sum < 28124 and sum != last:
            S_Of_2_Aband.append(sum)
            last = sum
print len(S_Of_2_Aband)
