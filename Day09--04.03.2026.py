message=input('tell me your name: ')
print(message)

message = 'if you tell me your name, i would appreaciate'
message += '\nwhat\'s your name?'
name=input(message) #打印message，等输入，赋值给name
print('your name is: '+ name)

message = 'how old are you?'
age=input(message)

age=input('how old are you?')
age=int(age)
print(age)
age > 15

4%3
4%9
4%2
del list
listlist=[]
list1=list(range(1,30,2))
list2=list(range(1,30,3))
for value1,value2 in zip(list1,list2):
    x=value1%value2
    listlist.append(x)
print(listlist)

number=int(input('if you tell me your age, i could judge if its odd or even'))
if number%2 == 0:
    print('your age is even')
else:
    print('your age is odd')

age = 5
while age < 18:
    print(f"your age is {age}, you can\'t drink or smoke.")
    age += 1

message1 = 'hi, i am your guidance, ask me anything you wanna to know: '
message1 += '\n if you don\'t have any more questions, enter quit.'
message2 = ""
message2 = (input(message1))
if message2 != quit:
    print(message2)
if message2 == quit:
    message2 = (input(message1))
    print('see you next time.')
    
