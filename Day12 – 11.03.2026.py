def pet(pet_type, pet_name):
    print()
pet(pet_type='',pet_name='')
def pet(pet_type, pet_name='daggo'):
    print(pet_type,pet_name)
pet('xxx')

def pet(last,first):
    last= input('last')
    first=input('first')
    full=last + first
    return full.upper()
pet('xxx','yyy')
def greet(names):
    for name in names:
        ms = 'love ' + name
        print(ms)
names = ['a','b','c']
greet(names)

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
print_models(unprinted_designs[:], completed_models) #type:ignore

def make_pizza(*toppings):
    print(toppings)
make_pizza('babara')
make_pizza('babara','lalara','mamara')

def make_pizza(size,*toppings):
    print('\nMaking a ' + str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)
make_pizza(12,'a','b','c')

def build_profile(first,last,**user_info):
    profile={}
    profile['first'] = first
    profile['last'] = last
    for k,v in user_info.items():
        profile[k] = v
    return profile
user_profile = build_profile('albert','einstein',
                             location = 'usa',
                             fach = 'physics')
print(user_profile)

def make_pizza(size,*toppings):
    print('making a ' + str(size) + '-inch pizzawith the following toppings:')
    for topping in toppings:
        print('-'+topping)

from module_name import first, last, second
from pizza import make_pizza as mp
mp(10,'ll')
mp(11,'pp')
from module_name import function_name as fn
from pizza import *
def function_name(pamameter,paramater_1='default value'):
    pass

