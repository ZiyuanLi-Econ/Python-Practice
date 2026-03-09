prompt = '\n tell me something, i will give it back to you:'
prompt += "\n enter 'quit' to end the program"
message = ''
while message != 'quit':
    message=input(prompt)
    if message != 'quit':
        print(message)

prompt = '\n tell me something, i will give it back to you:'
prompt += "\n enter 'quit' to end the program"
active= True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

prompt = '\nTell me your favoriate country in your mind'
prompt += "\n enter 'quit' to end the program"
for value in range(0,250):
    while True:
        city = input(prompt)
        if city == 'quit':
            break
        else:
            print(f'{city} is the NO.{value} in your mind')

count = 1
lists=[]
while count < 100:
    count += 1
    if count % 2 == 0:
        lists.append(count)
        continue
print(lists)

unconfirmed_users = ['ana','bnb','cnc']
confirmed_users = []
while unconfirmed_users:
    current_users = unconfirmed_users.pop()
    print('verifying user: ' + current_users)
    confirmed_users.append(current_users)
print(confirmed_users)
for name in reversed(confirmed_users):
    print(name)

pets = ['dog','cat','swan']
while 'cat' in pets:
    pets.remove('cat')
    print(pets)

answers={}
active = True
while active:
    name = input('what\'s your name?')
    answer = input('what\'s your favorite mountain?')
    answers[name]=answer
    question = input('finished? (yes/no)')
    if question != 'yes':
        continue
    else:
        active = False
        for key, value in answers.items():
            print(key + '\'s favorite mountain is ' + value)