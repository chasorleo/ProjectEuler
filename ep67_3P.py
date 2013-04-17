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
#print dataMat

#Search############################################################
Sum = 0
LL = LR = RL = RR = 0
CL = 0  # CurrentLine
CO = 0  # ColumnOffSet
CC = 0  # CurrentColumn
tempMaxL = 0
tempMaxR = 0
tempMaxM = 0
ML = MM = MR = 0
Max = 0

while CL < Line - 2:
    Sum += int(dataMat[CL][CC])
    print 'dataMat[CL][CC]', dataMat[CL][CC]
    print 'CL', CL
    print 'Sum', Sum
#Calculate Path Sum and fin, out the laergest
    if CC == 0:
        LL = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC])
        LR = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC + 1])
        RL = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC])
        RM = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 1])
        RR = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 2])
        tempMaxL = 0
        tempMaxR = 0
        tempCO = 0
        if LL > LR:
            tempMaxL = LL
        else:
            tempMaxL = LR
        if RL > RM:
            tempMaxR = RL
        else:
            tempMaxR = RM
        if tempMaxR < RR:
            tempMaxR = RR
        if tempMaxL > tempMaxR:
            CO = 0
        else:
            CO = 1
    elif CC == 1:
        LM = int(dataMat[CL + 1][CC - 1]) + int(dataMat[CL + 2][CC - 1])
        LR = int(dataMat[CL + 1][CC - 1]) + int(dataMat[CL + 2][CC])
        ML = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC - 1])
        MM = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC])
        MR = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC + 1])
        RL = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC])
        RM = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 1])
        RR = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 2])
        if LM > LR:
            tempMaxL = LM
        else:
            tempMaxL = LR

        if ML > MM:
            tempMaxM = ML
        else:
            tempMaxM = MM
        if tempMaxM < MR:
            tempMaxM = MR

        if RL > RM:
            tempMaxR = RL
        else:
            tempMaxR = RM
        if tempMaxR < RR:
            tempMaxR = RR

        if tempMaxL > tempMaxM:
            Max = tempMaxL
            CO = -1
        else:
            Max = tempMaxM
            CO = 0
        if Max < tempMaxR:
            tempMaxR = tempMaxR
            CO = 1

    else:
        LL = int(dataMat[CL + 1][CC - 1]) + int(dataMat[CL + 2][CC - 2])
        LM = int(dataMat[CL + 1][CC - 1]) + int(dataMat[CL + 2][CC - 1])
        LR = int(dataMat[CL + 1][CC - 1]) + int(dataMat[CL + 2][CC])
        ML = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC - 1])
        MM = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC])
        MR = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC + 1])
        RL = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC])
        RM = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 1])
        RR = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 2])

        if LL > LM:
            tempMaxL = LL
        else:
            tempMaxL = LM
        if tempMaxL < LR:
            tempMaxL = LR

        if ML > MM:
            tempMaxM = ML
        else:
            tempMaxM = MM
        if tempMaxM < MR:
            tempMaxM = MR

        if RL > RM:
            tempMaxR = RL
        else:
            tempMaxR = RM
        if tempMaxR < RR:
            tempMaxR = RR

        if tempMaxL > tempMaxM:
            Max = tempMaxL
            CO = -1
        else:
            Max = tempMaxM
            CO = 0
        if Max < tempMaxR:
            tempMaxR = tempMaxR
            CO = 1
#Update CL and CO
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
#CC += CO
print 'After LAST the dataMat[CL][CC]', dataMat[CL][CC]
print 'After LAST', Sum
#if int(dataMat[CL + 1][CC]) > int(dataMat[CL + 1][CC + 1]):
#    Sum += int(dataMat[CL + 1][CC])
#else:
#    Sum += int(dataMat[CL + 1][CC + 1])
print Sum
