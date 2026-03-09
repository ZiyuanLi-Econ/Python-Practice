alien={'color':'yellow','age':10}
print(alien['color'])
print(alien['age'])
alien={'color3':'green','color2':'yellow','color4':'pink','color1':'blue'}
alien=dict(sorted(alien.items()))
print(alien)

for key,value in alien.items():
    if value == 'pink':
        print(key)

alien['color5','color6']='red','grey'
alien['color5']='red'
alien['color6']='grey'
alien={}
alien['color']='red'
alien['color3']='red'
print('the alien is now '+ alien['color3'] + '.')
del alien['color3']

alien={
    'color1':'red',
    'color2':'blue',
    'color3':'pink',
}

print('my favoriate color is ' +
      alien['color3'].upper() +
      '.')

alien={'color3':'green','color2':'yellow','color4':'pink','color1':'blue'}
for key, value in alien.items():
    if key == 'color3':
        print(value)

for k,v in alien.items():
    print("\n"+  k,v)

alien={'color3':'green','color2':'yellow','color4':'pink','color1':'blue'}
alien=dict(sorted(alien.items()))
for k,v in alien.items():
    print('\ncolor: ' + k)
    print('value: ' + v)

for k,v in alien.items():
    print('the ' +
          k.title() + 
          ' is ' +
          v.title() +
          '.')

for k in alien.keys():
    print(k.title())
for v in alien.values():
    print(v.title())

for k in alien:
    print(k,v)

alien={'color3':'green','color2':'yellow','color4':'pink','color1':'blue'}
friends=['yellow']
wow_account,NONE_account = 0,0
for v in alien.values(): # take care: v doesnt represent for value but key, must append .values()
    if v in friends:
        print('WOW')
        wow_account += 1
    if v not in friends:
        print('NONE')
        NONE_account += 1
print(wow_account)
print(NONE_account)

alien=dict(sorted(alien.items()))
#or 
for value in sorted(alien.items()):
    print()

alien={'color3':'green','color2':'yellow','color4':'pink','color1':'yellow'}
for value in set(alien.values()):
    print (value)

alien_0={'C':'green'}
alien_1={'C':'pink'}
alien_2={'C':'yellow'}
aliens=[alien_0,alien_1,alien_2]
print(aliens)

aliens = []
for value in range (1,11):
    new_alien={'C':"black",'speed':f"{value}"}
    aliens.append(new_alien)
print (aliens)

for alien in aliens[:5]:
    print(alien)
for alien in aliens[0:3]:
    if alien['C'] == ['green']:
        alien['C'] == ['orange']
print(aliens)

pizza={'toppings':['cheese','beef']}
print(pizza['toppings'])
for key in pizza['toppings']:
    print(key)

users={
    'A':{
        'C':'WOW',
        'B':'OWO'
    },
    'D':{
        'C':'WWO',
        'B':'OOW'
    }
}
for B in users.values():
    print(B)
