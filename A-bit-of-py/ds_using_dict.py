# ab是地址（Address）簿（Book)的缩写
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com'
}

print("Swaroop's address is", ab['Swaroop'])

# 删除一对键值——值配对
del ab['Spammer']

print('\nThere are {0} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {0} at {1}'.format(name, address))

#添加一对键值——值配对
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

