##like objects in js

contacts = {'Jason': '321', 'Frank': '789'}
jasons_phone = contacts['Jason']

print('Diall {} to call Jason'.format(jasons_phone))

contacts['Tony'] = ['753', '456']
print(contacts)

del contacts['Jason']
print(contacts)

for number in contacts['Tony']:
    print('Phone: {}'.format(number))


for name in contacts:
    print('The number for {0} is {1}.'.format(name, contacts[name]))

for person, phone_number in contacts.items():
    print('The number for {0} is {1}.'.format(person, phone_number))
