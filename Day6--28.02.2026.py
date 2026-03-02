#Review
title(),upper(),lower(), #type:ignore
rstrip(),lstrip(),strip() #type:ignore
M=['L','K','J']
M.append('H')
M.insert(0,'G')
print(M)
pop_M=M.pop(0)
print(pop_M)
M.remove('K')
del M[0]
sorted(M),M.sort(inverse=True),len(M),M.reverse()
P=pop_M[:]
for value in range(1,10,2):
    print(value)
O=list(range(1,5))
print(O)
I=[value**2 for value in range(2,100,2)]
print(I)
print(I[4:1156])
print(I[0:5])
U=(11,20)
import statistics
max(I),min(I),sum(I),print(statistics.variance(I))
car=1
car==1
car!=1
car,bike,bus=1,2,3
car==1 and bike == 2
car==1 and bike == 3
car==1 or bike == 3
for x in range(1,10,2):
    if x>0:
        print(x)
    if x==0:
        print(x+1)
    if x<0:
        print(x+2)
