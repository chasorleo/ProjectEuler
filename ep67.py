# Open data file
fob = open('ep67.txt', 'r')

Line = 100

b = fob.read()

#Build the data Matix
dataMat = [None] * Line
for i in range(Line):
    dataMat[i] = [None] * Line
c = b.split()

n = 0
for i in range(0, Line):
    for j in range(0, i + 1):
        dataMat[i][j] = c[n]
        n = n + 1

#Search############################################################
Sum = 0
LL = LR = RL = RR = 0
CL = 0  # CurrentLine
CO = 0  # ColumnOffSet
CC = 0  # CurrentColumn

while CL < Line - 2:
    Sum += int(dataMat[CL][CC])
    print 'dataMat[CL][CC]', dataMat[CL][CC]
    print Sum
    #Calculate Path Sum and fin, out the laergest
    LL = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC])
    LR = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC + 1])
    RL = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 1])
    RR = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 2])
    tempMaxL = 0
    tempMaxR = 0
    tempCO = 0
    if LL > LR:
        tempMaxL = LL
    else:
        tempMaxL = LR
    if RL > RR:
        tempMaxR = RL
    else:
        tempMaxR = RR
    if tempMaxL == tempMaxR:
        print '!!!!!!!!!!!!!!!!!!!!!!!!!'
    if tempMaxL > tempMaxR:
        CO = 0
    else:
        CO = 1
    CL += 1
    CC += CO
print 'After WHILE the dataMat[CL][CC]', dataMat[CL][CC]
print 'After WHILE', Sum
# Tackle the last two lines, CL is the last second line
CL -= 1
LL = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC])
RR = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 2])
if int(dataMat[CL + 1][CC]) > int(dataMat[CL + 1][CC + 1]):
    if LL >= RR:
        CO = 0
        Sum += int(dataMat[CL + 1][CC])
    else:
        CO = 1
        Sum += int(dataMat[CL + 1][CC + 1])
else:
    if LL >= RR:
        CO = 0
        Sum += int(dataMat[CL + 1][CC])
    else:
        CO = 1
        Sum += int(dataMat[CL + 1][CC + 1])
CL += 1
CC += CO
if int(dataMat[CL + 1][CC]) > int(dataMat[CL + 1][CC + 1]):
    Sum += int(dataMat[CL + 1][CC])
else:
    Sum += int(dataMat[CL + 1][CC + 1])
print 'LAST', Sum
