
from time import time
start_time = time()


def GetDigit(n):
    diglist = []
    digit = 0
    remain = 0
    num = n
    l = len(str(n))
    for i in range(l - 1, -1, -1):
        digit = num / 10 ** i
        remain = num % 10 ** i
        num = remain
        diglist.append(digit)
    return diglist

biglist = []
for i in range(1, 6000000):
    sum = 0
    list = GetDigit(i)
    for j in list:
        sum += j ** 5
    if i == sum:
        biglist.append(sum)
print biglist
##for i in range(10000000, 10000000):
##    list = GetDigit(i)
##    sum = 0
##    for j in list:
##        sum += j ** 5
##    if sum == n:
##        print n
print time() - start_time, "seconds"
