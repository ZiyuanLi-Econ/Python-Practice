users = {
    'aeinstein':{
        'first':'swan',
        'last':'elk',
        'location':'princeton',
    },
    'murie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
    }
}

for username,userinfo in users.items():
    print('\nUsername: ' + username)
    Full_name = userinfo['first'] + userinfo['last']
    Location = userinfo['location']
    print('Full_name: ' + Full_name + '\nLocation: '  + userinfo['location'])

alien={}
for alien in alien[:3]:
    if alien['color'] == 'yellow':
        alien['color'] = 'grey'

for alien in alien[:3]:
    for key in alien:
        if key.startswith('color') and alien[key] == 'green':
            alien[key] = 'blue'
        if key.endwith('color'):
            print()

