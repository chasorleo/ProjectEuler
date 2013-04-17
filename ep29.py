from time import time
start_time = time()
a = []
c = 0
l = 0
for i in range(2, 101):
    for j in range(2, 101):
        c = i ** j
        a.append(c)
a.sort()
print len(a)
## Remove Dup
l = len(a)
n = 0
while n < l - 2:
    m = n + 1
    rep = 0
    while m < l - 1:
        if a[n] == a[m]:
            rep += 1
        else:
            break
        m += 1
    k = 0
    while k < rep:
        a.pop(n + k)
        k += 1
    n += 1
    l = len(a)
print len(a)
print time() - start_time, "seconds"
