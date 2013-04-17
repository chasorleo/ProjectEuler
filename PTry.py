from time import time
import EPpackage as EP
start_time = time()

list = []
for i in range(3, 10000000):
    dig = EP.GetDigit(i)
    sum = 0
    for j in dig:
        sum += EP.Factorial(j)
    if sum == i:
        list.append(i)
print list
print time() - start_time, "seconds"

