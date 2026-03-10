def greet_user():
    print('fuck you')
greet_user()

def greet_user(user_name):
    print('hello, '+ user_name.upper())
greet_user('Li')

def favorite_book(book):
    print('your favoriate book is ' + book + '.')
favorite_book('700')

def pet(pet_type, pet_name):
    print('my pet\'s type is ' + pet_type) 
    print('my pet\'s name is ' + pet_name)
pet('swan', 'anna')
pet(pet_name='anna',pet_type='swan')

def pet(pet_name, pet_type = 'dog'):
    print('your ' + pet_type + '\'s name is ' + pet_name + '.')
pet(pet_name = 'jessy')
pet('jessy')

def name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.upper()
musician = name('Ziyuan','Li')
print(musician)

def name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    print(full_name.upper())
name('Ziyuan','Li')

def name(first,middle,last):
    if middle: # == if middle != ""
        full = first + ' ' + middle + ' ' + last
        return full
    else:
        full = first + ' ' + last
        return full
musician = name('ziyuan','oscar','li')
print(musician) 

def name(first, last):
    person={'first':first,'last':last}
    return person
people = name('ziyuan','li')
print(people)

def name(first, last):
    person={'first':first,'last':last}
    return person
while True:
    print('tell me your name.')
    print('enter q to quit')
    first=input('first name')
    if first == 'q':
        break
    last=input('last name')
    if last == 'q':
        break
    print(name(first,last))

def name(names):
    for name in names:
        msg = 'hello '+name
        print(msg)
names=[]
while True:
    print('tell me your name and enter q for quit.')
    first = input('what is your first name?')
    if first =='q':
        break
    last = input('what is your last name?')
    if last =='q':
        break
    full = first + last
    names.append(full)
name(names)


design=['A','B','C']
printed=[]
while design:
    zeigen = design.pop()
    print(zeigen)
    printed.append(zeigen)
for printe in printed:
    print('we have already printed ' + printe + '.')


def print_model(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('printing model: ' + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    print('schon ausgedrucket')
    for moddel in completed_models:
        print(moddel)
unprinted_designs = ['A','B','C']
completed_models = []

print_model(unprinted_designs,completed_models)
show_completed_models(completed_models)

#delete
print_model(unprinted_designs[:], completed_models)
