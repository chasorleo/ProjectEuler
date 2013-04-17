# Open data file
fob = open('nam_sort.txt', 'r')
b = fob.read()
#Build the data Matix
c = b.split()
print len(c)
sumposition = 0
for i in range(0, len(c)):
    print 'enter name loop', i
    sumsoreletter = 0
    for j in c[i]:
        print 'enter letter loop', j
        soreletter = 0
        if j == "A":
            soreletter = 1
        elif j == "B":
            soreletter = 2
        elif j == "C":
            soreletter = 3
        elif j == "D":
            soreletter = 4
        elif j == "E":
            soreletter = 5
        elif j == "F":
            soreletter = 6
        elif j == "G":
            soreletter = 7
        elif j == "H":
            soreletter = 8
        elif j == "I":
            soreletter = 9
        elif j == "J":
            soreletter = 10
        elif j == "K":
            soreletter = 11
        elif j == "L":
            soreletter = 12
        elif j == "M":
            soreletter = 13
        elif j == "N":
            soreletter = 14
        elif j == "O":
            soreletter = 15
        elif j == "P":
            soreletter = 16
        elif j == "Q":
            soreletter = 17
        elif j == "R":
            soreletter = 18
        elif j == "S":
            soreletter = 19
        elif j == "T":
            soreletter = 20
        elif j == "U":
            soreletter = 21
        elif j == "V":
            soreletter = 22
        elif j == "W":
            soreletter = 23
        elif j == "X":
            soreletter = 24
        elif j == "Y":
            soreletter = 25
        elif j == "Z":
            soreletter = 26
        sumsoreletter += soreletter
        print 'screletter is:', soreletter
    print 'sumsoreletter is:', sumsoreletter
    sumposition += (i + 1) * sumsoreletter
    print sumsoreletter
print c[0]
print c[0][0]
print sumposition
