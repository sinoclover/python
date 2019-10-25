# # 比较数字
# num1 = float(input('Enter the first number: '))
# num2 = float(input('Enter the second number:'))
# if num1 < num2:
#     print(num1, 'is less than', num2)
# elif num1 > num2:
#     print(num1, 'is greater than', num2)
# else:
#     print(num1, 'is equal to', num2)

# # 折扣问题
# price = float(input('Enter the price of the product: '))
# if price <= 10:
#     print('The discount of this product is 10%, and the final price is ', price * (1 - 0.1))
# else:
#     print('The discount of this product is 20%, and the final price is ', price * (1 - 0.2))

# # 用户筛选
# user = input('Enter your gender(f/m): ')
# if user == 'm':
#     print('Sorry, you are not fit for this project.')
# elif user == 'f':
#     age = float(input('Please enter your age: '))
#     if 10 < age < 12:
#         print('Yes, you are the one we found!')
#     else:
#         print('Sorry, you are not fit for this project.')
# else:
#     print('Wrong, please enter correct gender.')

# # 油箱问题
# size = int(input('Enter the size of your tank: '))
# persent = int(input('Enter the persent full of your tank: '))
# KmPerL = int(input('Enter the km per liter: '))
# print('''Size of tank: {0}
# persent full: {1}
# km per liter: {2}'''.format(size, persent, KmPerL))
# distance = (size * persent * 0.01 - 5) *  KmPerL
# print('You can go another', distance, 'km')
# if distance > 200:
#     print('''The next gas station is 200 km away
#     You can wait for the next station.''')
# else:
#     print('''The next gas station is 200 km away
#         Get gas now.''')

# # 密码问题1
# passcode = int(input('Please enter the passcode: '))
# if passcode == 123456:
#     print("You're in.")
# else:
#     print('Wrong, please try again.')

# # 密码问题2
# while True:
#     passcode = int(input('Please enter the passcode: '))
#     if passcode == 123456:
#         print("You're in.")
#         break
#     else:
#         print('Wrong, please try again.')





