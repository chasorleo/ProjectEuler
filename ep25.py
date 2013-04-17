import EPpackage
b = 0
n = 500
while b < 10 ** 1000:
    b = EPpackage.fiboGenTermsN(n)
    n += 1
print n
print b[-1]
