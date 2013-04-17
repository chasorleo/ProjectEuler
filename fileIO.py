#!/usr/bin/python

# Open a file
fo = open("ep67.txt", "r+")

#str = fo.next()
#print "Read String is : ", len(str)
#print "Type of str is : ", type(str)
#
#str = fo.next()
#print "Read String is : ", str
#
#position = fo.tell()
#print "Current file position : ", position
#print "Type of position is : ", type(position)
#
#str = fo.seek(0, 3)
#position = fo.tell()
#print "Current file position : ", position
#
#print "Read String is : ", str

l = 1
read = []
while l < 12:
    str = fo.next()
    read.append(str)
    l = l + 1
    print "read is ", read
print "read is ", read
print int(read[1: 10])
# Close opend file
fo.close()
