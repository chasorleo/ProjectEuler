def Factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * Factorial(n - 1)
sum = 0
for i in str(Factorial(100)):
    sum += int(i)
print sum
