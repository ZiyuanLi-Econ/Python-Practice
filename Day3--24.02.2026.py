message=" zi "
print(message.rstrip())
print(message.lstrip())
print(message.strip())

age=23
print("happy "+str(age)+"rd birthday")

age="23"
print(int(age))

name="ziyuan"
print(name.lower())
print(name.upper())
print(name.title())
print("pp\npp\n\tll ")
print("let\'go")
0.2**0.1
0.2*0.1
0.2/0.1

courses=['public','micro','macro','math']
print(courses[1])
print(courses[1].upper())
print(courses[-2].upper())


courses=['public','micro','macro','math']
number=['1st','2nd','3rd','4th']
x,y=0,0
while x<4:
 message=("In " + number[0+y] +" semester, i will attend " + courses[0+x].title() + '.')
 print(message)
 x,y=x+1,y+1


k='llempirical'
courses[0]=k
print(courses)

courses.append('HISTORY'.title())
print(courses)
courses.insert(0,'english')
del courses[-1]

pop_courses = courses.pop(0)
print(courses.pop(0))
print("the first courses i have finshed is " + courses.pop(0))

x=0
while x<4:
 courses=['public','micro','macro','math']
 pop_courses=courses.pop(0+x)
 print(pop_courses.title())
 x=x+1

courses.remove('public')
print(courses)

courses=['public','micro','macro','math']
kkk='public'
courses.remove(kkk)
print(courses)

cars=['audi','bmw','toyoto','byd']
cars.sort(reverse=True)
print(cars)

sorted(cars)
print(cars)
sorted(cars,reverse=True)

cars.reverse()
print(cars)
len(cars)