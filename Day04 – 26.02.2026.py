title,lower,upper()
print ("ll\tll")
rstrip,;strip,strip()
str(), int()
M=['0','y','2','3']
print(M[1])
M[0]='N'
print(M)
M.append("K")
M.insert(0,"P")
del M[0]
M.remove('K')
M.sort(reverse=True)
M.reverse()
len(M)

magicians=["liu","oscar","swan"]
for magician in magicians:
    print(magician +", was a great trick")
    print("Thanks for you listening!")

for value in range(1,10):
    print(value)

numbers=list(range(1,6))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)


squared=list(range(1,20))
while len(squared) > 1:
        pop_squared=squared.pop(-1)
for values in range(2,20):
    squared.append(values**2)
print(squared)

for values in range(2,20):
     print(values)

min(Numbers)
max(Numbers)
sum(Numbers)


Numbers=list(range(1,20))
average = sum(Numbers)/len(Numbers)
variance_list=[]
variance = 0
N = len(Numbers)
for x in Numbers:
    variance += (x-average)**2 / (N-1) 
    variance_list.append(variance)
print(variance_list)
print(variance)

print(statistics.variance(Numbers))
import statistics
print(statistics.mean(Numbers))

trible=[value**3 for value in range(0,11)]
print(trible)
print(Numbers[:])

value=[]
for value_ in Numbers[:6]:
     value.append(value_)
print(value)

myfriend_value = value[:]
print(myfriend_value)

dimensions =(0,200)
print(dimensions)
dimensions.insert(0,100)

diemensions =(0,200)
for diemension in dimensions: 
     print(diemension)

xxx=list(range(1,10))
print(xxx)

xxxx=range(1,10)
print(xxxx)

valuess=[]
for value in range(1,10):
    valuess.append(value)
print(valuess)

valuess.insert(0,0)
len(valuess)

