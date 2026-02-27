#setting
menu={'apple':2,'mango':3,'peach':1,'banana':2,'orange':6}
request=['apple','orange','kiwi','peach']
absense=['peach']
kitchen=[]

#sort
lists=[request,absense,kitchen]
for part in lists:
    part.sort() 
menu= dict(sorted(menu.items()))

print(request)
print(menu)
print(absense)
print(kitchen)

#no request 
if len(request)==0:
    print("just have a try, don\'t hesitate.")
else:
    for fruit in request[:]: #requst vs absenes
        if fruit in absense:
            print(f'sorry, today we don\'t have {fruit}.')
            request.remove(fruit)
        elif fruit not in menu: #request vs menu
            print(f'sorry, an order for {fruit} is impossibe.')
            request.remove(fruit)

#final confirmation
    kitchen[:]=request[:]

#discount
    cost=0
    for fruit in request:
        cost += menu[fruit]
    if len(request) >= 3:
        cost=cost*0.9
    print(f'your order = {request}')
    print(f'costs= {cost}')


#wrong version:
#lists=[request,absense,kitchen]
#while len(lists) > 0:
#    for part in lists:
#        pop_lists=[]
#        lists[0].sort
#        pop_lists=lists.pop(0)
#print(pop_lists)

#lists[:]=pop_lists[:]
#menu=sorted(menu)
#lists.append(menu)
#lists=sorted(lists)
#print(lists,menu,request,absense)
#no request 
#if len(request)==0:
#    print("just have a try, don\'t hesitate.")
#
#requst vs absenes
#for i, fruit in request:
#    print(i,':',fruit)
#if i in absense:
#    print('sorry, today we don\'t have {i}.')
#    del request[i]
#elif i not in menu: #request vs menu
#    print('sorry, an order for {i} is impossibe.')
#    request.remove(i)

#final confirmation
#kitchen[:]=request[:]

#discount
#for fruit in request:
#    cost += request[fruit]
#if len(request) >= 3:
#    cost=cost*0.9
#print(request,cost)