# Open data file
fob = open('ep81simple.txt', 'r')

Line = 5

b = fob.read()
#Build the data Matix
dataMat = [None] * Line
for i in range(Line):
    dataMat[i] = [None] * Line
c = b.split()
print c
n = 0
for i in range(0, Line):
    for j in range(0, Line):
        dataMat[i][j] = c[n]
        n = n + 1
print dataMat
#print dataMat

#Search############################################################
nR = nC = oR = oC = 0
RR = RD = DR = DD = 0
sum = 0
while nR < Line:
    sum += int(dataMat[nR][nC])
    RR = int(dataMat[nR][nC + 1]) + int(dataMat[nR][nC + 2])
    RD = int(dataMat[nR][nC + 1]) + int(dataMat[nR + 1][nC + 1])
    DR = int(dataMat[nR + 1][nC]) + int(dataMat[nR + 1][nC + 1])
    DD = int(dataMat[nR + 1][nC]) + int(dataMat[nR + 2][nC])
    if RR > RD:
        tempMaxR = RR
    else:
        tempMaxR = RD
    if DR > DD:
        tempMaxD = DR
    else:
        tempMaxD = DD
    if tempMaxR > tempMaxD:
        oR = 0
        oC = 1
    else:
        oR = 1
        oC = 0
    nR += oR
    nC += oC

print sum
#Update CL and CO
#     CL += 1
#     CC += CO
# print 'After WHILE the dataMat[CL][CC]', dataMat[CL][CC]
# print 'After WHILE', Sum
# # Tackle the last two lines, CL is the last second line
# CL -= 1
# LL = int(dataMat[CL + 1][CC]) + int(dataMat[CL + 2][CC])
# RR = int(dataMat[CL + 1][CC + 1]) + int(dataMat[CL + 2][CC + 2])
# if int(dataMat[CL + 1][CC]) > int(dataMat[CL + 1][CC + 1]):
#     if LL >= RR:
#         CO = 0
#         Sum += int(dataMat[CL + 1][CC])
#     else:
#         CO = 1
#         Sum += int(dataMat[CL + 1][CC + 1])
# else:
#     if LL >= RR:
#         CO = 0
#         Sum += int(dataMat[CL + 1][CC])
#     else:
#         CO = 1
#         Sum += int(dataMat[CL + 1][CC + 1])
# CL += 1
# CC += CO
# if int(dataMat[CL + 1][CC]) > int(dataMat[CL + 1][CC + 1]):
#     Sum += int(dataMat[CL + 1][CC])
# else:
#     Sum += int(dataMat[CL + 1][CC + 1])
# #CC += CO
# print 'After LAST the dataMat[CL][CC]', dataMat[CL][CC]
# print 'After LAST', Sum
# #if int(dataMat[CL + 1][CC]) > int(dataMat[CL + 1][CC + 1]):
# #    Sum += int(dataMat[CL + 1][CC])
# #else:
# #    Sum += int(dataMat[CL + 1][CC + 1])
# print Sum
