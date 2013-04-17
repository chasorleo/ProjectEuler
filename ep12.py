#file name Euler Project 12
n=int(raw_input('Input a integer to star :')
ps=[]
while len(ps)<500:
      ps=[]
      pp=n*(n+1)/2
      for a in range(1,pp/2+1):
      if pp%a==0:
      ps.append(a)
      print 'length is:',len(ps)
print 'Test Done! pp is:',pp
